class Strategy:
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    def execute(self, a, b):
        return self.strategy.execute(a, b)

# Uso
print(Context(AddStrategy()).execute(5, 3))
print(Context(MultiplyStrategy()).execute(5, 3))
