""" Originally copied from the simpler https://www.geeksforgeeks.org/observer-method-python-design-patterns/"""
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Any, Callable


class EventTypeEnum(Enum):
	UPDATE_DATA = "UPDATE_DATA"


@dataclass()
class Event:
    """ The observer pattern can be even simpler without events just a notification """
    type: EventTypeEnum
    data: Optional[Any]
    source: "Observable" = None


Observer = Callable[[Event], None]


class Observable:
    def __init__(self):
        self._observers: List[Observer] = []

    def notify(self, event: Optional[Event]):
        """Alert the observers"""
        event.source = self
        for observer in self._observers:
            observer(event)

    # noinspection PyUnusedLocal
    def attach(self, observer: Observer, type: EventTypeEnum = None):
        """
            If the observer is not in the list, append it into the list
            we could also attach on a specific event
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """Remove the observer from the observer list"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class Data(Observable):
    """monitor the object"""

    def __init__(self, name=''):
        Observable.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: int):
        self._data = value
        self.notify(Event(type=EventTypeEnum.UPDATE_DATA, data=value))


def receive_from_data(event: Event):
    print(f"Received {event}")


if __name__ == "__main__":
    obj1 = Data('Data 1')

    obj1.attach(receive_from_data)

    obj1.data = 10
    obj1.data = 15
