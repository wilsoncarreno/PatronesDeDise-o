class State:
    def handle(self):
        pass

class OnState(State):
    def handle(self):
        print("Encendido")

class OffState(State):
    def handle(self):
        print("Apagado")

class Context:
    def __init__(self, state):
        self.state = state
    def set_state(self, state):
        self.state = state
    def request(self):
        self.state.handle()

# Uso
ctx = Context(OffState())
ctx.request()
ctx.set_state(OnState())
ctx.request()
