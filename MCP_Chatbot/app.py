import streamlit as st
from main import get_mcp_answer
import re

st.set_page_config(page_title="MCP Q&A Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 MCP Q&A Chatbot")
st.markdown("""
Ask me anything about Model Context Protocol (MCP) servers! I can explain concepts, provide code examples, and help you troubleshoot.
""")

# Sidebar with MCP quick facts and example questions
with st.sidebar:
    st.header("MCP Quick Facts")
    st.markdown("""
- **MCP** stands for Model Context Protocol
- Used for model orchestration and context management
- Enables scalable, modular AI systems
- Common in distributed ML/AI infra
    """)
    st.header("Example Questions")
    st.markdown("""
- What is MCP?
- How do I implement an MCP server?
- Show a code example of MCP context passing
- What are common issues with MCP?
    """)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask a question about MCP...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("Thinking..."):
        answer = get_mcp_answer(user_input)
    st.session_state.chat_history.append(("bot", answer))

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant"):
            # Render code blocks if present
            code_blocks = list(re.finditer(r"```([\w]*)\n([\s\S]*?)```", msg))
            last_end = 0
            if code_blocks:
                for block in code_blocks:
                    # Text before code
                    if block.start() > last_end:
                        st.markdown(msg[last_end:block.start()])
                    lang = block.group(1) or None
                    code = block.group(2)
                    st.code(code, language=lang)
                    last_end = block.end()
                # Any text after last code block
                if last_end < len(msg):
                    st.markdown(msg[last_end:])
            else:
                st.markdown(msg) 