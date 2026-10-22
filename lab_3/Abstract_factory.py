from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("You have created a Windows button.")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("You have created a Windows checkbox.")

class MacButton(Button):
    def paint(self):
        print("You have created a Mac button.")

class MacCheckbox(Checkbox):
    def paint(self):
        print("You have created a Mac checkbox.")

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

if __name__ == "__main__":
    app1 = Application(WindowsFactory())
    app1.paint()

    app2 = Application(MacFactory())
    app2.paint()