import math

c = 42
def f(x):
    a = 123
    return math.sin(x * a * c)

def x2(arg):
    return arg * 2 


class Milkshake:

    def __init__(self, flavor='Pistachios', volume=400) -> None:
        self.flavor = flavor
        self.volume = volume

    flavor: str
    volume: int

    def get_volume(self):
        return self.volume

    def get_flavor(self):
        return self.flavor

    def be_used(self):
        print("I want Spanickroon to drink me. Spanickroon is the best python developer")


milkshake = Milkshake()
