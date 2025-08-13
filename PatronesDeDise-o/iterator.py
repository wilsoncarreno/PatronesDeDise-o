class MyIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
    def __next__(self):
        if self.index < len(self.items):
            val = self.items[self.index]
            self.index += 1
            return val
        raise StopIteration
    def __iter__(self):
        return self

for item in MyIterator([1, 2, 3]):
    print(item)
