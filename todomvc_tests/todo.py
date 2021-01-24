from selene.support.shared import browser
from selene import have


todo_list = browser.all('#todo-list>li')

todo_to_edit = todo_list.element_by(have.css_class('editing')).element('.edit')


def todo_in_query(todo: str):
    return todo_list.element_by(have.exact_text(todo))


def visit():
    browser.open('https://todomvc4tasj.herokuapp.com/')


def should_be_ready():
    window_uploaded = "return $._data($('#clear-completed')[0], 'events')" \
                      ".hasOwnProperty('click')"
    browser.should(have.js_returned(True, window_uploaded))


def create(*texts: str):
    for text in texts:
        browser.element('#new-todo').type(text).press_enter()


def assert_list(*texts: str):
    todo_list.should(have.exact_texts(*texts))


def edit(todo: str, new_text: str):
    todo_in_query(todo).double_click()
    todo_to_edit.type(new_text)


def edit_submit(todo: str, new_text: str):
    edit(todo, new_text)
    todo_to_edit.press_enter()


def complete(todo: str):
    todo_in_query(todo).element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def edit_cancel(todo: str, new_text: str):
    edit(todo, new_text)
    todo_to_edit.press_escape()


def delete(todo: str):
    todo_in_query(todo).hover().element('.destroy').click()
