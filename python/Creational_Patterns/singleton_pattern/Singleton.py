from threading import Lock
class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]



class Singleton(metaclass=SingletonMeta):
    value: str = None
    def __init__(self, value):
        self.value = value


