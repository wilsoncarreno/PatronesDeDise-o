class Subject:
    def __init__(self):
        self.observers = []
    def attach(self, obs):
        self.observers.append(obs)
    def notify(self, data):
        for obs in self.observers:
            obs.update(data)

class Observer:
    def update(self, data):
        print(f"Notificado con: {data}")

# Uso
s = Subject()
s.attach(Observer())
s.notify("Cambio en datos")
