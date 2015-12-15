import textwrap
import os
import pickle

todos = []

def main_loop():
    user_input = ""
    while 1:
        print run_command(user_input)
        user_input = raw_input("> ")
        if user_input.lower().startswith("quit"):
            print "Exiting..."
            break
        
def create_todo(todos, title, description, level):
    todo = {'title':title,
            'description':description,
            'level':level,}
    todos.append(todo)

def get_input(fields):
    user_input = {}
    for field in fields:
        user_input[field] = raw_input(field+" > ")
        print user_input
    return user_input

def get_function(command_name):
    return commands[command_name][0]

def get_fields(command_name):
    return commands[command_name][1]

def test(todos, abcd, ijkl):
    return "Command 'test' returned: "+\
           "abcd:"+abcd+" ijkl:"+ijkl

def run_command(user_input,data=None):
    user_input = user_input.lower()
    if user_input not in commands:
        return user_input+"?"+"I don't know what that command is."
    else:
        the_func = get_function(user_input)

    if data is None:
        the_fields = get_fields(user_input)
        data = get_input(the_fields)
    return the_func(todos, **data)

def capitalize(todo):
    todo['level'] = todo['level'].upper()
    return todo

def show_todo(todo, index):
    wrapped_title = textwrap.wrap(todo['title'], 16)
    wrapped_descr = textwrap.wrap(todo['description'], 24)
    output = str(index+1).ljust(8) + " "
    output += wrapped_title[0].ljust(16) + " "
    output += wrapped_descr[0].ljust(24) + " "
    output += todo['level'].ljust(16)
    output += "\n"

    max_len = max(len(wrapped_title),
                  len(wrapped_descr))

    for index in range(1, max_len):
        output += " "*8 + " "
        if index < len(wrapped_title):
            output += wrapped_title[index].ljust(16) + " "
        else:
            output += " "*16 + " "

        if index < len(wrapped_descr):
            output += wrapped_title[index].ljust(24) + " "
        else:
            output += " "*24 + " "
        output += "\n"
    return output

def sort_todos(todos):
    important = [capitalize(todo) for todo in todos
                 if todo['level'].lower() == 'important']
    unimportant = [todo for todo in todos
                   if todo['level'].lower() == 'unimportant']
    medium = [todo for todo in todos
              if todo['level'].lower() != 'important' and
              todo['level'].lower() != 'unimportant'
              ]
    todos = (important + medium + unimportant)
    return todos
    
def show_todos(todos):
    output = ("Item       Title        "
              "Description              Level\n")
    sorted_todos = sort_todos(todos)
    
    for index, todo in enumerate(sorted_todos):
        output += show_todo(todo, index)
    return output

def save_todo_list():
    save_file = file("todos.pickle", "w")
    pickle.dump(todos, save_file)
    save_file.close()

def load_todo_list():
    global todos
    if os.access("todos.pickle", os.F_OK):
        save_file = file("todos.pickle")
        todos = pickle.load(save_file)

todos = []
commands = {'new':[create_todo, ['title','description','level']],
            'show':[show_todos, []],
            'test':[test,['abcd','ijkl']]}

if __name__ == '__main__':
    main_loop()
    
