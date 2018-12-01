
class Planet():

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    age = property()

    @age.setter
    def age(self, value):
        min_age = 100_000_000
        if value < min_age:
            self._age = min_age
        else:
            self._age = value

    @age.getter
    def age(self):
        return self._age

    @classmethod
    def test_method(cls):
        test_name = "test"
        test_color = "green"
        return cls(test_name, test_color)


earth = Planet("earth", "blue")

earth.age = 500_000
print(earth.age)

test_planet = Planet.test_method()
print(test_planet.color)

print(earth.__dict__)