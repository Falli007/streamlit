import streamlit as st
import functions
 
todos = functions.get_todos()
 
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
 
st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")
 
# Use a for loop with enumerate to add unique keys to the checkboxes
for i, todo in enumerate(todos):
    st.checkbox(todo, key=f"checkbox_{i}")
 
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
 

print('Hello')

st.session_state