// Implemented by Haotian Tang and Shang Yang.
// @article{lin2024qserve,
//   title={QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving},
//   author={Lin*, Yujun and Tang*, Haotian and Yang*, Shang and Zhang, Zhekai and Xiao, Guangxuan and Gan, Chuang and Han, Song},
//   year={2024}
// }
#include <torch/extension.h>

void gemm_forward_cuda(torch::Tensor _in_feats, torch::Tensor _kernel, torch::Tensor _wscales, torch::Tensor _ascales, torch::Tensor _w_szs, torch::Tensor _a_ssums, torch::Tensor _out_feats);