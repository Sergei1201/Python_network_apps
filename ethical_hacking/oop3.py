class Monster:
    # Constructor
    def __init__(self, health, energy):
        self.health = health
        self.energy = self.set_energy(energy)
    
    # Methods
    def update_energy(self, amount):
        self.energy += amount
    
    def set_energy(self, energy):
        new_energy = energy * 5
        return new_energy
    
monster1 = Monster(30, 50)
print(monster1.energy)

