import streamlit as st
import functions

todos = functions.get_todos()
print(todos)


def add_todo():
    todo = st.session_state["new_todo"] + "\n" #get the value of "new_todo"(which is a key)
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) #checkbox(label:str, key:str|int)
    print(f"todo={todo}\n",f"checkbox = {checkbox}")
    if checkbox: #Any change to the page will result in the web.py to restart.
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun() #rerun the app.

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo') #on_change =add_todo (the method called when changed)
