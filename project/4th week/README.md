# Some tasks:
这次的任务从周一开始弄，并且抽空就搞，我就不信还弄不完...

下面这个任务，预计给大家两周时间完成，本周交流时不要求完成，但需要汇报进展:

## 掌握如何调用api来用现有大模型评测benchmark：

### 一、HumanEval Benchmark 简单介绍
HumanEval 是由 OpenAI 于 2021 年 7 月发布的代码生成能力评估基准，核心用途是客观衡量大型语言模型（LLM）从自然语言描述转换为可执行代码的能力，是目前代码生成模型评估的“行业标准”之一。其核心特点是聚焦“功能正确性”而非代码与参考示例的文本相似性，有 164 道人工精心设计的编程题目，每个题目有：
* 函数签名：包括task_id：任务唯一标识（如 HumanEval/0），用于区分 164 道不同题目，方便评估时定位具体任务及结果；
* docstring（题目描述）
* test（单元测试）：每道题平均包含 7.7 个手工设计的单元测试用例，用于验证生成代码的功能正确性，覆盖正常输入、边界情况、异常场景

模型需要生成函数代码，然后运行测试，看是否通过。最终指标一般是 pass@k（从模型生成的 k 个候选答案中，至少有 1 个是正确的概率。），例如 pass@1、pass@10

数据集：[humaneval: https://huggingface.co/datasets/openai/openai_humaneval ](https://huggingface.co/datasets/openai/openai_humaneval )
### * 目标一：在github上找到现有的评测代码，根据这个代码配置相应的环境

[相关步骤](https://chatgpt.com/s/t_69b2c65f15188191b75d6455784a45e8)

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
