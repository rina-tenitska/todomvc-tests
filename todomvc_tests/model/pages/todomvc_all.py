from selene import have
from selene.support.shared import browser
from todomvc_tests.model.controls.field import TextField


class TodoMvcAll:
    def visit(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        window_uploaded = "return $._data($('#clear-completed')[0], 'events')" \
                          ".hasOwnProperty('click')"
        browser.should(have.js_returned(True, window_uploaded))
        return self

    def visit_with(self, *todos: str):
        self.visit()
        new_todo = TextField.by('#new-todo')
        for todo in todos:
            new_todo.submit(todo)
        return self

    @property
    def collection(self):
        return browser.all('#todo-list>li')

    def create(self, *todos: str):
        new_todo = TextField.by('#new-todo')
        for todo in todos:
            new_todo.submit(todo)
        return self

    def assert_list(self, *todos: str):
        self.collection.should(have.exact_texts(*todos))
        return self

    def start_editing(self, todo, new_text):
        self.collection.element_by(have.exact_text(todo)).double_click()
        todo = TextField.by('.editing .edit')
        return todo.set_value(new_text)

    def edit(self, todo, new_text):
        self.start_editing(todo, new_text).submit('')
        return self

    def cancel_editing(self, todo, new_text):
        self.start_editing(todo, new_text).cancel()
        return self

    def complete(self, todo):
        self.collection.element_by(have.exact_text(todo))\
            .should(have.no.css_class('completed')).element('.toggle').click()
        return self

    def activate(self, todo):
        self.collection.element_by(have.exact_text(todo))\
            .should(have.css_class('completed')).element('.toggle').click()
        return self

    def assert_completed(self, todo: str):
        self.collection.element_by(have.exact_text(todo))\
            .should(have.css_class('completed'))
        return self

    def assert_active(self, *todos: str):
        for todo in todos:
            self.collection.element_by(have.exact_text(todo))\
                .should(have.no.css_class('completed'))
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def assert_all_completed(self):
        self.collection.should(have.css_class('completed'))
        return self

    def assert_all_active(self):
        self.collection.should(have.no.css_class('completed'))
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def delete(self, todo: str):
        self.collection.element_by(have.exact_text(todo)).hover()\
            .element('.destroy').click()
        return self
