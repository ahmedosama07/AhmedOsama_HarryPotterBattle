# importing wizard class
from Wizard import Wizard

# creating two objects for the two wizards
harry = Wizard("Harry Potter")
voldemort = Wizard("Voldemort")

# game loop
while harry.health > 0 and voldemort.health > 0:
    # reading spells as input
    print("Enter the two spells (harry then voldemort)")
    harry_spell, voldemort_spell = input().split()

    # checking if spell is valid
    if harry.is_spell(harry_spell) == -1 or voldemort.is_spell(voldemort_spell) == -1:
        continue

    # checking if shield is used
    voldemort_shield = False
    harry_shield = False
    if harry_spell == "sheild":
        harry_shield_status = harry.shield_used()
        if harry_shield_status == -1:
            harry_shield = False
        else:
            harry_shield = True
    if voldemort_spell == "sheild":
        voldemort_shield_status = voldemort.shield_used()
        if voldemort_shield_status == -1:
            voldemort_shield = False
        else:
            voldemort_shield = True

    # power of the spell
    harry_attack_power = harry.attack(harry_spell, voldemort_shield)
    voldemort_attack_power = voldemort.attack(voldemort_spell, harry_shield)

    # wizard's energy
    harry_energy = harry.wizard_energy()
    voldemort_energy = voldemort.wizard_energy()

    # power difference between two spells
    power_difference = harry_attack_power - voldemort_attack_power

    # wizard's health
    harry_power = harry.wizard_health()
    voldemort_power = voldemort.wizard_health()

    # decrementing health
    if power_difference > 0:
        voldemort_power = voldemort.decrease_power(power_difference)
    elif power_difference < 0:
        harry_power = harry.decrease_power(abs(power_difference))

    # printing results
    print("         Harry                Voldemort")
    print(f"Health : {harry_power}                      {voldemort_power}")
    print(f"Energy : {harry_energy}                      {voldemort_energy}")


# game end
if harry.health == 0 and voldemort.health != 0:
    voldemort.winner()
elif harry.health != 0 and voldemort.health == 0:
    harry.winner()
