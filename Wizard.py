# import numpy library to use it for arrays
import numpy as np


# wizard class
class Wizard:
    # reading from file
    all_spells = np.loadtxt("spells.txt", usecols=range(0, 3), dtype='str')
    wizard_spells = []

    # constructor takes wizard's name as argument
    def __init__(self, name):
        # setting wizard's attributes
        self.name = name
        self.shield_limit = 3
        self.energy = 500
        self.health = 100
        for spell in self.all_spells:
            if spell[0] == "A" or spell[0] == self.name[0]:
                self.wizard_spells = np.append(self.wizard_spells, spell[1:])

        self.wizard_spells = self.wizard_spells.reshape(int(len(self.wizard_spells) / 2), 2)

    # performing spells on opponent
    def attack(self, spell, opponent_shield):
        # handling ValueError for the index of the spell
        try:
            # getting the index of the spell to know its power
            i = int(str(np.where(self.wizard_spells == spell))[8])
            power = int(self.wizard_spells[i, 1])

            # subtracting spell's power from wizard's energy
            self.energy = self.energy - power
            if self.energy < 0:
                self.energy = 0
                return 0
            if opponent_shield:
                return 0
            else:
                return power
        except ValueError:
            print("not spell")
            return -1

    # check for spell
    def is_spell(self, spell):
        try:
            return int(str(np.where(self.wizard_spells == spell))[8])
        except ValueError:
            print("not spell")
            return -1

    # energy getter
    def wizard_energy(self):
        return self.energy

    # health getter
    def wizard_health(self):
        return self.health

    # decrementing health
    def decrease_power(self, power_difference):
        if power_difference > self.health:
            self.health = 0
        else:
            self.health = self.health - power_difference
        return self.health

    # using the shield
    def shield_used(self):
        if self.shield_limit == 0:
            return -1
        else:
            self.shield_limit -= 1
            return self.shield_limit

    # print winner's name
    def winner(self):
        print(f"        {self.name} is winner ...")
