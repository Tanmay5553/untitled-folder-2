from abc import ABC,abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("Ican walk and run ")

class Snake(Animal):
    def move(self):
        print("i can crawl")

class Dog(Animal):
    def move(self):
        print("i can bark")

H=Human
H.move()

S=Snake
S.move()

D=Dog
D.move()