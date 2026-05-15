from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
print("first variable",os.environ["GROQ_API_KEY"])
print(os.getenv("GROQ_API_KEY"))


def get_llm():
    return ChatGroq(
        model_name="qwen/qwen3-32b",
        temperature=0.2
    )
# if __name__ == "__main__":
#     llm = get_llm()
#     response = llm.invoke(["Hello, how are you?"])
#     print(response)
x="https://www.unifiedremote.com/downloads"
y=10
x=10