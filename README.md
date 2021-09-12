# AhmedOsama_HarryPotterBattle
M.I.A offline training task 2

How it works:
- List of spells is given from a text file named `spells.txt` 
-	User is asked to enter two spells the first one is for Harry and the second is for Voldemort
-	We check if the spell belongs to each wizard’s allowed spells or not
    *	If yes then we get its power from the array of spells
    *	Else, the user is asked to try again
-	We calculate the power difference between spells as well as each wizard’s new energy
-	We subtract the power difference between spells from the health of the losing wizard
-	We print the results of the round
-	We repeat the previous steps again until one wizard has health = zero or become not able to duel (his energy = 0)
