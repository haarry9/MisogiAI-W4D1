from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    max_output_tokens=200,
    google_api_key=GEMINI_API_KEY
)

def get_mcp_answer(user_message: str) -> str:
    """
    Takes a user message and returns the Gemini response as a string.
    """
    message = [
        ("system",
         "You're a chatbot that specializes in answering questions about MCP servers. Your job is to assist the development team in learning about Model Context Protocol (MCP) and needs an intelligent Q & A chatbot that can answer questions about MCP concepts, implementation, best practices, and troubleshooting."
        ),
        ("user", user_message)
    ]
    ai_msg = llm.invoke(message)
    content = ai_msg.content
    if isinstance(content, list):
        # Join all string and dict (as str) elements
        return "\n".join(str(x) for x in content)
    return str(content)

if __name__ == "__main__":
    user_input = "What is MCP?"
    print(get_mcp_answer(user_input))