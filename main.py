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
    ["7", "8", "9", "➕"],
    ["4", "5", "6", "➖"],
    ["1", "2", "3", "✖"],
    ["0", "C", "=", "/"]
]

symbol_map = {
    "➕": "+",
    "➖": "-",
    "✖": "*",
    "➗": "/"
}

for row in buttons:
    cols = st.columns(4)
    for i, button in enumerate(row):
        if cols[i].button(button, use_container_width=True):
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
                  st.session_state["expression"] += symbol_map.get(button, button)

            st.rerun()
