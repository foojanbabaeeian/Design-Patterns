import usable_interface
import adaptee
class Adapter(usable_interface.UsableInterface):
    def __init__(self):
        self._adapt = adaptee.Adaptee()

    def usable_method(self):
        return self._adapt.unusable_method()