class Memento:
    def __init__(self, state):
        self.state = state

class Editor:
    def __init__(self):
        self.state = ""
    def type(self, text):
        self.state += text
    def save(self):
        return Memento(self.state)
    def restore(self, memento):
        self.state = memento.state

# Uso
editor = Editor()
editor.type("Hola ")
saved = editor.save()
editor.type("Mundo")
editor.restore(saved)
print(editor.state)  # "Hola "
