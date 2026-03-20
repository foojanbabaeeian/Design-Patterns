import abc
class UsableInterface(abc.ABC):
    @abc.abstractmethod
    def usable_method(self):
        pass