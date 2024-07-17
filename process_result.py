import os
from typing import List
import glob
from datasets import load_dataset
import json_lines
import json

def extract_log(files: List = [], output_file: str = 'qserve_result_all.jsonl'):
    result_line = []
    for f in files:
        with open(f, 'r') as data:
            for line in data.readlines():
                if 'question' in line:
                    result_line.append(line)
    with open(output_file, 'w') as result:
        result.writelines(result_line)

def match_medbench(result_all_file, medbench_folder, output_folder):
    result_all = dict()
    with open(result_all_file, 'rb') as f: 
        for item in json_lines.reader(f):
            result_all[item['question']] = item['answer']

    for test_file_path in sorted(glob.glob(os.path.join(medbench_folder, "**/*.jsonl"), recursive=True)):
        if test_file_path.endswith("提交结果示例.jsonl"):
            continue
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        predict_file_path = test_file_path.replace(medbench_folder, output_folder)
        predict_file_path = '/'.join(predict_file_path.split('/')[:-2]+predict_file_path.split('/')[-1:])

        if os.path.exists(predict_file_path) == True:
            print(f"{predict_file_path} is finish, continue")
            continue

        test_dataset = load_dataset(
            "json",
            data_files=test_file_path,
            split="train",
        )

        with open(predict_file_path, "w", encoding="utf8") as f:      
            for data in test_dataset:
                question = data['question']
                if question in result_all.keys():
                    data['answer'] = result_all[question]
                else:
                    assert 1 == 2, 'question not found!'
                f.write(json.dumps(data, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    if os.path.exists('qserve_result_20bv14.jsonl'):
        match_medbench('qserve_result_20bv14.jsonl', '/root/workspace/external_data/MedBench', 'MedBenchQoQResult20bv14')