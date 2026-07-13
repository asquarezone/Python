from typing import Protocol

class Walker(Protocol):
    def walk(self) -> None:
        ...

class Dog(Walker):
    def bark(self):
        print("bow bow" )

    def walk(self):
        print("dog is walking")

class Human(Walker):
    def cheat(self):
        print("cheater")


    def walk(self):
        print("human is walking")

class Toy(Walker):
    def walk(self):
        print("toy is walking")


class Robot(Walker):

    def power_on(self):
        print("robot is powered on")

    def power_off(self):
        print("robot is powered off")

    def walk(self):
        print("robot is walking")


def make_it_walk(walker):
    walker.walk()


if __name_ == "_main_":
    d = Dog()
    h = Human()
    r = Robot()
    t = Toy()

    make_it_walk(d)
    make_it_walk(h)
    make_it_walk(r)
    make_it_walk(t)

