#This is program that will check the possible blood genotype of kids from their parents geno
#The program will cross the genotype of the parents to get the genotype of the kids


import time

normalGene = ["AA", "AS", "SS"]


def gradual(anyword):#to print output slower

    for char in anyword:
        print(char, end='', flush = True)
        time.sleep(0.03)
    
    print()

def mother():#getting genotype of the mother
    bryan = True
    
    while bryan:
        mum = input("Enter the genotype of the MOTHER (eg. AS, AA, SS): ").upper()
        print()

        if not mum:
            gradual("Do not leave the space blank!")
            print()
            bryan = True
        elif mum not in normalGene:
            gradual("This Genotype is invalid!")
            print()
            bryan = True
        else:
            if mum == "AA":
                MotherGene = list(mum)
                bryan = False
            elif mum == "AS":
                MotherGene = list(mum)
                bryan = False
            elif mum == "SS":
                MotherGene = list(mum)
                bryan = False
    return MotherGene

def father():#getting the genotype of the father
    
    bryan = True
    while bryan:
        dad = input("Enter the genotype of the FATHER (eg. AS, AA, SS): ").upper()
        print()

        if not dad:
            gradual("Do not leave the space blank!")
            print()
            bryan = True
        elif dad not in normalGene:
            gradual("This Genotype is invalid!")
            print()
            bryan = True
        else:
            if dad == "AA":
                FatherGene = list(dad)
                bryan = False
            elif dad == "AS":
                FatherGene = list(dad)
                bryan = False
            elif dad == "SS":
                FatherGene = list(dad)
                bryan = False
    return FatherGene
    
def crossing(MotherGene, FatherGene):#crossing the genotypes
    Genotype = []
    

    MainMom = sorted(MotherGene)
    MainDad = sorted(FatherGene)

    kid1 = (MainDad[0],MainMom[0])
    kid2 = (MainDad[0],MainMom[1])
    kid3 = (MainDad[1],MainMom[0])
    kid4 = (MainDad[1],MainMom[1])
    
    kid1 = "".join(sorted(kid1))
    kid2 = "".join(sorted(kid2))
    kid3 = "".join(sorted(kid3))
    kid4 = "".join(sorted(kid4))

    Genotype.append(kid1)
    Genotype.append(kid2)
    Genotype.append(kid3)
    Genotype.append(kid4)

    return kid1, kid2, kid3, kid4, Genotype

    
def result(kid1, kid2, kid3, kid4, Genotype):
    print()
    print()
    time.sleep(1)
    gradual(f"The possible genotype of the first child is: '{kid1}' ")
    print()
    time.sleep(1)
    gradual(f"The possible genotype of the second child is: '{kid2}' ")
    print()
    time.sleep(1)
    gradual(f"The possible genotype of the third child is: '{kid3}' ")
    print()
    time.sleep(1)
    gradual(f"The possible genotype of the fourth child is: '{kid4}' ")
    print()
    time.sleep(1)

    
    if "SS" in Genotype:
        gradual("There's probability that one or more of the kids will be Sickler(s)!")
        time.sleep(1)
        print()
        print()
        print("====================E=N=D=====O=F=====P=R=O=G=R=A=M=====================")
    else:
        gradual("Your kids are safe! Non of them will show any sign of Sickle Cell Anemia!")
        time.sleep(1)
        print()
        print()
        print("====================E=N=D=====O=F=====P=R=O=G=R=A=M=====================")

def main():
    print("======================G=E=N=O=T=Y=P=E=====C=H=E=C=K=E=R========================")
    gradual("This programs checks for the possible genotype of kids from parents genotype!")
    print()
    print()
    FatherGene = father()
    MotherGene = mother()
    kid1, kid2, kid3, kid4, Genotype = crossing(MotherGene, FatherGene)
    result(kid1, kid2, kid3, kid4, Genotype)


main()
