from todomvc_tests.model import todos


def test_common_todo_functionality():
    todos.visit()

    todos.create('a', 'b', 'c')
    todos.assert_list('a', 'b', 'c')

    todos.edit_submit('b', 'b edited')

    todos.toggle('b edited')

    todos.clear_completed()
    todos.assert_list('a', 'c')

    todos.edit_cancel('c', 'to be canceled')

    todos.delete('c')
    todos.assert_list('a')
