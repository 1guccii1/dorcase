import streamlit as st
import json

# Load your JSON
with open("dor.json", "r") as f:
    data = json.load(f)

st.title("My Q&A App 🤖✨")

for q in data:
    st.subheader(f"Q: {q['question']}")
    st.write(f"A: {q['answer']}")
