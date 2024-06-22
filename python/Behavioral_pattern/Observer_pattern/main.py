from __future__ import annotations
from random import randrange
from typing import List


class Subject():

    _state: int = None

    _observers: List[Subject] = []

    def attach(self, observer: Subject) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Subject) -> None:
        self._observers.remove(observer)


    def notify(self) -> None:

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def execute_event(self) -> None:

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class ObserverA:
    def update(self, subject: Subject) -> None:
        print(f"ObserverA: Reacted to the event state of {subject._state}")


class ObserverB:
    def update(self, subject: Subject) -> None:
            print(f"ObserverB: Reacted to the event state of {subject._state}")


if __name__ == "__main__":
    # The client code.

    subject = Subject()

    observer_a = ObserverA()
    subject.attach(observer_a)

    observer_b = ObserverB()
    subject.attach(observer_b)

    subject.execute_event()
    subject.execute_event()

    subject.detach(observer_a)

    subject.execute_event()