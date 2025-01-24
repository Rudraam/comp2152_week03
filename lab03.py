import random
#Dice options created using range() and list()
dice_options = list(range(1, 7))


#weapons list

weapons = ["Fist","Knife","Club","Gun","Bomb","Nuclear Bomb"]

print("Avaliable Weapons are: ", ' , '.join(weapons))

def getCombatstrength(prompt):
    while True:
        value = int(input(prompt))
        if 1<= value <= 6:
         return value
    else:
        print("Invalid input. Please enter a number between 1 and 6")

Combatstrength = getCombatstrength("Please enter a number between 1 and 6 for player")
mCombatstrength = getCombatstrength("Please enter a number between 1 and 6 for player")

for j in range(1, 21, 2): 
   heroRoll = random.choice(dice_options)
   monsterRoll = random.choice(dice_options)

   heroWeapon = weapons[heroRoll - 1]
   monsterWeapon = weapons[monsterRoll - 1]

   heroTotal = Combatstrength + heroRoll
   monsterTotal = mCombatstrength + monsterRoll

   print("\n Hero Rolled{heroRoll}, Monster rolled {mosterRoll}")
   print("\n Hero selected {heroWeapon}, Monster selected {monsterWeapon}")
   print("\n Hero total is {heroTotal}, Monster total is {monsterTotal}")

   if heroTotal > monsterTotal:
    print("Player won!")
   elif heroTotal < monsterTotal:
    print("Monster lost!")
   else:
    print("Match tie!")