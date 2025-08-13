from abc import ABC, abstractmethod

# 1️⃣ Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# 2️⃣ Concrete Products for Windows
class WindowsButton(Button):
    def render(self):
        print("🪟 Rendering a Windows style button")

class WindowsCheckbox(Checkbox):
    def render(self):
        print("🪟 Rendering a Windows style checkbox")

# 3️⃣ Concrete Products for Mac
class MacButton(Button):
    def render(self):
        print("🍏 Rendering a Mac style button")

class MacCheckbox(Checkbox):
    def render(self):
        print("🍏 Rendering a Mac style checkbox")

# 4️⃣ Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# 5️⃣ Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# 6️⃣ Client Code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()

# 7️⃣ Example Usage
if __name__ == "__main__":
    print("Client: Windows UI")
    client_code(WindowsFactory())

    print("\nClient: Mac UI")
    client_code(MacFactory())
