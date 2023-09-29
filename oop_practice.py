from abc import ABC, abstractmethod

import config_dota2game


class Character(ABC):

    @abstractmethod
    def attack(self, other):
        pass

    def __init__(self, *, name: str, surname=None):
        self.name = name
        self.surname = surname or ''
        self.health_points = 100

    @property
    def is_alive(self):
        return self.health_points > 0

    def __str__(self):
        return f'{self.name}'

class Beast(Character):
    def __init__(self, name, surname):
        super().__init__(surname=surname, name=name)
        self.power = config_dota2game.BeastParametrs.POWER
        self.accuracy = config_dota2game.BeastParametrs.ACCURACY
        self.health_points = config_dota2game.BeastParametrs.HEALTH_POINTS

    def attack(self, other):
        raise NotImplemented


class Trolls(Character):
    def __init__(self, name):
        super().__init__(name=name)
        self.power = config_dota2game.TrollParametrs.POWER
        self.accuracy = config_dota2game.TrollParametrs.ACCURACY

    def attack(self, other):
        print(f'{self.name.title()} is attacking {other.name.title()}')
        if self == other:
            return 
        other.health_points -= self.power
        if not other.is_alive:
            print(f'{self} won')


troll = Trolls('Alex')
troll2 = Trolls('BOB')
troll.attack(troll2)

print(troll2.health_points, troll2.is_alive)
