# Some tasks:
这次的任务从周一开始弄，并且抽空就搞，我就不信还弄不完...

下面这个任务，预计给大家两周时间完成，本周交流时不要求完成，但需要汇报进展:

掌握如何调用api来用现有大模型评测benchmark

## 一、HumanEval Benchmark 简单介绍

HumanEval benchmark 是一个 代码生成能力评测数据集，由 OpenAI 提出，用来评估大模型写 Python 函数的能力。
它包含 164 个 Python 编程题，每个题目有：

* 函数签名
* docstring（题目描述）
* 单元测试

模型需要生成函数代码，然后运行测试，看是否通过。最终指标一般是 pass@k（例如 pass@1、pass@10）。

数据集：[humaneval: https://huggingface.co/datasets/openai/openai_humaneval ](https://huggingface.co/datasets/openai/openai_humaneval )
### * 目标一：在github上找到现有的评测代码，根据这个代码配置相应的环境

[1](https://chatgpt.com/s/t_69b2c65f15188191b75d6455784a45e8)

* 目标二：掌握多线程/异步的方式调用api
* 目标三：将推理的结果以json或jsonl的格式存储
* 目标四：评测至少三个大模型
五、一个很多人不知道的加分点

如果你想 做得更完整一点（老师会很满意），可以再跑一个模型做对比，比如：

DeepSeek-V3
vs
DeepSeek-Coder

或者：

temperature = 0.2
vs
temperature = 0.8

然后比较：

pass@1

这就是 benchmark 对比实验
