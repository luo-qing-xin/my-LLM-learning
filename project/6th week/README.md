# Some Tasks：
## Task 1: Benchmark
在 HumanEval 基准上评测 DeepSeek 系列模型，与技术报告评测结果对齐

测试集就像是一个针对AI的“闭卷考试”，题目是新的，没有在市面上流通的，考验真能力。

https://github.com/deepseek-ai/DeepSeek-V3?tab=readme-ov-file#4-evaluation-results

DeepSeek-V3 是一个 超大规模 MoE（Mixture-of-Experts，混合专家）语言模型,总参数量 671B，但每个 token 只激活 37B 参数，所以推理更高效

训练使用了 14.8 万亿 tokens

#### 1. Base Model 评测
Base Model 是“基础模型”，还没经过聊天对齐。它主要看语言能力、知识、代码、数学等基础水平。
* 通用知识与理解类(English)
* 代码能力(Code)
* 数学能力(Math)
* 中文能力(Chinese)
* 多语言能力
#### 2. Chat Model 评测
Chat Model 是经过对齐后的对话模型，更接近用户实际使用场景。

这部分的意义是：
看它在真实聊天、指令遵循、开放式问答、代码与数学综合能力上的表现。
* 英文知识与推理
  
GPQA-Diamond 59.1
GPQA 是高难度专业问答，通常很能拉开模型差距。
59.1 说明它在高难知识推理上具备很强实力。
IF-Eval 86.1
衡量指令遵循能力。
这说明它在理解用户要求、按格式执行任务方面比较可靠。
* 代码与软件工程能力
  
SWE Verified 42.0
这是软件工程任务，更接近真实修复代码问题。
这个成绩说明它在真实工程场景中也有较强能力，但和最顶级闭源模型相比仍有提升空间。

Aider-Edit / Aider-Polyglot
主要看代码编辑和多语言代码任务。
表现不错，说明它适合编程助手类应用。

* 数学能力
  
AIME 2024 39.2
这是非常难的美国数学邀请赛题目，39.2 很强。
说明它在高难度数学推理上已经接近顶尖水平。

MATH-500 90.2
这个结果尤其亮眼，说明它在标准数学测试里非常强。

CNMO 2024 43.2
中文奥数类任务表现也很好，说明它在复杂数学问题上具备较强能力。
* 中文能力
  
C-Eval 86.5
C-SimpleQA 64.8
说明它对中文知识问答、中文理解也很有竞争力。

* 开放式生成
  
Arena-Hard 85.5
AlpacaEval 2.0 70.0
这两个更接近“真实对话体验”评价。

尤其是 AlpacaEval 2.0 = 70.0 非常突出，说明：

语言生成质量高

回答更符合人类偏好

对话体验较好

https://github.com/deepseek-ai/DeepSeek-Coder

**这页在介绍 DeepSeek-V3 是一个参数规模极大、训练效率很高、在数学和代码上尤其强、并且整体性能已接近顶级闭源模型的开源 MoE 大语言模型。**

## Task 2: Paper Reading
#### 1. 读两篇论文并分享
bingqi       https://arxiv.org/pdf/2107.03374



[CSDN论文精读](https://blog.csdn.net/heroding23/article/details/133189960?

1. 真实场景下代码都是不断迭代debug的结果
2. <img width="1185" height="855" alt="image" src="https://github.com/user-attachments/assets/aa142575-9fd7-4bb1-b546-84d4b73fa4fc" />
3. 作者的代码lexer基于GPT-3文本的tokenizer实现。但是由于代码和文本分布不同，tokenizer并不高效，最大的根源来自于空格和空行，为此作者加入了额外的token集用于表示不同长度的空白，这使得作者能够少用30%的token来表示代码。

4. p值设为0.95。这是什么？？


5. *上图展示的是排序算法的性能，即允许模型生成k的答案，只是根据不同的策略和指标挑选最好的结果进行单元测试，Oracle虽然是最好的策略，但是在现实中，你不可能对每个方案都进行一次测试。因此相对比较合理的方案是对任何一个解，去看每个候选token在softmax中的概率取log算均值，将均值最高的选择出来相对性能较好*。没看懂

6. 用于Codex的监督微调，什么叫做监督微调？？

zilu            https://arxiv.org/abs/2108.07732

pinzheng   https://openreview.net/forum?id=chfJJYC3iL 

（如果能读一读审稿人意见和作者回复就更好了）

#### 2. 以及一篇自己找的论文
要求：2024年1月之后，与大模型、篮球相关（因为我们目前的研究方向是AI赋能篮球方面的）

问题：
1. 怎么解决谷歌学术在vpn的使用下无法进入的问题

#### 3. 分享读的论文
（用文档或者PPT记录，**一句话总结、研究背景和动机、研究方法、实验结果、价值和局限性**）

建议先自己读，再用大模型读，看写出来的东西有什么区别

