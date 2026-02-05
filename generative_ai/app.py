import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")
model = "deepseek-chat"

prompt = "完成下列句子：很久很久以前，有一个"
messages = [{"role": "user", "content": prompt}]

client = OpenAI(api_key=api_key, base_url=base_url)
response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=1024
)
print(response.choices[0].message.content)