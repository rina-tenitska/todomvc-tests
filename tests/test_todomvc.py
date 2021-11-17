from selene import be, have
from selene.support.shared import browser

todos = browser.all("#todo-list>li")


def test_crud_tasks_management():
    given_app_opened_with("a", "b", "c")
    todos_should_be("a", "b", "c")

    edit_with_enter("b", "b edited")

    toggle("b edited")
    clear_completed()
    todos_should_be("a", "c")

    cancel_edit_with_escape("c", "c to be canceled")

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


def test_adds_tasks():
    given_app_opened_with("a", "b", "c")
    todos_should_be("a", "b", "c")


def test_edits_task_with_enter():
    given_app_opened_with("a", "b", "c")

    edit_with_enter("b", "b edited")
    todos_should_be("a", "b edited", "c")


def test_edits_tasks_with_tab():
    given_app_opened_with("a", "b", "c")

    edit_with_tab("b", "b edited")
    todos_should_be("a", "b edited", "c")


def test_cancels_edit_tasks_with_escape():
    given_app_opened_with("a", "b", "c")

    cancel_edit_with_escape("b", "b edited")
    todos_should_be("a", "b", "c")


def test_tasks_count():
    given_app_opened_with("a", "b", "c")
    tasks_count_should_be(3)

    toggle("b")
    tasks_count_should_be(2)

    toggle_all()
    tasks_count_should_be(0)

    toggle_all()
    tasks_count_should_be(3)


def test_complete_tasks():
    given_app_opened_with("a", "b", "c")

    toggle("b")
    completed_tasks_should_be("b")

    toggle_all()
    completed_tasks_should_be("a", "b", "c")


def test_un_completes_task():
    given_app_opened_with("a", "b", "c")
    toggle("b")

    toggle("b")
    completed_tasks_should_be_empty()


def test_completes_all_tasks():
    given_app_opened_with("a", "b", "c")

    toggle_all()
    completed_tasks_should_be("a", "b", "c")


def test_un_complete_all_tasks():
    given_app_opened_with("a", "b", "c")
    toggle_all()

    toggle_all()
    completed_tasks_should_be_empty()


def test_deletes_task():
    given_app_opened_with("a", "b", "c")
    toggle("b")

    delete("b")
    todos_should_be("a", "c")


def test_clear_completed():
    given_app_opened_with("a", "b", "c")
    clear_completed_should(be.hidden)

    toggle_all()
    clear_completed_should(be.visible)

    clear_completed()
    clear_completed_should(be.hidden)


def test_clear_complete_all_tasks():
    given_app_opened_with("a", "b", "c")
    toggle_all()

    clear_completed()
    todos_should_be_empty()


def open():
    browser.open("http://todomvc4tasj.herokuapp.com")
    are_require_js_contexts_loaded = "return (Object.keys(require.s.contexts._.defined).length === 39"
    is_clear_completed_clickable = "$._data($('#clear-completed').get(0), 'events').hasOwnProperty('click'))"
    browser.should(have.js_returned(
        True, "{0} && {1}".format(are_require_js_contexts_loaded,
                                  is_clear_completed_clickable)))


def given_app_opened():
    if browser.config._source.has_webdriver_started():
        browser.clear_local_storage()
    open()


def given_app_opened_with(*texts):
    given_app_opened()
    add(*texts)


def add(*texts):
    for text in texts:
        browser.element("#new-todo").type(text).press_enter()


def todos_should_be(*texts):
    todos.filtered_by(be.visible).should(have.exact_texts(*texts))


def todos_should_be_empty():
    todos.should(have.size(0))


def start_editing(text, new_text):
    todos.element_by(have.exact_text(text)).double_click()
    return todos.element_by(have.css_class("editing")) \
        .element(".edit").with_(set_value_by_js=True).set_value(new_text)


def edit_with_enter(text, new_text):
    start_editing(text, new_text).press_enter()


def cancel_edit_with_escape(text, new_text):
    start_editing(text, new_text).press_escape()


def edit_with_tab(text, new_text):
    start_editing(text, new_text).press_tab()


def delete(text):
    todos.element_by(have.exact_text(text)).hover().element(".destroy").click()


def clear_completed():
    browser.element("#clear-completed").click()


def clear_completed_should(is_visible):
    browser.element("#clear-completed").should(is_visible)


def completed_tasks_should_be_empty():
    todos.filtered_by(have.css_class("completed")).should(be.empty)


def completed_tasks_should_be(*texts):
    todos.filtered_by(have.css_class("completed")) \
        .should(have.exact_texts(*texts))


def toggle(text):
    todos.element_by(have.exact_text(text)).element(".toggle").click()


def toggle_all():
    browser.element("#toggle-all").click()


def filter_all():
    browser.element("[href='#/']").click()


def filter_active():
    browser.element("[href='#/active']").click()


def filter_completed():
    browser.element("[href='#/completed']").click()


def tasks_count_should_be(tasks_count):
    browser.element("#todo-count>strong").should(
        have.exact_text(str(tasks_count)))
