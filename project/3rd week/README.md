# Some Exporation
这次是开学的第一周，还挺忙的，于是...把项目拖到了周末来做：

学习使用API的方式调用大模型：

我是使用的[硅基流动 (SiliconFlow)](https://cloud.siliconflow.cn/me/account/ak)的API（因为有16元的代金券嘻嘻）
硅基流动的 API 基础地址（固定值，无需修改）
    base_url="https://api.siliconflow.cn/v1"
    <img width="2202" height="150" alt="image" src="https://github.com/user-attachments/assets/c2cdddb7-5210-4bec-9257-5cc1b2b31ca9" />
代码如下：
```
from openai import OpenAI
client = OpenAI(
    api_key="sk-olcrkbxpwgseittqcnsqhokycublteikefzvehwhnjyslzma",
    base_url="https://api.siliconflow.cn/v1"
)
response=client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",#这个要去看文档，选择你需要的模型
    messages=[
        {"role": "system", "content": "你是我的人工智能助手，协助我解答问题和提供信息。"},
        {"role": "user", "content": "请介绍一下深度学习的基本概念。"}
    ],
    max_tokens=500,
    temperature=0.7
)
#关键字参数，Python 会根据参数名来识别，而不是根据位置。
print(response.choices[0].message.content)
```
* 探索1：了解API调用大模型的各个参数含义，可以通过寻找教程、阅读手册等


* 探索2：设计prompt，在鸢尾花数据集上完成分类，调整prompt查看区别
* 探索3：对比之前鸢尾花分类方法，代码实现逻辑上有何异同
* 探索4：使用GPT-2模型分类鸢尾花，对比当下先进的LLM（不局限在准确率上，所有的都可以分享）

可能使用到的资源：[https://www.volcengine.com](https://www.volcengine.com)

下阶段任务预告：Learn to Evaluate LLMs on HumanEval Code Generation Benchmark
（感兴趣可以先探索并分享一部分进展）
