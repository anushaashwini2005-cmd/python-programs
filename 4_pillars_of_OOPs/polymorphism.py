class Dog:
    def sound(self):
        print("Dog says Woof!")

class Cat:
    def sound(self):
        print("Cat says Meow!")

class Cow:
    def sound(self):
        print("Cow says Moo!")
def make_sound(animal):
    animal.sound()
d = Dog()
c = Cat()
w = Cow()
make_sound(d)
make_sound(c)
make_sound(w)