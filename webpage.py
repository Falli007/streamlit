import streamlit as st
import functions as fn


todos = fn.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    fn.write_todos(todos)

    
st.title ('My To Do App')
st.subheader ('This is my To Do App')
st.write ('This App is to increase my productivity.')


# Display the todos list with checkboxes
for idx, todo in enumerate(todos):
    st.checkbox(todo, key=f"checkbox_{idx}")


st.text_input(label='', placeholder='Type your new todo here...', on_change=add_todo)
