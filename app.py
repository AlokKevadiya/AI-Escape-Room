"""Run with: python -m streamlit run app.py"""
from dotenv import load_dotenv
import streamlit as st
from escape_room import v1
from escape_room.llm import ModelUnavailable
from escape_room.world import INTRO

load_dotenv()
st.set_page_config(page_title="The Locked Library", page_icon="🗝️")
st.title("The Locked Library")
st.caption("Version 1 • AI Game Master baseline")
if "history" not in st.session_state:
    st.session_state.history = [{"role": "assistant", "content": INTRO}]
if st.button("Restart game"):
    st.session_state.clear()
    st.rerun()
st.info("Explore with natural language. Examine objects, collect items and solve puzzles.")
for row in st.session_state.history:
    with st.chat_message(row["role"]):
        st.write(row["content"])
if message := st.chat_input("What would you like to do?", max_chars=500):
    try:
        with st.spinner("The Game Master is thinking…"):
            answer = v1.respond(st.session_state.history, message)
        st.session_state.history.extend([
            {"role": "user", "content": message},
            {"role": "assistant", "content": answer}])
        st.rerun()
    except ModelUnavailable as error:
        st.error(str(error))
