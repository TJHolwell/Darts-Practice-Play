import streamlit as st

st.title("Darts Practice")


import random

def practice():
    target = random.randint(1, 20)
    multiplier = random.randint(1, 3)
    st.write(f"Target {target} on the board with a multiplier of {multiplier}")

def play():
    if 'total_player_One' not in st.session_state:
        st.session_state.total_player_One = 501
    if 'total_player_Two' not in st.session_state:
        st.session_state.total_player_Two = 501
    if 'turn' not in st.session_state:
        st.session_state.turn = 1

    st.write(f"Player One score: {st.session_state.total_player_One}")
    st.write(f"Player Two score: {st.session_state.total_player_Two}")

    if st.session_state.turn == 1:
        score_One = st.number_input("What is your score Player One:", min_value=0, max_value=180, step=1)
        if st.button("Submit Score Player One"):
            st.session_state.total_player_One -= score_One
            st.write(f"Player One you have: {st.session_state.total_player_One}")
            st.session_state.turn = 2
    else:
        score_Two = st.number_input("What is your score Player Two:", min_value=0, max_value=180, step=1)
        if st.button("Submit Score Player Two"):
            st.session_state.total_player_Two -= score_Two
            st.write(f"Player Two you have: {st.session_state.total_player_Two}")
            st.session_state.turn = 1

    if st.session_state.total_player_One <= 0 or st.session_state.total_player_Two <= 0:
        st.write("GAME OVER!", end=" ")
        if st.session_state.total_player_One <= 0:
            st.write("Player One wins!")
        elif st.session_state.total_player_Two <= 0:
            st.write("Player Two wins!")

st.title("Darts Game")

direct = st.radio("What are you planning on doing today?", ("Practice", "Play"))

if direct == "Practice":
    practice()
elif direct == "Play":
    play()

if st.button("Reset Game"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
