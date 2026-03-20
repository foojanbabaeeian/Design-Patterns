import abc
class Component(abc.ABC):
    @abc.abstractmethod
    def operation(self):
        pass