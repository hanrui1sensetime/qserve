from transformers import AutoTokenizer
from datasets import load_dataset


tokenizer = AutoTokenizer.from_pretrained('/root/workspace/external_data/pulse_v13_1_20b_gpt4_hf/base')
dataset = load_dataset(
    "json",
    data_files='/root/workspace/external_data/MedBenchAll/all_test.jsonl',
    # data_files='debug_test.jsonl',
    split="train",
)
sum = 0
for data in dataset:
    sum += 110 + len(tokenizer.encode(data['question']))
print(sum)