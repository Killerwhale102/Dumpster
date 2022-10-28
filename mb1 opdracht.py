import time 


def death():
    time.sleep(1)
    print(""" 
                              .___.
          /)               ,-^     ^-. 
         //               /           \ 
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\               \    /|\    /
          \)               \   \_/   /
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^
""")
    time.sleep(1)
    print("You died")
    exit()


def win():
    time.sleep(1)
    print("""
 __     __                    _       
 \ \   / /                   (_)      
  \ \_/ /__  _   _  __      ___ _ __  
   \   / _ \| | | | \ \ /\ / / | '_ \ 
    | | (_) | |_| |  \ V  V /| | | | |
    |_|\___/ \__,_|   \_/\_/ |_|_| |_|
                                      
    """)
    exit()
    

def intro():
    print("\nThe story opens with an Imperial wagon driving four prisoners down a snowy mountain pass. All are seated and bound; the one dressed in finery is gagged.\n")
    time.sleep(1.0)
    print("Hey, you. You're finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there, One says.")
    time.sleep(1.0)
    print("Shut up back there! An Imperial Soldier shouts from the front of the cart\n")
    time.sleep(1.0)
    print("You and the other prisoners arrive at a camp.")
    time.sleep(1.0)
    print("Do you choose to stay in line or try to run away?")

    choice_1 = input

    while choice_1 != "stay" or "run":
        time.sleep(1)
        choice_1 = input("stay or run >> ")
        if choice_1 == 'stay':
            story1()
        
        elif choice_1 == 'run':
            print("You try to run away byt got shot by the archers.")
            death()

        else:
            print("Do you choose to stay in line or try to run away.")


def story1():
    print("\nYou are pushed down on the beheading block.")
    time.sleep(1)
    print("Suddenly a dragon appears in the sky and starts razing the city.")
    time.sleep(1)
    print("You stand up and decide what to do.\n")
    print("Choose between following the soldiers, prisoners or try to escape alone.")
    time.sleep(1)

    choice_2 = input

    while choice_2 != "soldiers" or "prisoners" or "alone":
        choice_2 = input("soldiers, prisoners or alone")
        if choice_2 == "soldiers":
            time.sleep(1)
            soldiers()

        elif choice_2 == "prisoners":
            time.sleep(1)
            print("You follow the prisoners and seek shelter in the half burned down barracks.")
            prisoners()

        elif choice_2 == "alone":
            time.sleep(1)
            print("You dicide to go alone. You run and hide into the nearby shed")
            alone()

        else:
            print("Choose between following the soldiers, prisoners or try to escape alone")


def soldiers():
    print("\nYou follow the soldiers into the the tower to seek shelter.")
    time.sleep(1)
    print("You grab a sword and continue furhter into the castle.")
    time.sleep(1)
    print("A soldier opens a door and gets jumped by the prisoners with shivs.\n\nHey you, one scream. You're a traitor. He promply starts swinging his sword towards you.")
    time.sleep(1)
    print("Choose between trying to fight him or trying to dodge")

    choice_3 = input

    while choice_3 != "fight" or "dodge":
        choice_3 = input("fight or dodge >> ")
        if choice_3 == "fight":
            time.sleep(1)
            print("\nYou try to fight but unfortunately you're weak as fuck and get killed instantly.")
            time.sleep(1)
            death()
        
        elif choice_3 == "dodge":
            time.sleep(1)
            print("\nYou dodge out of the way and push the attacker into the soldiers. They kill him and start taking care of the others.")
            time.sleep(1)
            print("After the battle you are finally free and the soldiers let you go for helping them.")
            win()



def prisoners():
    time.sleep(1)
    print("Inside the barracks a prisoner named Rolaf helps you cut the rope binding your hands together")
    time.sleep(1)
    print("The group then proceeds to hear the clacking sounds of gears turning.\n\nYou turn towards the door which slowly opens, from within several soldiers appear.")
    time.sleep(1)
    print("Do you fight with the group, flee or try to solo?")

    choice_3 = input

    while choice_3 != "fight" or "flee" or "solo":
        choice_3 = input("fight, flee or solo >> ")
        if choice_3 == "fight":
            time.sleep(1)
            print("\nYou all scream your battlecries and proceed to ambush the soldiers")
            prisoners2()

        elif choice_3 == "flee":
            time.sleep(1)
            print("\nYou cowardly run away not looking back at the people that just helped you")
            time.sleep(1)
            print("You find youself outside, the dragon roars above you.\nYou run towards a shed that you have seen earlier.")
            time.sleep(1)
            alone()

        elif choice_3 == "solo":
            time.sleep(1)
            print("Like an absolute buffoon you charge all soldiers by yourself. You promply die")
            death()

        else:
            print("fight, flee or solo >> ")


