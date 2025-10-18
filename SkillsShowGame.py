import time
import random
import threading


riddles = [
    "What has keys but can't open locks?",
    "I’m tall when I’m young, and I’m short when I’m old. What am I?",
    "What can travel around the world while staying in the corner?",
    "What has a face and two hands but no arms or legs?",
    "What comes once in a minute, twice in a moment, but never in a thousand years?",
    "What is full of holes but still holds a lot of weight?",
    "What has a neck but no head?",
    "What is always in front of you but can’t be seen?",
    "What can you catch but not throw?",
    "What is as light as a feather, yet the strongest man can't hold it for much longer?"
]


health = 3

print("\t>>>==========>\n\n")
time.sleep(0.05)
print("\t\t>>>==========>\n\n")
time.sleep(0.05)
print("\t\t\t>>>==========>\n\n")
time.sleep(0.05)
print("\t\t\t\t>>>==========>\n\n")
time.sleep(0.05)
print("\t\t\t\t\t>>>==========>\n\n")
time.sleep(0.05)
print("\t\t\t\t>>>==========>\n\n")
time.sleep(0.05)
print("\t\t\t>>>==========>\n\n")
time.sleep(0.05)
print("\t\t>>>==========>\n\n")
time.sleep(0.05)
print("\t>>>==========>\n\n")




def slow(anyword):

    for char in anyword:
        print(char, end='', flush = True)
        time.sleep(0.03)
    
    print()


