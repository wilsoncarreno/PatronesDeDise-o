class SingletonMeta(type):
    """Metaclass that creates only one instance per subclass."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Base Singleton
class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key, None)

# Extended Singleton (subclass)
class AdvancedConfiguration(Configuration):
    def load_defaults(self):
        self.settings.update({
            "theme": "dark",
            "language": "en"  })

# Client code
config1 = AdvancedConfiguration()
config1.load_defaults()

config2 = AdvancedConfiguration()
config2.set("theme", "light")

print(config1.get("theme"))  # light (same instance)
print(config1 is config2)    # True
