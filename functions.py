FILEPATH = "todo.txt"

def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_local:
        todos_local = [line.strip() for line in file_local.readlines()]
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
        