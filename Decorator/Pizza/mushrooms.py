import decorator
class Mushrooms(decorator.Decorator):
    def get_price(self):
        return super().get_price() + .5

    def get_description(self):
        return super().get_description() + "+ Mushrooms "