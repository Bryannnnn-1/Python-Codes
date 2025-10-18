

def Area_Of_Circle_If_Radius():#calculate area of a circle if radius is given
    
    while True:

        print(" ")
        print("Enter the RADIUS of the CIRLCE in (cm)")
        print("Enter only the digit, omit the (cm)")
        print(" ")
        userInput = input("RADIUS: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                radius = float(userInput)
                Area = 3.142 * (radius**2)
                power = "\u00b2"
                print(f"The AREA of the CIRCLE with RADIUS '{radius}cm' is: {Area}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        


def Area_Of_Circle_If_Diameter():#calculate area of a circle if the diameter is given

    while True:

        print(" ")
        print("Enter the DIAMETER of the CIRLCE in (cm)")
        print("Enter only the digit, omit the (cm)")
        print(" ")
        userinput = input("DIAMETER: ")
        print(" ")
        

        if not userinput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                diameter = float(userinput)
                Area = 3.142 * ((diameter / 2)**2)
                power = "\u00b2"
                print(f"The AREA of the CIRCLE with DIAMETER '{diameter}cm' is: {Area}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def AreaTriangle():# calculate area of a traingle

    while True:
        print("Enter the HEIGHT of the TRIANGLE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("HEIGHT: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                height = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")

    while True:
        print(" ")
        print("Enter the BASE of the TRIANGLE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("BASE: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                base = float(userInput)
                power = "\u00b2"
                area = 0.5 * height * base
                print(f"The AREA of the TRIANGLE with BASE '{base}cm' and HEIGHT '{height}cm' is: {area}cm{power} ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def AreaRectangle():# calculate area of a Rectangle

    while True:
        print("Enter the LENGTH of the RECTANGLE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("LENGTH: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                length = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")

    while True:
        print(" ")
        print("Enter the WIDTH of the RECTANGLE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("WIDTH: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                width = float(userInput)
                power = "\u00b2"
                area = length * width
                print(f"The AREA of the RECTANGLE with LENGTH '{length}cm' and WIDTH '{width}cm' is: {area}cm{power} ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def AreaSquare():#calculate area of a square

    
    while True:
        print(" ")
        print("Enter the LENGTH of one side of the SQUARE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("LENGTH: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                length = float(userInput)
                power = "\u00b2"
                area = length ** 2
                print(f"The AREA of the square with LENGTH of one-side '{length}cm' is: {area}cm{power} ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def AreaTrapezium():#calculate area of a trapezium

    while True:#get top trapezium
        print("Enter the TOP PARALLEL SIDE of the Trapezium in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("TOP PARALLEL SIDE: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                topSide = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")


    while True:#get bottom trapezium
        print("Enter the BOTTOM PARALLEL SIDE of the TRAPEZIUM in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("BOTTOM PARALLEL SIDE: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                bottomSide = float(userInput)
                if topSide >= bottomSide:
                    print("The top parallel line cannot be longer than the bottom!")
                    print("Please try again!")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(" ")
                    continue
                else:
                    break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



    while True:
        print("Enter the HEIGHT of the TRAPEZIUM in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("HEIGHT: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                height = float(userInput)
                area = ((topSide + bottomSide) * 2) * height
                power = "\u00b2"
                print(f"The TRAPEZIUM has the following parameters:\nTop parallel side '{topSide}cm',\nBottom parallel side '{bottomSide}cm', Height of '{height}cm' ")
                print(" ")
                print(f"The AREA of the TRAPEZIUM is: {area}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def AreaParallelogram():#calculate area of a parallelogram


    while True:
        print("Enter the HEIGHT of the PARALLELOGRAM in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("HEIGHT: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                height = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")

    while True:
        print(" ")
        print("Enter the BREADTH of the PARALLELOGRAM in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("BREADTH: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                breadth = float(userInput)
                power = "\u00b2"
                area = height * breadth
                print(f"The AREA of the PARALLELOGRAM with BREADTH '{breadth}cm' and HEIGHT '{height}cm' is: {area}cm{power} ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def volumeCube():#calculate volume of cube


    while True:
        print(" ")
        print("Enter the LENGTH of one side of the CUBE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("LENGTH: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                length = float(userInput)
                power = "\u00b3"
                volume = length ** 3
                print(f"The VOLUME of the CUBE with LENGTH of one-side '{length}cm' is: {volume}cm{power} ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def volumeCuboid():#calculate volume of cuboid


    while True:
        print("Enter the LENGTH of the CUBOID in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("LENGTH: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
        else:

            try:
                length = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")


    while True:
        print("Enter the WIDTH of the CUBOID in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("WIDTH: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                width = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



    while True:
        print("Enter the HEIGHT of the CUBOID in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("HEIGHT: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                height = float(userInput)
                volume = length * width * height
                power = "\u00b3"
                print(f"The CUBOID has the following parameters:\nLENGTH '{length}cm',\nWIDTH '{width}cm', HEIGTH of '{height}cm' ")
                print(" ")
                print(f"The VOLUME of the CUBOID is: {volume}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def volume_Cone_Radius():#calculate volume of cone


    while True:
        print("Enter the RADIUS of the CONE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("RADIUS: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                radius = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")


    while True:
        print("Enter the HEIGHT of the CONE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("HEIGHT: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                height = float(userInput)
                volume = (3.142/3) * (radius ** 2 ) * height
                power = "\u00b3"
                print(f"The CONE has the following parameters:\nRADIUS '{radius}cm',\nHEIGTH of '{height}cm' ")
                print(" ")
                print(f"The VOLUME of the CONE is: {volume}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def volume_Cone_Diameter():#calculate volume of cone


    while True:
        print("Enter the DIAMETER of the CONE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("RADIUS: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                diameter = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")


    while True:
        print("Enter the HEIGHT of the CONE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("HEIGHT: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                height = float(userInput)
                volume = (3.142/3) * ((diameter / 2) ** 2 ) * height
                power = "\u00b3"
                print(f"The CONE has the following parameters:\nDIAMETER '{diameter}cm',\nHEIGTH of '{height}cm' ")
                print(" ")
                print(f"The VOLUME of the CONE is: {volume}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")


    
def Volume_Of_Sphere_If_Radius():#calculate volume of a sphere if radius is given
    while True:

        print(" ")
        print("Enter the RADIUS of the SPHERE in (cm)")
        print("Enter only the digit, omit the (cm)")
        print(" ")
        userInput = input("RADIUS: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                radius = float(userInput)
                volume = ((4 * 3.142) / 3) * (radius**3)
                power = "\u00b3"
                print(f"The VOLUME of the SPHERE with RADIUS '{radius}cm' is: {volume}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        


def Volume_Of_Sphere_If_Diameter():#calculate volume of sphere if diameter is given
    while True:

        print(" ")
        print("Enter the DIAMETER of the SPHERE in (cm)")
        print("Enter only the digit, omit the (cm)")
        print(" ")
        userInput = input("DIAMETER: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                diameter = float(userInput)
                volume = ((4 * 3.142) / 3) * ((diameter / 2)**3)
                power = "\u00b3"
                print(f"The VOLUME of the SPHERE with DIAMETER '{diameter}cm' is: {volume}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        


def volumeHollowCylinder():#calculate volume of a hollow cylinder


    while True:
        print("Enter the BIG DIAMETER of the CONE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("RADIUS: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                radius = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")


    while True:
        print("Enter the RADIUS of the CONE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("RADIUS: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                radius = float(userInput)
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



    while True:
        print("Enter the HEIGHT of the CONE in (cm)")
        print("Enter only the digit, omit the (cm)")
        userInput = input("HEIGHT: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:

            try:
                height = float(userInput)
                volume = (3.142/3) * (radius ** 2 ) * height
                power = "\u00b2"
                print(f"The CONE has the following parameters:\nRADIUS '{radius}cm',\nHEIGTH of '{height}cm' ")
                print(" ")
                print(f"The VOLUME of the CONE is: {volume}cm{power}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                break
            except ValueError:
                print("Enter a valid number please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def volumePyramid():
    pass
def volumeCylinder():
    pass
def volumeHemiSphere():
    pass
def volumeParrallelpiped():
    pass



def area():#function to call if the user wants to calculate area
    
    while True:
    
        print(" ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ")
        print("THESE ARE THE AVAILABLE SHAPES FOR AREA CALCULATION.")
        print(" ")
        print("[1]  CIRCLE")
        print(" ")
        print("[2]  TRIANGLE")
        print(" ")
        print("[3]  RECTANGLE")
        print(" ")
        print("[4]  SQUARE")
        print(" ")
        print("[5]  TRAPEZIUM")
        print(" ")
        print("[6]  PARALLELOGRAM")
        print(" ")
        print(" ")
        print("WHAT SHAPE DO YOU WANT TO CALCULATE FOR? ")
        print(" ")

        userInput = input("Choose from 1 to 6: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:
            try:
                shape = int(userInput)
                if shape == 1:
                    print(" ")
                    print("Are you gonna use DIAMETER or RADIUS")
                    print(" ")
                    print("Type RADIUS or DIAMETER")
                    UserInput = input(" ").upper()

                    if not UserInput:
                        print("Don't leave any space blank!")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(" ")
                        continue
                    elif not UserInput.isalpha():
                        print("Error, please try again!")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(" ")
                        continue
                    else:
                        if UserInput == "RADIUS":
                            Area_Of_Circle_If_Radius()
                        elif UserInput == "DIAMETER":
                            Area_Of_Circle_If_Diameter()
                        else:
                            print("Wrong input...!")
                            print("Try again!")
                            print(" ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            area()
                elif shape == 2:
                    AreaTriangle()
                elif shape == 3:
                    AreaRectangle()
                elif shape == 4:
                    AreaSquare()
                elif shape == 5:
                    AreaTrapezium()
                elif shape == 6:
                    AreaParallelogram()
                else:
                    print("THE SHAPE YOU CHOSE IS NOT AVAILABLE!")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(" ")
                    continue
                break
            except ValueError:
                print("Enter a valid option please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def volume():#function to call if the user wants to calculate volume

    while True:

        print(" ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ")
        print("THESE ARE THE AVAILABLE SHAPES FOR VOLUME CALCULATION.")
        print(" ")
        print("[1]  CUBE")
        print(" ")
        print("[2]  CUBOID")
        print(" ")
        print("[3]  CONE")
        print(" ")
        print("[4]  HOLLOW CYLINDER")
        print(" ")
        print("[5]  SPHERE")
        print(" ")
        print("[6]  PYRAMID")
        print(" ")
        print("[7]  CYLINDER")
        print(" ")
        print("[8]  HEMISPHERE")
        print(" ")
        print("[9]  PARALLELPIPED")
        print(" ")
        print(" ")
        print(" ")
        print("WHAT 3D SHAPE DO YOU WANT TO CALCULATE FOR? ")
        print(" ")

        userInput = input("Choose from 1 to 9: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:
            try:
                Shape = int(userInput)
                if Shape == 1:
                    volumeCube()
                elif Shape == 2:
                    volumeCuboid()
                elif Shape == 3:
                    print(" ")
                    print("Are you gonna use DIAMETER or RADIUS to calculate for the CONE?")
                    print(" ")
                    print("Type RADIUS or DIAMETER")
                    UserInput = input(" ").upper()

                    if not UserInput:
                        print("Don't leave any space blank!")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(" ")
                        continue
                    elif not UserInput.isalpha():
                        print("Error, please try again!")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(" ")
                        continue
                    else:
                        if UserInput == "RADIUS":
                            volume_Cone_Radius()
                        elif UserInput == "DIAMETER":
                            volume_Cone_Diameter()
                        else:
                            print("Wrong input...!")
                            print("Try again!")
                            print(" ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            volume()
                elif Shape == 4:
                    volumeHollowCylinder()
                elif Shape == 5:
                    print(" ")
                    print("Are you gonna use DIAMETER or RADIUS to calculate for the SPHERE?")
                    print(" ")
                    print("Type RADIUS or DIAMETER")
                    UserInput = input(" ").upper()

                    if not UserInput:
                        print("Don't leave any space blank!")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(" ")
                        continue
                    elif not UserInput.isalpha():
                        print("Error, please try again!")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(" ")
                        continue
                    else:
                        if UserInput == "RADIUS":
                            Volume_Of_Sphere_If_Radius()
                        elif UserInput == "DIAMETER":
                            Volume_Of_Sphere_If_Diameter()
                        else:
                            print("Wrong input...!")
                            print("Try again!")
                            print(" ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            volume()
                elif Shape == 6:
                    volumePyramid()
                elif Shape == 7:
                    volumeCylinder()
                elif Shape == 8:
                    volumeHemiSphere()
                elif Shape == 9:
                    volumeParrallelpiped()
                else:
                    print("THE SHAPE YOU CHOSE IS NOT AVAILABLE!")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(" ")
                    menu()
                break
            except ValueError:
                print("Enter a valid option please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")



def menu():#function for the user to select if he/she wants to solve area or volume

    while True:
        print(" ")
        print("~~~~~~~~~~~~~~~~~~W~E~L~C~O~M~E~~~~T~O~~~~M~Y~~~~C~A~L~C~U~L~A~T~O~R~~~~~~~~~~~~~~~~~~~~~")
        print(" ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~D~E~S~I~G~N~E~D~~~~B~Y~~~~B~R~Y~A~N~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ")
        print("WHAT DO YOU WANT TO CALCULATE FOR? ")
        print(" ")
        print("[1]  AREA")
        print(" ")
        print("[2]  VOLUME")
        print(" ")

        userInput = input("Choose 1 or 2: ")
        print(" ")
        

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        else:
            try:
                choice = int(userInput)
                if choice == 1:#if choice is (1) which is area~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    area()
                    ending()
                elif choice == 2:#if choice is (1) which is volume~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    volume()
                    ending()
                else:
                    print(" ")
                    print("THIS IS NOT AN OPTION!")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(" ")
                    menu()
                break
            except ValueError:
                print("Enter a valid option please!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")

















































































































































































































































































def ending():#function to check if the user wants to continue the code or not

    while True:
        print(" ")
        print(" ")
        print("DO YOU WANT TO SOLVE ANOTHER PROBLEM?")
        print(" ")
        print("YES or NO")
        print(" ")

        userInput = input("Type Yes or No: ").upper()
        print(" ")

        if not userInput:
            print("Don't leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            continue
        elif not userInput.isalpha():
            print("Error!, please enter yes or no!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
        else:
            if userInput == "YES":
                print(" ")
                print("Program continue...")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                menu()
            elif userInput == "NO":
                print(" ")
                print("Program ending...")
                print(" ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                exit()
            else:
                (" ")
                print("Invalid input!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                ending()

menu()#calling the menu() function to run the code



    
    
    