def start():
    global health
    slow("You are an investigator sent to uncover the mysteries of an old, abandoned mansion.") 
    slow("Over the years, people have vanished inside its walls, and rumors of dark forces have surrounded it. ") 
    slow("Your mission is to uncover the secrets of the chamber and escape before you become another lost soul.")
    print(" ")
    slow("You have to get through the living room, dance hall, kitchen, library, and then to the basement where")
    slow("the documentaries about the house is kept. You have a full health of 100HP and for any damage")
    slow("you take, 20HP will be deducted from your HP. Also be ready to crack your brain for clues and puzzles.")
    slow("Once your HP is 0, you are dead!")
    print(" ")
    print(" ")
    print("  # # # #   #       #   # # #              # # #     # # # #    #     #   # # # #   # # #     # # # #       ##     ")
    print("  #     #   # #     #   #     #             #     #   #         #     #   #     #   #     #   #             ##     ")
    print("  # # # #   #   #   #   #      #            # # #     # # # #   #  #  #   # # # #   # # #     # # # #       ##     ")
    print("  #     #   #     # #   #     #             #     #   #         # # # #   #     #   #    #    #                    ")
    print("  #     #   #       #   # # #              # # #     # # # #    #     #   #     #   #     #   # # # #       ##     ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("   #     #        # # # #   # # #     # # # #                                                                             ##     ")
    print("   #     #        #     #   #     #   #                                                                                   ##     ")
    print("   #     #        # # # #   # # #     # # # #                                                                                  ##     ")
    print("   #     #        #     #   #    #    #                                                                                              ")
    print("     # #          #     #   #     #   # # # #                                                                                  ##     ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")


    bryan = True
    while bryan:
        slow("Do you still want to enter the Forgotten Chamber?? ")
        print(" ")
        slow("\tYES or NO")
        print(" ")
        enter = str(input(">>>>> ")).lower()

        if not enter:
            print("Don't leave the space blank!")
            print(" ")
            print(" ")
            bryan = True
        elif enter == "yes":
            print(" ")
            slow("You are so brave!")
            print(" ")
            while True:
                slow("What is your name?")
                print(" ")
                name = str(input(">>>>> "))

                if not name:
                    print("Don't leave any space blank!")
                    print(" ")
                    print(" ")
                    continue
                elif not name.isalpha():
                    print("Your name cannot contain numbers or characters!")
                    print(" ")
                    print(" ")
                    continue
                else:
                    print(" ")
                    slow(f"Goodluck with the quest, {name}")
                    livingRoom()
                    danceHall()
                break
        elif enter == "no":
            print(" ")
            slow("Oopss....looks like someone is too scared!")
            slow("Hahahaha!")
            print(" ")
            slow("Program ending...")
            exit()
        else:
            print("Invalid Input!")
            print(" ")
            bryan = True


def countdownLivingRoom():
    global health

    start = 5
    while start > 0:
        print(f"\r{start}", end=' ', flush= True)
        time.sleep(1)

        start -= 1

        print("\r" + " " * 10, end='', flush=True)


    
def livingRoom():
    time.sleep(2)
    print(" ")
    slow("You enter the Living Room. The room is dimly lit and dusty. A large chandelier hangs from the ceiling.")
    slow("You notice a strange painting on the wall, and as you approach, a cold breeze sweeps through the room.")
    slow("Suddenly, you hear footsteps coming from the hallway...")
    print(" ")
    time.sleep(2)
    slow("Oopss!...looks like you stepped on something...it's a note and it has something written on it")
    print(" ")
    slow("The message written on the note will appear and disappear in...")
    time.sleep(1)

    countdownLivingRoom()
    print(" ")

    print("1 2 5 5 4 6 6 1", end='', flush=True)

    time.sleep(3)

    print("\r" + " " * 30, end='', flush=True)

    danceHall()

def danceHall():
    global health
    time.sleep(1)
    print(" ")
    slow("You have successfully made it past the living room...")
    time.sleep(1)
    slow("You then climb the stairs and opens the door that leads to the Dance Hall.")
    slow("You step into the Dance Hall. The room is filled with cobwebs and forgotten items.")
    slow("A large, broken piano sits in the center, and OZEBA plays softly from it, even though no one is near.")
    slow("You started shaking and walking slowly and suddenly you...")
    slow("You stepped on a human skull and as you looked down, something tapped your shoulder.....")
    print(" ")
    time.sleep(1)
    slow("You freaked out and started running helter-skelter......and you came across a door that has a password lock.")
    slow("Ohhhh.....hope you remember the digits written on the note back in the living room?")
    slow("And once you touch the door, you have to input the 4 digit pin")
    slow("You have only 3 attempts....")
    slow("If you use up your attempts, you will return back to the Living room with -1 life")
    print(" ")
    print(" ")
    print(" ")

    bryan = True

    while bryan:
        slow("what will you do right now?")
        print(" ")
        slow("[1] Touch the door!")
        print(" ")
        slow("[2] Go back to the living room!")
        print(" ")
        slow("CHOOSE 1 OR 2")
        print(" ")

        test = input(">>>>> ")

        if not test:
            print("Don't leave any space blank!")
            print(" ")
            print(" ")
            bryan = True
        elif test == "1":
            print(" ")
            slow("You touched the door.....and now you have to enter the 4 digit code")
            slow(".....And be careful here because any error you make counts as an attempt")
            attempt = 3

            haaland = True
            while haaland:
                print(" ")
                slow("Enter the 4 digit code")
                print(" ")
                passcode = input(">>>>> ")

                if not passcode:
                    print(" ")
                    print(" ")
                    print("-1 attempt")
                    attempt -= 1
                    if attempt <= 0:
                        print(" ")
                        slow("Unfortunatly.....you couldn't make it :( .........you will have to go back to the living room")
                        time.sleep(0.5)
                        slow("\t\t\tSpawning...")
                        time.sleep(0.5)
                        slow("\t\tSpawning...")
                        time.sleep(0.5)
                        slow("\tSpawning...")
                        livingRoom()
                elif passcode == "4661":
                    print(" ")
                    slow("Wow.....you have successfully cracked the code!...")
                    slow("You are a genius!")
                    print(" ")
                    haaland = False
                    library()
                else:
                    print(" ")
                    slow("Invalid!")
                    print(" ")
                    print("-1 attempt")
                    attempt -= 1
                    if attempt <= 0:
                        print(" ")
                        slow("Unfortunatly.....you couldn't make it :( .........you will have to go back to the living room")
                        time.sleep(0.5)
                        slow("\t\t\tSpawning...")
                        time.sleep(0.5)
                        slow("\t\tSpawning...")
                        time.sleep(0.5)
                        slow("\tSpawning...")
                        livingRoom()
        elif test == "2":
            print(" ")
            slow("You will return to the living room with -1 life")
            print(" ")
            time.sleep(0.5)
            slow("\t\t\tSpawning...")
            time.sleep(0.5)
            slow("\t\tSpawning...")
            time.sleep(0.5)
            slow("\tSpawning...")
            slow("You have spawned back to the sitting room!")
            livingRoom()
        else:
            print("Invalid option!")
            print(" ")
            print(" ")
            bryan = True


def library():
    global health
    slow("You made it through the Dance hall.....you are indeed, an Investigator :)")
    time.sleep(1)
    slow("You enter the library. The room is lined with shelves of dusty, old books.")
    slow("In the center of the room, there's a large table with an open book. The book is blank initially, ")
    slow("but as you approached the book, a note displays on it saying.....")
    time.sleep(0.5)
    slow("\t\t\t.....")
    time.sleep(0.5)
    slow("\t\t.....")
    time.sleep(0.5)
    slow("\t.....")

    time.sleep(1)
    slow("TO OPEN THE DOOR TO THE BASEMENT, YOU HAVE TO SOLVE A RIDDLE! ")
    time.sleep(1)
    print(" ")
    slow("THERE IS AN INVISIBLE TIMER THAT COUNTSDOWN...YOU HAVE ONLY 40 SECONDS TO SOLVE THE RIDDLE!")
    print(" ")
    slow(" ")
    print(" ")
    print(" ")


    bryan = True

    while bryan:
        slow("what will you do right now?")
        print(" ")
        slow("[1] Accept your fate and solve the riddle!")
        print(" ")
        slow("[2] Give up and go back to the dance hall!")
        print(" ")
        slow("[3] Quit game!")
        slow("CHOOSE 1 / 2 / 3")
        print(" ")

        test = input(">>>>> ")

        if not test:
            print("Don't leave any space blank!")
            print(" ")
            print(" ")
            bryan = True
            break
        elif test == "1":
            riddle = random.choice(riddles)
            print(" ")
            slow("You have accepted your fate.....")
            print(" ")
            slow("The riddle is.....")
            print(" ")
            time.sleep(1)
            slow(riddle)
            print(" ")
            

            if riddle == (riddles[0]):
                slow("[A]  Computer")
                slow("[B]  Piano")#################
                slow("[C]  Treasure Chest")
                slow("[D]  Keychain")
                slow("[E]  Map")
            elif riddle == (riddles[1]):
                slow("[A]  Tree")
                slow("[B]  Building")
                slow("[C]  Mountain")
                slow("[D]  Tower")
                slow("[E]  Candle")##################
            elif riddle == (riddles[2]):
                slow("[A]  Stamp")###############
                slow("[B]  Letter")
                slow("[C]  Globe")
                slow("[D]  Bird")
                slow("[E]  Flag")
            elif riddle == (riddles[3]):
                slow("[A]  Clock")##################
                slow("[B]  Mannequin")
                slow("[C]  Painting")
                slow("[D]  Mirror")
                slow("[E]  Statue")
            elif riddle == (riddles[4]):
                slow("[A]  The Letter 'E'")
                slow("[B]  The sun")
                slow("[C]  The Letter 'M'")#######################
                slow("[D]  A leap year")
                slow("[E]  A second")
            elif riddle == (riddles[5]):
                slow("[A]  A sponge")
                slow("[B]  A net")##############################
                slow("[C]  A rope")
                slow("[D]  A sieve")
                slow("[E]  A troller")
            elif riddle == (riddles[6]):
                slow("[A]  A shirt")
                slow("[B]  A guitar")
                slow("[C]  A bottle")##################################
                slow("[D]  A vase")
                slow("[E]  A violin")
            elif riddle == (riddles[7]):
                slow("[A]  Your reflection")
                slow("[B]  The wind")
                slow("[C]  The past")
                slow("[D]  The future")##################################
                slow("[E]  The horizon")
            elif riddle == (riddles[8]):
                slow("[A]  A ball")
                slow("[B]  A butterfly")
                slow("[C]  A frisbee")
                slow("[D]  A fish")
                slow("[E]  A cold")#####################
            elif riddle == (riddles[9]):
                slow("[A]  Water")
                slow("[B]  Smoke")
                slow("[C]  Feather")
                slow("[D]  Breath")########################
                slow("[E]  Bubble")
           


                mbappe = True
                while mbappe:
                    print(" ")
                    print(" ")
                    answer = input("Choose from the options A / B / C / D / E: ").upper

                    if not answer:
                        print("No blank spaces!")
                        print(" ")
                        print(" ")
                        continue
                    else:
                        if riddle == (riddles[0]) and answer == "b":
                            print(" ")
                            slow(">>>>>>>>>>>>>CORRECT>>>>>>>>>>>>")
                            slow("You are a genius!......")
                            time.sleep(1)
                            slow("The door to the basement opens......")
                            basement()
                            break
                        else:
                            print(" ")
                            slow("<<<<<<<<<<<<<WRONG<<<<<<<<<<<<<")
                            print(" ")
                            slow("-1 attempt")
                            attempt -= 1
                            print(" ")
                            slow(f"You have {attempt} more attempt(s) remaining ")

                            if attempt <= 0:
                                print(" ")
                                slow("Unfortunatly.....you couldn't make it :( .........you will have to go back to the dance hall")
                                slow("And 1 life will be deducted from your HP...")
                                health -= 1
                                print(" ")
                                slow(f"You have {health} life(s) remaining!")
                                print(" ")

                                if health <= 0:
                                    slow("Unfortunately...You were killed :(")
                                    print(" ")
                                    slow("Farewell brave man...")
                                    print(" ")
                                    slow("Game ending...")
                                    print(" ")
                                    exit()
                                else:
                                    time.sleep(0.5)
                                    slow("\t\t\tSpawning...")
                                    time.sleep(0.5)
                                    slow("\t\tSpawning...")
                                    time.sleep(0.5)
                                    slow("\tSpawning back to dance hall...")
                                    danceHall()
                            else:
                                slow(f"You have {attempt} more attempt(s) remaining ")
                                print(" ")
                                mbappe = True
############################################################################################################################################
                        if riddle == (riddles[1]) and answer == "e":
                            print(" ")
                            slow(">>>>>>>>>>>>>CORRECT>>>>>>>>>>>>")
                            slow("You are a genius!......")
                            time.sleep(1)
                            slow("The door to the basement opens......")
                            basement()
                            break
                        else:
                            print(" ")
                            slow("<<<<<<<<<<<<<WRONG<<<<<<<<<<<<<")
                            print(" ")
                            slow("-1 attempt")
                            attempt -= 1
                            print(" ")
                            slow(f"You have {attempt} more attempt(s) remaining ")

                            if attempt <= 0:
                                print(" ")
                                slow("Unfortunatly.....you couldn't make it :( .........you will have to go back to the dance hall")
                                slow("And 1 life will be deducted from your HP...")
                                health -= 1
                                print(" ")
                                slow(f"You have {health} life(s) remaining!")
                                print(" ")

                                if health <= 0:
                                    slow("Unfortunately...You were killed :(")
                                    print(" ")
                                    slow("Farewell brave man...")
                                    print(" ")
                                    slow("Game ending...")
                                    print(" ")
                                    exit()
                                else:
                                    time.sleep(0.5)
                                    slow("\t\t\tSpawning...")
                                    time.sleep(0.5)
                                    slow("\t\tSpawning...")
                                    time.sleep(0.5)
                                    slow("\tSpawning back to dance hall...")
                                    danceHall()
                            else:
                                slow(f"You have {attempt} more attempt(s) remaining ")
                                print(" ")
                                mbappe = True
                                

                                        



            
                    
        elif test == "2":
            slow("Going back to the dance hall...")
            print(" ")
            time.sleep(0.5)
            slow("\t\t\tSpawning...")
            time.sleep(0.5)
            slow("\t\tSpawning...")
            time.sleep(0.5)
            slow("\tSpawning back to dance hall...")
            danceHall()



        elif test == "3":
            slow("Soldiers don't give up in war front!...")
            print(" ")
            slow("Game Over!!!")
            print(" ")
            exit()           






    
def basement():
    pass



#start()

library()
