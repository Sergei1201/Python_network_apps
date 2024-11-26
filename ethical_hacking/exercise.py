class Hero:
    # Constructor
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster
    
    # Methods
    def attack(self):
        return self.monster.get_damage(self.damage)

    
class Monster:
    # Constructor
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    # Methods
    def get_damage(self, amount):
        self.health -= amount
        return self.health

monster = Monster(100, 50)
hero = Hero(25, monster)
print(hero.attack())
        