def prisoners2():
    time.sleep(1)
    print("You all heroicly fight the soldiers and somehow are victorious")
    time.sleep(1)
    print("You and Rolaf thank eachother and together with the others you escape the castle")
    time.sleep(1)
    win()

def alone():
    time.sleep(1)
    print("Once inside the shed you hear the sounds of screaming and fighting outside. You dicide to look around for any useful items")
    time.sleep(1)
    print("Looking around you notice several bits and tools. looking further into a pile of scrap metal you find a lockpick.\n")
    time.sleep(1)
    print("Also you notice a trapdoor on the shed floor.")
    time.sleep(1)
    print("What do you decide to do first?")

    choice_4 = input

    while choice_4 != "trapdoor":
        choice_4 = input("lockpick or trapdoor >> ")
        if choice_4 == "lockpick":
            time.sleep(1)
            print("\nYou pick up the lockpick and put it in your pocket ")
            time.sleep(1)
            alone2(True)

        elif choice_4 == "trapdoor":
            time.sleep(1)
            print("\nYou walk towards the trapdoor but as soon as you get close the door collapses and you fall in.")
            time.sleep(1)
            sewers(False)


def alone2(has_lockpick):

    choice_4 = input
    print("Do you leave or go towards the trapdoor?")

    while choice_4 != "trapdoor":
        choice_4 = input("leave or trapdoor >> ")

        if choice_4 == "trapdoor" and has_lockpick == False:
            time.sleep(1)
            print("You walk towards the trapdoor but as soon as you get close the door collapses and you fall in.")
            sewers(False)

        elif choice_4 == "trapdoor" and has_lockpick == True:
            time.sleep(1)
            print("You walk towards the trapdoor but as soon as you get close the door collapses and you fall in.")
            sewers(True)
        
        elif choice_4 == "leave":
            time.sleep(1)
            print("You leave the shed")
            time.sleep(1)
            print("You open the doors of the shed and walk outside")
            time.sleep(1)
            print("The dragon notices you and covers you in flames")
            death()


def sewers(has_lockpick):
    time.sleep(1)
    print("You wake up in shock but suprisingly you aren't hurt. you look around and see a iron gate on one side and a pathway on the other")
    time.sleep(1)
    print("Do you try the gate or the pathway?")

    choice_5 = input

    while choice_5 != "gate" or "pathway":
        choice_5 = input()
        if choice_5 == "gate" and has_lockpick == False:
            print("You walk towards the gate")
            gate(False)
        elif choice_5 == "gate" and has_lockpick == True:
            print("You walk towards the gate")
            gate(True)

        elif choice_5 == "pathway":
            print("\nYou walk along the path.")
            time.sleep(1)
            print("But then suddently you hear a noice. A mutated crocodile jumps up from the sewers beneath")
            time.sleep(1)
            print("and swallows you whole.")
            death()

        else:
            print("Do you try the gate or the pathway?")


def gate(has_lockpick):

    print("do you open the gate with the lockpick")

    choice_6 = input

    while choice_6 != "yes" or "no":
            choice_6 = input("yes or no >> ")
            if choice_6 == "yes" and has_lockpick == True:
                print("You open the gate with the lockpick")
                print("The door leads to freedom")
                win()

            elif choice_6 == "yes" and has_lockpick == False:
                print("You dont have a lockpick")
                print("do you open the gate with the lockpick?")

            elif choice_6 == "no" and has_lockpick == True:
                print("You leave the gate alone and walk back to the middle of the room.")
                sewers(True)

            elif choice_6 == "no" and has_lockpick == False:
                print("You leave the gate alone and walk back to the middle of the room.")
                sewers(False)

            else:
                print("do you open the gate with the lockpick?")


intro()

