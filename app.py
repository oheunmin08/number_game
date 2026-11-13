import random
import streamlit as st
from number_utils import load_best, save_best

def new_game():st.session_state.answer = random.randint(1, 100)st.session_state.tries = 0st.session_state.msg = '1~100 사이의수를맞혀보세요!'st.session_state.done = Falseif 'answer' not in st.session_state:   # 처음접속했을때만new_game()