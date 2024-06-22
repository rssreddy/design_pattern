from Singleton import Singleton
from threading import Thread

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)

if __name__ == '__main__':
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()

