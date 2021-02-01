from todomvc_tests.model.pages.todomvc_all import TodoMvcAll


def test_create():
    TodoMvcAll().visit_with('a', 'b', 'c')
    TodoMvcAll().assert_list('a', 'b', 'c')


def test_edit():
    TodoMvcAll().visit_with('a', 'b', 'c')\
        .edit('b', 'b edited')
    TodoMvcAll().assert_list('a', 'b edited', 'c')


def test_cancel_editing():
    TodoMvcAll().visit_with('a', 'b', 'c')\
        .cancel_editing('b', 'to be canceled')
    TodoMvcAll().assert_list('a', 'b', 'c')


def test_complete():
    TodoMvcAll().visit_with('a', 'b', 'c')\
        .complete('b')
    TodoMvcAll().assert_completed('b')
    TodoMvcAll().assert_active('a', 'c')


def test_activate():
    TodoMvcAll().visit_with('a', 'b', 'c')\
        .complete('b')\
        .activate('b')
    TodoMvcAll().assert_active('a', 'b', 'c')


def test_complete_all():
    TodoMvcAll().visit_with('a', 'b', 'c')\
        .toggle_all()
    TodoMvcAll().assert_all_completed()


def test_activate_all():
    TodoMvcAll().visit_with('a', 'b', 'c')\
        .toggle_all()\
        .toggle_all()
    TodoMvcAll().assert_all_active()


def test_clear_completed():
    TodoMvcAll().visit_with('a', 'b', 'c')\
        .complete('b')\
        .clear_completed()
    TodoMvcAll().assert_list('a', 'c')


def test_delete():
    TodoMvcAll().visit_with('a', 'b', 'c')\
        .delete('b')
    TodoMvcAll().assert_list('a', 'c')
