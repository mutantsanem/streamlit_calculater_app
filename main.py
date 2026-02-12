import streamlit as st

st.title(" Calculator")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state["expression"] = ""

# Display expression
st.text_input("Expression", st.session_state["expression"], disabled=True)

# Button layout
cols = st.columns(4)

buttons = [
    "7", "8", "9", "plus +",
    "4", "5", "6", "minus -",
    "1", "2", "3", "multi *",
    "0", "C", "=", "divide /"
]

for i, button in enumerate(buttons):
    col = cols[i % 4]
    if col.button(button):
        if button == "C":
            st.session_state["expression"] = ""
        elif button == "=":
            try:
                st.session_state["expression"] = str(
                    eval(st.session_state["expression"])
                )
            except:
                st.session_state["expression"] = "Error"
        else:
            st.session_state["expression"] += button

        st.rerun() 
