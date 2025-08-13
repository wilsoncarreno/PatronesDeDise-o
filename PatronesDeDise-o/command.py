class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on()

class Light:
    def on(self):
        print("Light is ON")

# Uso
light = Light()
cmd = LightOnCommand(light)
cmd.execute()
