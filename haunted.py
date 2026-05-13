# Haunted House
import time

inventory = []

def have_item(item_target):
  for item in inventory:
    if item == item_target:
      return True
  return False


def welcome():
  print("     __________| |____")
  print("    /                 \\")
  print("   /     Welcome to    \\")
  print("  /                     \\")
  print("  |   my    House!      |")
  print("  |     ____     ___    |")
  print("  |    |    |   |___|   |")
  print("__|____|____|___________|__")
  print("")
  time.sleep(1)
  comeIn = input("Do you want to come in (Y/N)?").upper()
  if comeIn=="Y":
    hall()
  else:
    gameOver()
 
def hall():
  print("--- You are entering the hall ---")
  print("")
  time.sleep(1)
  print("There are 7 doors for you to choose from:")
  print("")
  time.sleep(1)
  print(" - A door to the library (1),")
  print(" - A door to the main bedroom (2),")
  print(" - A door to the living room (3),")
  print(" - A door to the dining room (4),")
  print(" - A door to the kitchen (5),")
  print(" - The main door to leave the house (6).")
  print(" - A door to the basement (7).")
  time.sleep(2)
  whereTo = input("Where do you want to go? (1 to 7)")
  if whereTo=="1":
    library()
  elif whereTo=="2":
    bedroom()
  elif whereTo=="3":
    living_room()
  elif whereTo=="4":
    dining_room()
  elif whereTo=="5":
    kitchen()
  elif whereTo=="6":
    gameOver()    
  elif whereTo== "7":
    basement()
  #Add more elif statements here for options 3,4 and 5

def library():
  print("--- You are entering the library ---")
  print("")
  time.sleep(1)
  libraryanswer = input ("You see a book on a shelf that is slanted. Do you grab it? (Y/N)").upper()
  if libraryanswer=="Y":
    secret_door()
  else:
      hall()
     
     
def secret_door():
  print("--- You discover a secret door behind the shelf.")
  time.sleep(1)
  print("You walk in the room, and see a rock.")
  time.sleep(1)
  print("The rock has a rusted sword embedded into it.")
  time.sleep(1)
  print("You want to pull it out.")
  time.sleep(1)
  print("It accepts your soul and it comes out.")
  time.sleep(1)
  secretanswer = input("Do you try to pull the golden sword out? (Y/N)")
  if secretanswer=="Y":
    print("You have pulled out the legendary sword Excalibur and its Scabbard Avalon")
    time.sleep(1)
    print("Avalon will save you from shedding blood.(It will heal your wounds.)")
    time.sleep(1)
    print("Excalibur will disintegrate all your enemies.")
    inventory.append("Excalibur")
    time.sleep(1)
    print("")
    print("(SECRET ENDING) You have pulled the magic sword out!")
    print("(SECRET ENDING) You look behind you and see the monsters that were guarding the sword look at you with malice.")
    print("(SECRET ENDING) You somehow are a expert swordsman now just by holding the magic sword.")
    print("(SECRET ENDING) You defeat the monsters and you are filled with confidence.")
    hall()
  else:
    print("You decide not to pull the magic sword out.")
    print("You turn around to go back to the hall, but the monsters that were guarding the magic sword have grabbed you and killed you.")
 
 
def bedroom():
  print("--- You are entering the main bedroom ---")
  print("")
  time.sleep(1)
 
  if have_item("Excalibur"):
    print("You hold the light of your sword up and the Ghost disintergrates.")
    hall()
  else:
    bedroomanswer = input("You see a ghost with a knife standing above the bed. Do you run? (Y/N)")
    if bedroomanswer=="N":
      print("--- The ghost has killed you and possessed your body. --- ")
    else:
      hall()

def living_room():
  print(" --- You are in the living room ---")
  print("")
  print("Congrats! You have picked the only safe room.")
  print("How much luck do you have!?")
  LRanswer = input("Well? What do you want to do? Do you want to leave or keep going?")
  if LRanswer=="Leave":
    gameOver()
  elif LRanswer=="Keep going":
    hall()
  time.sleep(1)

def basement():
  print (" --- You are entering the basement ---")
  print("")
  time.sleep(1)
  print(" --- You walk into a party full of monsters, demons, and vampires. --- ")
  print("")
  print("All the monsters are fighting for the right to kill you.")
  print("A demon gives you the chance to live and tells you to pick one of three cards.")
  BTAnswer= input ("Do you pick card 1,2, or 3?")
  if BTAnswer=="1":
    print("You picked the correct card.")
    print("")
    print("The demon still gets angry and steals your soul.")
  else:
    print("You picked the wrong card.")
    print("The demon takes your soul.")
 
def dining_room():
  print("--- You are entering the dining room ---")
  print("")
  print("--- The door that you came in has locked. ---")
  print("")
  print("A note on the counter says that you have to answer an equation to leave alive.")
  print("")
  print("--- The equation is 2x+50=10 ---")
  time.sleep(1)
  DR_answer = input ("What is your Response?")
  if DR_answer =="-20":
    print("You are allowed to leave.")
    hall()
  else:
    print("You die of old age in that room.")

def kitchen():
  print("--- You are entering the kitchen")
  print("")
  print("--- There are 3 magic potions on the Kitchen Table. ---")
  print("")
  print("You have to pick the correct one or the ghost from the bedroom will be notified.")
  time.sleep(1)
  kitchenanswer = input ("Which potion do you choose? The First,Second,Or Third?")
  if kitchenanswer == "Third":
    print("You picked the correct one! You are allowed to Leave.")
    hall()
  else:
    print("Wrong potion!")
    print("")
    print("The Ghost runs from the bedroom to the kitchen and grabs you. He stabs you with his knife and you die.")
   
def gameOver():
  print("")
  print("You took the wise decision to leave the house while you are still alive! Very wise decision indeed.")
  print("")
  time.sleep(2)
  print("All the monsters in the Haunted house wave to you as you leave.")
  print("")
  print("Good bye and come back soon!")
 
 

 

#Main Program Starts Here
welcome()
 

