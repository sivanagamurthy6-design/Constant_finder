import streamlit as st
from graph import build_graph

st.set_page_config(page_title="LangGraph Chatbot", layout="centered")
st.title("🤖 LangGraph Chatbot (GROQ + Memory)")

graph = build_graph()

# Plain-text memory
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat
for msg in st.session_state.messages:
    if isinstance(msg, str):
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg.content)

user_input = st.chat_input("Ask something...")

if user_input:
    # Store user text only
    st.session_state.messages.append(user_input)

    # Invoke LangGraph
    result = graph.invoke(
        {"messages": st.session_state.messages}
    )

    # Update memory
    st.session_state.messages = result["messages"]

    st.chat_message("assistant").write(
        result["messages"][-1].content
    )
x='Sivanaga bheemasinghi'