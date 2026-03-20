import json

def load(path):
    with open(path) as f:
        return [json.loads(line)["completion"] for line in f]

a = load("samples_deepseek-ai_DeepSeek-V3.jsonl")
b = load("samples_Qwen_Qwen3-Coder-30B-A3B-Instruct(1).jsonl")

same = sum([x == y for x, y in zip(a, b)])
print("相同条数:", same)