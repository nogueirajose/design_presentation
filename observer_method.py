# Observer Design Pattern Example in Python

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserverA(Observer):
    def update(self, message):
        print(f"ConcreteObserverA received message: {message}")

class ConcreteObserverB(Observer):
    def update(self, message):
        print(f"ConcreteObserverB received message: {message}")

# Example usage:
if __name__ == "__main__":
    subject = Subject()

    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.attach(observer_a)
    subject.attach(observer_b)

    subject.notify("Event 1")

    subject.detach(observer_a)

    subject.notify("Event 2")
