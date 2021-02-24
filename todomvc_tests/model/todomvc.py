from selene import have, command
from selene.support.shared import browser


class TodoMvc:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def open(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        app_loaded = "return $._data($('#clear-completed')[0], 'events')"\
                     ".hasOwnProperty('click')"
        browser.should(have.js_returned(True, app_loaded))
        return self

    def create(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').type(todo).press_enter()
        return self

    def given_opened_with(self, *todos: str):
        self.open()
        self.create(*todos)

    def should_have(self, *todos: str):
        self.todo_list.should(have.exact_texts(*todos))
        return self

    def start_editing(self, todo, new_text):
        self.todo_list.element_by(have.exact_text(todo)).double_click()
        return self.todo_list.element_by(have.css_class('editing'))\
            .element('.edit').with_(set_value_by_js=True).set_value(new_text)

    def edit(self, todo, new_text):
        self.start_editing(todo, new_text).press_enter()
        return self

    def edit_by_focus_change(self, todo, new_text):
        self.start_editing(todo, new_text).press_tab()
        return self

    def cancel_editing(self, todo, new_text):
        self.start_editing(todo, new_text).press_escape()
        return self

    def toggle(self, todo):
        self.todo_list.element_by(have.exact_text(todo)).element('.toggle').click()
        return self

    def should_have_completed(self, *todos: str):
        self.todo_list.filtered_by(have.css_class('completed'))\
            .should(have.exact_texts(*todos))
        return self

    def should_have_active(self, *todos: str):
        self.todo_list.filtered_by(have.no.css_class('completed'))\
            .should(have.exact_texts(*todos))
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def delete(self, todo: str):
        self.todo_list.element_by(have.exact_text(todo)).hover()\
            .element('.destroy').click()
        return self

    def should_have_items_left(self, count: int):
        browser.element('#todo-count strong').should(have.exact_text(str(count)))
        return self

    def should_be_empty(self):
        self.todo_list.should(have.size(0))
