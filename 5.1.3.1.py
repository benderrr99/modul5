import random

class Fighter:
    def __init__(self, name, healt = 100):
        self.name = name
        self.healt = healt

    def fight(self, hit):
        if type(self) == type(hit):
            hit.healt -= 20
        else:
            raise TypeError

fighters = [Fighter('Ван Дам'), Fighter('Сталлоне')]
while True:
    i = random.randint(0, 1)
    attack, victim = fighters[i], fighters[i - 1]
    attack.fight(victim)
    print(attack.name, 'атаковал', victim.name)
    print('У', victim.name, 'осталось здоровья', victim.healt)
    if victim.healt <= 0:
        print(attack.name, 'победил!!!')
        break
