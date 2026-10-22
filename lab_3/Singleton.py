class Singleton:
    _instance = None

    def __init__(self):
        self.settings = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Singleton()
        return cls._instance

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key)


if __name__ == "__main__":
    a = Singleton.get_instance()
    b = Singleton.get_instance()

    a.set_setting("language", "ru")

    print("a is b:", a is b)
    print("Настройка через b:", b.get_setting("language"))