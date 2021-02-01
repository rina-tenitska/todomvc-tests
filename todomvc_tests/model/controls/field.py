from selene import command
from selene.core.entity import Element
from selene.support.shared import browser


class TextField:
    def __init__(self, element: Element):
        self.element = element

    @staticmethod
    def by(selector: str):
        return TextField(browser.element(selector))

    def submit(self, text):
        self.element.type(text).press_enter()
        return self

    def set_value(self, text):
        self.element.perform(command.js.set_value(text))
        return self

    def cancel(self):
        self.element.press_escape()
