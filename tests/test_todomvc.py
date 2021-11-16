from selene import be, have
from selene.support.conditions.be import hidden, visible
from selene.support.shared import browser

todos = browser.all("#todo-list>li")


def test_todo_crud_management():
    given_app_opened_with("a", "b", "c")
    todos_should_be("a", "b", "c")

    edit("b", "b edited")

    toggle("b edited")
    clear_completed()
    todos_should_be("a", "c")

    cancel_edit("c", "c to be canceled")

    delete("c")
    todos_should_be("a")


def test_filters_tasks():
    given_app_opened_with("a", "b", "c")
    toggle("b")

    filter_active()
    todos_should_be("a", "c")

    filter_completed()
    todos_should_be("b")

    filter_all()
    todos_should_be("a", "b", "c")


def open():
    browser.open("http://todomvc4tasj.herokuapp.com")
    are_require_js_contexts_loaded = "return (Object.keys(require.s.contexts._.defined).length === 39"
    is_clear_completed_clickable = "$._data($('#clear-completed').get(0), 'events').hasOwnProperty('click'))"
    browser.should(have.js_returned(
        True, "{0} && {1}".format(are_require_js_contexts_loaded,
                                  is_clear_completed_clickable)))


def given_app_opened():
    browser.quit()
    open()


def given_app_opened_with(*texts):
    given_app_opened()
    add(*texts)


def add(*texts):
    for text in texts:
        browser.element("#new-todo").type(text).press_enter()


def todos_should_be(*texts):
    todos.filtered_by(be.visible).should(have.exact_texts(*texts))


def start_editing(text, new_text):
    todos.element_by(have.exact_text(text)).double_click()
    return todos.element_by(have.css_class("editing")) \
        .element(".edit").with_(set_value_by_js=True).set_value(new_text)


def edit(text, new_text):
    start_editing(text, new_text).press_enter()


def cancel_edit(text, new_text):
    start_editing(text, new_text).press_escape()


def delete(text):
    todos.element_by(have.exact_text(text)).hover().element(".destroy").click()


def clear_completed():
    browser.element("#clear-completed").click()


def toggle(text):
    todos.element_by(have.exact_text(text)).element(".toggle").click()


def filter_all():
    browser.element("[href='#/']").click()


def filter_active():
    browser.element("[href='#/active']").click()


def filter_completed():
    browser.element("[href='#/completed']").click()
