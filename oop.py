from datetime import datetime

class Human:
    __population = 0
    DNA = 'XXX YYY'

    @classmethod
    def __increase_population(cls):
        cls.__population += 1

    @classmethod
    def __decrease_population(cls):
        cls.__population -= 1

    def __init__(self, name: str):
        self.name = name
        self.money = 0
        # self.__class__.__increase_population()
        Human.__increase_population()

    def __str__(self):
        return f'Human {self.name}'

    # def __repr__(self):
    #     return f'Human {self.name}'
    __repr__ = __str__

class Player(Human):
    def __init__(self, name: str, skills: list[str]):
        super().__init__(name=name)
        self.skills = skills

class SportTeam:
    def __init__(self, name: str, month_salary_one_person: int = 1000):
        self.name = name
        self.date = datetime.now()
        self.players: list[Human] = []
        self.money = 0
        self.month_salary_one_person = month_salary_one_person

    def __str__(self):
        return f'Team {self.name}'

    __repr__ = __str__

    def pay_salary(self) -> None:
        if len(self.players) * self.month_salary_one_person <= self.money:
            print('paying......')
            for player in self.players:
                player.money += self.month_salary_one_person
                self.money -= self.month_salary_one_person
        else:
            print('Not enough money')

    def fire(self, player: Human):
        self.players.remove(player)
        return self
team = SportTeam('Al-Nassr')

cr7 = Player(name='Cristiano Ronaldo', skills=['soccer'])
team.players.append(cr7)

team.pay_salary()
# team.money += 5000
# team.pay_salary()
print(cr7.DNA)

# sr = Human('Sergio-Ramos')
# team.players.append(sr)
# team.pay_salary()



# print(cr7)
# print(sr)
# print(cr7.name)
# print(team.name)
# print(team.date)
# print(team.players)
# print(team.money)
# print(team.money)
# print(team.fire(sr).fire(sr))
# print(team.players)
