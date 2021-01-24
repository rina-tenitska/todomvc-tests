from todomvc_tests import todo


def test_common_todo_functionality():
    todo.visit()

    todo.should_be_ready()

    todo.create('a', 'b', 'c')
    todo.assert_list('a', 'b', 'c')

    todo.edit_submit('b', ' edited')

    todo.complete('b edited')

    todo.clear_completed()
    todo.assert_list('a', 'c')

    todo.edit_cancel('c', ' to be canceled')

    todo.delete('c')
    todo.assert_list('a')
