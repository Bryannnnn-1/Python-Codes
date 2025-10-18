#H:\IN CLASWORK



def FileHandling1():#Writing into a file
    
    file = open("textFile.txt", "w")

    file.write("Hello, Bryan!")

    file.close()

def FileHandling2():#Reading a file
    print("~~~~~~~~~~~~~Reading a file~~~~~~~~~~~~~~")
    
    ThisFile = open("textFile.txt", "r")

    print(ThisFile.read())

    ThisFile.close()

def FileHandling3():#Writing to the file(Overwrite)
    print("~~~~~~~~~~~~Writing to the file~~~~~~~~~~~~~")
    
    with open("textFile.txt", "w") as file:

        file.write("\n Removed(Hello, Bryan!)")

    with open("textFile.txt", "r") as file:

        print(file.read())
    


def FileHandling4():#Appending to the file(adding to the end of the file)
    print("~~~~~~~~~~~~Appending to the file~~~~~~~~~~~~~")
    
    with open("textFile.txt", "a") as file:

        file.write("\n Adding to (Hello, Bryan!)")

    with open("textFile.txt", "r") as file:
        
        print(file.read())


def FileHandling5():#Reading the entire file
    print("~~~~~~~~~~~~Read the entire file~~~~~~~~~~~~~")
    
    with open("textFile.txt", "r") as file:

        content = file.read()

        print(content)


def FileHandling6():#Reading specific number of character
    print("~~~~~~~~~~~~Reading specific number of character~~~~~~~~~~~~~")
    
    with open("textFile.txt", "r") as file:

        print(file.readlines())


def FileHandling7():#Reading line by line
    print("~~~~~~~~~~~~Reading specific number of character~~~~~~~~~~~~~")
    
    with open("textFile.txt", "r") as file:
        
        for line in file:

            print(line.strip())
   


def main():
    #FileHandling1()
    #FileHandling2()
    #FileHandling3()
    #FileHandling4()
    #FileHandling5()
    #FileHandling6()
    FileHandling7()


main()
