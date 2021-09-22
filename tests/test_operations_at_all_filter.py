from todomvc_tests.model import todomvc


def test_create_first_todo():
    todomvc.open()

    todomvc.should_be_empty()

    todomvc.create('a')

    todomvc.should_have('a')
    todomvc.should_have_items_left(1)


def test_create_many():
    todomvc.open()

    todomvc.create('a', 'b', 'c')

    todomvc.should_have('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_edit():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_edit_by_focus_change():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.edit_by_focus_change('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_cancel_editing():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.cancel_editing('b', 'to be canceled')

    todomvc.should_have('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_complete():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.toggle('b')

    todomvc.should_have_completed('b')
    todomvc.should_have_active('a', 'c')
    todomvc.should_have_items_left(2)


def test_activate():
    todomvc.given_opened_with('a', 'b', 'c')
    todomvc.toggle('b')

    todomvc.toggle('b')

    todomvc.should_have_active('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_complete_all():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.toggle_all()

    todomvc.should_have_active()
    todomvc.should_have_completed('a', 'b', 'c')
    todomvc.should_have_items_left(0)


def test_activate_all():
    todomvc.given_opened_with('a', 'b', 'c')
    todomvc.toggle_all()

    todomvc.toggle_all()

    todomvc.should_have_completed()
    todomvc.should_have_active('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_clear_completed():
    todomvc.given_opened_with('a', 'b', 'c', 'd')
    todomvc.toggle('b')
    todomvc.toggle('d')

    todomvc.clear_completed()

    todomvc.should_have('a', 'c')
    todomvc.should_have_items_left(2)


def test_delete():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.delete('b')

    todomvc.should_have('a', 'c')
    todomvc.should_have_items_left(2)


def test_delete_last_todo():
    todomvc.given_opened_with('a')

    todomvc.delete('a')

    todomvc.should_be_empty()
