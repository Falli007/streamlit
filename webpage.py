import streamlit as st
import functions as fn

todos = fn.get_todos()




st.title ('My To Do App')
st.subheader ('This is my To Do App')
st.write ('This App is to increase my productivity.')


# Display the todos list with checkboxes
for idx, todo in enumerate(todos):
    st.checkbox(todo, key=f"checkbox_{idx}")


