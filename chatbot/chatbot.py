import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

print("=== PLAIN CHATBOT ===")

question = input("You: ")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nChatbot:")
print(response.choices[0].message.content)