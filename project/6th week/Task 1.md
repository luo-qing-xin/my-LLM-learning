## Task 1: Benchmark
在 HumanEval 基准上评测 DeepSeek 系列模型，与技术报告评测结果对齐

测试集就像是一个针对AI的“闭卷考试”，题目是新的，没有在市面上流通的，考验真能力。

https://github.com/deepseek-ai/DeepSeek-V3?tab=readme-ov-file#4-evaluation-results

DeepSeek-V3 是一个 超大规模 MoE（Mixture-of-Experts，混合专家）语言模型,总参数量 671B，但每个 token 只激活 37B 参数，所以推理更高效,训练使用了 14.8 万亿 tokens
<img width="1108" height="396" alt="image" src="https://github.com/user-attachments/assets/ad5150c9-2301-4b43-b708-cb16570790a0" />
最初的v3版本在硅基流动上被下架了

```
models = [
    "deepseek-ai/DeepSeek-V3",
    "Qwen/Qwen3-Coder-30B-A3B-Instruct",
    "zai-org/GLM-4.6",
]
```
<img width="1105" height="299" alt="image" src="https://github.com/user-attachments/assets/793f8d3c-e29e-433c-a095-7fa28427dd50" />
<img width="994" height="657" alt="image" src="https://github.com/user-attachments/assets/97e51362-739a-4dd4-afac-32fcb0b0550d" />


而我使用的deepseek-ai/DeepSeek-V3是经过优化过的，所以正确率稍高应该正常
<img width="2129" height="274" alt="image" src="https://github.com/user-attachments/assets/110e2fd7-17e1-4bdf-9582-a062c27d7600" />


下面我要找一个经过humaneval测试（v3.2已经是livecodebench的测试集了）的大模型：





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
