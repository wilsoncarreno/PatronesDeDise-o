class AbstractClass:
    def template_method(self):
        self.step1()
        self.step2()

    def step1(self):
        pass
    def step2(self):
        pass

class ConcreteClass(AbstractClass):
    def step1(self):
        print("Paso 1")
    def step2(self):
        print("Paso 2")

# Uso
obj = ConcreteClass()
obj.template_method()
