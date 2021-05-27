class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SharedResources(metaclass=Singleton):

    def __init__(self):
        self.__attrs = {}

    def add_attribute(self, name: str, obj: object):
        self.__attrs[name] = obj

    def get_attribute(self, name: str):
        return self.__attrs[name]

    def __contains__(self, key):
        return key in self.__attrs
