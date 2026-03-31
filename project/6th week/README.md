# Some Tasks：

吕品正（me）  

[全文翻译](https://chat.deepseek.com/share/bngk595gw2mmcn51rt)

# [《LIVECODEBENCH》](https://openreview.net/forum?id=chfJJYC3iL )

## Abstract

#### 1. 问题背景
- 代码领域的大语言模型（LLMs）发展迅速  
- 现有评测基准（如 HUMANEVAL、MBPP）存在问题：
  - 数据污染（训练数据泄漏）
 
  LLM 是在海量且难以探查的语料库上训练的，当前的基准面临着数据污染的风险，因为训练数据可能包含这些基准样本。
  - 过拟合
  
   **过拟合Overfitting**是指：

模型在训练数据上表现很好，但在新数据（没见过的数据）上表现很差。

| 类型        | 特点          |
| --------- | ----------- |
| ✅ 正常（泛化好） | 学到规律，能处理新数据 |
| ❌ 过拟合     | 只记住训练数据     |
| ❌ 欠拟合     | 连训练数据都学不好   |


  - 难度饱和
  - 仅评测代码生成（不全面）

#### 2. 方法概述
提出新的评测基准：
> **LIVECODEBENCH（LCB）**

##### 核心特点
- 持续从真实平台收集新题：
  - LeetCode
  - AtCoder
  - Codeforces
- 保证评测数据“未被模型见过”（避免污染）
- 覆盖多种代码能力，而非单一生成任务

#### 3. 数据规模
- 题目数量：600+
- 时间范围：2023.05 – 2024.08
- 属于目前规模最大的代码评测之一

#### 4. 评测创新

##### 4.1 时间切片评测
- 使用模型训练截止时间之后的数据进行测试  
- 用于检测数据污染问题

##### 4.2 多维能力评测
评测四种能力：
- Code Generation（代码生成）就是按题目，AI写代码
- Self-Repair（代码修复）就是debug
- Code Execution（代码执行）在脑子里跑一遍代码，自己推理答案
- Test Output Prediction（输出预测）给题目和输入值，自己推理出答案
- 
后两项统称为AI的颅内思考

#### 5. 实验与发现
- 评测了 50+ 大语言模型
- 关键发现：
  - 可以有效检测数据污染
  - 传统 benchmark 存在过拟合
  - 多维评测更真实反映模型能力

#### 6. 一句话总结

> Livecodebench是一个  **动态更新 + 无污染 + 多能力评测** 的新一代代码大模型评测基准。

---
![0b596d97d9bb8bf9c14cb77382306000](https://github.com/user-attachments/assets/0cf86230-50cf-4f8a-9e51-1eccb44c56d2)
![becdbad4e44cd43df9079ae3f6591c3d](https://github.com/user-attachments/assets/7f9cf444-50b0-4cd8-99d4-336d745c79cc)
![40265a89f4703c302c323dceff1a5a30](https://github.com/user-attachments/assets/c043e34d-5e50-4850-b08d-a92cc8521b05)
![aca9d13d69de6aef06bcb1833c4ac81e](https://github.com/user-attachments/assets/649f585e-1352-4ee5-9d3a-440097ad97cd)





## 1. Introduction
一些背景+构建这个数据集的原则+一些发现的综述

原则如下：
* 实时更新以防止污染
- Avoid contamination by using newly released problems
- Evaluate models only on post-cutoff data
* 全面评估
- Code generation
- Self-repair
- Code execution
- Test output prediction
* 高质量的问题和测试
- Carefully filtered
- Rich test cases (avg >18)
* 难度引导的问题筛选
- Avoid too-hard problems
- Maintain meaningful model comparison
---
## 2. Motivation
---
## 3. Benchmark Overview
从三个竞赛网站上选，LeetCode，AtCoder，Codeforces

* 数据收集：写了自动化的 HTML 爬虫，解析数学公式并排除包含图像的问题，排除了不适合通过输入输出示例评分的问题
  
* 些评级将问题分类为 EASY、MEDIUM 和 HARD，以便进行更细粒度的模型比较，大致根据 HUMANEVAL 分数估算难度。
 
* 随时间推移滚动，根据模型发布时间来筛选问题
---

## 4. Evaluation Scenarios
模型:评估了 52 个不同规模的模型。从1.3B到70B（什么叫做B,是参数数量？？）

评估指标:
**使用pass@1指标**

我们使用温度为 0.2、top_p 为 0.95 的核采样

### 4.1 Code Generation
- Input: problem description
- Output: correct program
- 对于指令微调模型，我们使用零样本提示
- 基础模型使用单样本提示

### 4.2 Self-Repair
- Model fixes incorrect code using feedback，零样本提示

### 4.3 Code Execution
- Predict output of given code，使用少样本提示，有和没有思维链提示（什么叫做CoT？？）

### 4.4 Test Output Prediction
- Predict expected output from ，使用零样本提示，给定problem + input
---
## 5. Key Findings
### 5.1 Contamination Detection
- Performance drops after model cutoff dates
- Confirms training data leakage

- <img width="1127" height="807" alt="image" src="https://github.com/user-attachments/assets/3516b683-212e-412a-952a-fb1414991018" />


### 5.2 Holistic Capability Differences
- Models perform differently across tasks

### 5.3 HUMANEVAL Overfitting
- Some models perform well only on HUMANEVAL
- Poor generalization

### 5.4 Open vs Closed Models
- Closed models generally outperform
- Gap remains significant

---

## 6. Dataset Construction

### Data Collection
- Automated scraping
- Extract:
  - Problem statements
  - Test cases
  - Solutions

### Filtering
- Remove:
  - Multi-answer problems
  - Interactive tasks

---

## 7. Experimental Setup

### Models
- 50+ models
- Range: 1.3B → 70B

### Metric
- **PASS@1**

---

## 8. Conclusion

LIVECODEBENCH:
- Avoids contamination
- Provides holistic evaluation
- Enables more reliable benchmarking

---
##### 引言：评估方法却相对停滞
##### 方法：1.我们根据带有发布日期的标签来评估模型在新问题上的表现
2.我们使用自我修复场景评估基于执行反馈的多轮编码能力（没太看懂？？）
3.高质量的问题和测试，测试样例不足，他们通过实施启发式方法来检测和移除不适合基于输入输出自动评分的问题，提供了大量的测试用例。

#### 相关问题：
1. 什么是SQL
2. 用于压力测试解决方案？？hyw
3. 什么叫做过拟合（HUMANEVAL 过拟合）？？
4. 以进行鲁棒的对抗性测试for robust adversarial tests
   
## Task 1: Benchmark
在 HumanEval 基准上评测 DeepSeek 系列模型，与技术报告评测结果对齐

测试集就像是一个针对AI的“闭卷考试”，题目是新的，没有在市面上流通的，考验真能力。

但是目前，因为数据污染、过拟合、过饱和以及仅关注代码生成的问题，现有的评估基准（如HumanEvla、MBPP）已无法充分评估其能力。

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
（如果能读一读审稿人意见和作者回复就更好了）


谢秉奇       https://arxiv.org/pdf/2107.03374



[CSDN论文精读](https://blog.csdn.net/heroding23/article/details/133189960?

1. 真实场景下代码都是不断迭代debug的结果
2. <img width="1185" height="855" alt="image" src="https://github.com/user-attachments/assets/aa142575-9fd7-4bb1-b546-84d4b73fa4fc" />
3. 作者的代码lexer基于GPT-3文本的tokenizer实现。但是由于代码和文本分布不同，tokenizer并不高效，最大的根源来自于空格和空行，为此作者加入了额外的token集用于表示不同长度的空白，这使得作者能够少用30%的token来表示代码。

4. p值设为0.95。这是什么？？


5. *上图展示的是排序算法的性能，即允许模型生成k的答案，只是根据不同的策略和指标挑选最好的结果进行单元测试，Oracle虽然是最好的策略，但是在现实中，你不可能对每个方案都进行一次测试。因此相对比较合理的方案是对任何一个解，去看每个候选token在softmax中的概率取log算均值，将均值最高的选择出来相对性能较好*。没看懂

6. 用于Codex的监督微调，什么叫做监督微调？？
7. 作者构建环境让代码在沙盒中进行集成测试。？？hyw
8. 现在有一个观点是在大模型的更新迭代前少进行微调，先吃尽版本更新的红利。
9. 因为这些代码看起来会更加准确，用户难以识别出错误，可实际上已经做了有害的事情。，**这说明大模型也会出错！！！**

邱子路            [《Program Synthesis with Large Language Models》](https://arxiv.org/abs/2108.07732)

1. 什么叫做微调fine-tuning？？
2. 什么叫代码上的机器学习 

[论文摘要](https://zhuanlan.zhihu.com/p/1931417730176747302)



#### 2. 以及一篇自己找的论文
要求：2024年1月之后，与大模型、篮球相关（因为我们目前的研究方向是AI赋能篮球方面的）

问题：
1. 怎么解决谷歌学术在vpn的使用下无法进入的问题

#### 3. 分享读的论文
（用文档或者PPT记录，**一句话总结、研究背景和动机、研究方法、实验结果、价值和局限性**）

建议先自己读，再用大模型读，看写出来的东西有什么区别

