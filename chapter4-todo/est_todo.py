import todo
import os

def test_create_todo():
    todo.todos = []
    todo.create_todo(todo.todos,
                     title="Make some stuff",
                     description="Stuff needs to be programmed",
                     level="Important")
    assert len(todo.todos) == 1, "Todo was not created!"
    assert todo.todos[0]['title'] == "Make some stuff"
    assert todo.todos[0]['description'] == "Stuff needs to be programmed"
    assert todo.todos[0]['level'] == "Important"

    print "ok - create_todo"

def test_get_function():
    assert todo.get_function('new') == todo.create_todo
    print "ok - get_funtion"

def test_get_fields():
    assert (todo.get_fields('new') == ['title','description','level'])
    print "ok - test_get_fields"

def test_run_command():
    result = todo.run_command('test',{'abcd':'efgh','ijkl':'mnop'})
    expected = """Command 'test' returned: abcd:efgh ijkl:mnop"""
    assert result == expected,result+" != "+expected
    print "ok - run_command"

def test_show_todos():
    todo.todos = [{'title':'test unimportant todo',
                     'description':'a unimportant test',
                     'level':'Unimportant'},
                  {'title':'test medium todo',
                     'description':'a medium test',
                     'level':'Medium'},
                  {'title':'test important todo',
                     'description':'tan important test',
                     'level':'Important'}
                  ]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")
    print result

    first_line = lines[0]    
    assert "Item" in first_line
    assert "Title" in first_line
    assert "Description" in first_line
    assert "Level" in first_line

    secone_line = lines[1]
    assert "1" in secone_line
    assert "test" in secone_line
    assert "test" in secone_line
    assert "IMPORTANT" in secone_line

    print "ok - show_todos"                         

def test_todo_sort_order():
    todo.todos = [{'title':'test unimportant todo',
                     'description':'a unimportant test',
                     'level':'Unimportant'},
                  {'title':'test medium todo',
                     'description':'a medium test',
                     'level':'Medium'},
                  {'title':'test important todo',
                     'description':'tan important test',
                     'level':'Important'}
                  ]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")
    print result
    
    #assert "Unimportant" in lines[3]
    #assert "Medium" in lines[2]
    #assert "IMPORTANT" in lines[1]

def test_save_todo_list():
    todos_original = [{'title':'test important todo',
                     'description':'tan important test',
                     'level':'Important'}]
    todo.todos = todos_original
    print os.listdir('.')
    assert "todos.pickle" not in os.listdir('.')

    todo.save_todo_list()
    assert "todos.pickle" in os.listdir('.')

    todo.load_todo_list()
    assert todo.todos == todos_original
    os.unlink("todos.pickle")
    print "ok - save todo list"

def test_todo_sort_after_order():
    todo.todos = [{'title':'test unimportant todo',
                     'description':'a unimportant test',
                     'level':'Unimportant'},
                  {'title':'test medium todo',
                     'description':'a medium test',
                     'level':'Medium'},
                  ]
    todo.create_todo(todo.todos,
                     title="Make some stuff",
                     description="Stuff needs to be programmed",
                     level="Important")
    assert todo.todos[0]['level'] == "Important"
    assert todo.todos[1]['level'] == "Medium"
    assert todo.todos[2]['level'] == "Unimportant"
    
test_create_todo()
test_get_function()
test_get_fields()
test_run_command()
test_show_todos()
test_todo_sort_order()
#test_save_todo_list()
test_todo_sort_after_order()
