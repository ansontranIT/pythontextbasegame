#COSC1519 Introduction to Programming
#Student name: Anson Tran
#Student number: 3906959
#Practical group: 
# Monday 10:30am
#Coded in Python 3.9.4 on Microsoft Visual Studio
## Part 1 - Game Introduction
print("Oi, sellsword. Name. What's yer name?")
player_name = input("Name's ")
print(f"Right then {player_name}. What's yer profession?")

#Defining player's class + giving a unqiue response to each class
title_required = ("Please choose from A, B, C, or D")
title = ("Former Knight A), Monster Slayer B), Gladiator C), Thief D)")
print(title)
char_input = input(">")
if char_input == "A":
    print(f"{player_name} the Former Knight aye?",
    "Hah, what's a 'noble' like you doing out here with a bunch of cutthroats? Hahahhahah!")
    pname = (f"{player_name} the Former Knight") 
elif char_input == "B":
    print(f"{player_name} the Monster Slayer aye?",
    "I see we have a professional admist our rabble.")
    pname = (f"{player_name} the Monster Slayer") 
elif char_input == "C":
    print(f"{player_name} the Gladiator aye?",
    "A gladiator I see. What? No challenge in the arena so you hunt monsters now?")
    pname = (f"{player_name} the Gladiator") 
elif char_input == "D":
    print(f"{player_name} the Thief aye?",
    "Aaa, a fellow, a pal. Don't worry 'friend', I'll keep an eye out for ye")
    pname = (f"{player_name} the Thief") 
else:
    print(title_required)

## Part 2 - Adventure
print(f"Alright here's the contract {pname}\n",
"Out with ye I got more customers to serve, take some rations while you're at it.")
print("You see.")
#Nested For loop for ration generation
ration_colour = ["red", "green", "blue"]
ration_size = ["small", "medium", "large"]
for x in ration_colour:
    for y in ration_size:
        print(x, y)
r_number = int(input("How many take do you take? Insert an Integer"))
colour_input = input("Which ones do you take")

print("The contracter waves you away. Reading through the contract, there have been sightings of an unknown monster terrorising the outskirts of the city.")
if r_number > 1 and input == "red":
    print("You take", r_number, "red rations.")
else:
    print("You take", r_number, "assorted rations.")

#Player chooses where they want to go from a list of locations
def location_input():
    """ Player inputs where they want to go"""
    
    print("The Woodcutter's Hut A)", "The Trapper's Home B)", 'The Old Abandoned House on the Outskirts C)', 'Out into the forest D)')
    location = input('Where do you want to check out first?')
    if location == "A":
        print("You begin making your way towards the Woodcutter's Hut")
        lo = ("Woodcutter's Hut")
    elif location == "B":
        print("You begin making your way towards the Trapper's Home")
        lo = ("Trapper's Home")
    elif location == "C":
        print("You begin making your way towards the Old Abandoneed House on the Outskirts")
        lo = ("Abandoned House on the Outskirts")
    elif location == "D":
        print("You begin making your way towards the Forest")
        lo = ("Forest")
    else:
        print('Choose where you want to go')
        location_input()

location_input()
## Part 3 - Repetitive Actions
print('You begin heading off to your location.\n'
'Times passes until you reach your destination It is a long trip.\n'
'Finally you made it.\n')
travel_length = float(input("How many hours have you traveled? Insert a float"))
print(f"You've traveled for {travel_length} hours")
print('You see nothing out of the ordinary after getting there. But feel something in the air.\n'
'Suddenly you hear the loud screeching sound of a ghoul\n')

#A simple while loop for combat segment. Player chooses an attack that hits for 5 damage
# until the HP hits 0
def combat():
    """ This is the combat system where the user inputs a letter corresponding to an attack """
    actions = ["Strike A", "Thrust B", "Pommel C"]
    for y in actions:
          print(y)
    com_health = 30
    while (com_health > 0):
      combat_input = input("What do you do?")
      if combat_input == "A":
        com_health = com_health - 5
        print("You strike the creature dealing 5 damage")
        print("Ghoul Health: ", com_health)
      elif combat_input == "B":
        com_health = com_health - 5
        print("You thrust at the creature dealing 5 damage")
        print("Ghoul Health: ", com_health)
      elif combat_input == "C":
        com_health = com_health - 5
        print("You pommel the creature dealing 5 damage")
        print("Ghoul Health: ", com_health)
      else:
        print("Choose a correct action")
        combat()
    print("You killed the creature")
combat()
## Part 4 - Final Scene 
ending = ('\nHaving the head of a ghoul as proof of your work and your payment.\n'
'A job well done and a reward for your troubles.\n'
'However more work needs to be done.\n')

## Part 5 - Ending

reward_list = ['New Sword A', 'New Shield B', 'New Bow C']
print("Returning to the contractor with the Ghoul's head he gives you a choice of rewards\n",
    "What do you pick?")
for x in reward_list: 
    print(x)
treasure = input(">")
if treasure == "A":
    print(ending)
elif treasure == "B":
    print(ending)
elif treasure == "C":
    print(ending)
else:
    print('Choose your reward')





