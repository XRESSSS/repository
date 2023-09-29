import datetime
import time
from abc import ABC, abstractmethod

class Mammal(ABC):
    def drink(self):
        print('I am drinking')

    @abstractmethod
    def run(self, name):
        pass

class Cow(Mammal):
    def run(self, name):
        print(f'Cow {human} is running')

class Human(Mammal):
    def __init__(self):
        self.birth = datetime.datetime.now()
        print(self.birth)
        self.money = 0

    @property
    def age(self):
        return datetime.datetime.now() - self.birth


    def run(self, name):
        print(f'Human {human} is running very slow')

# mammal = Mammal()
cow = Cow()
human = Human()
human.money += 5000
print(human.__dict__)

cow.drink()
human.drink()
time.sleep(2)
print(human.age)

# mammal.drink()
cow.run('Bobik')
human.run('Alex')
