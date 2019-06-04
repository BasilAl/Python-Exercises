'''Γράψτε ένα πρόγραμμα το οποίο διαβάζει 3άδες χαρακτήρων από 5 διαφορετικά τυχαία
σημεία ενός αρχείου κειμένου και στη συνέχεια φτιάχνει ένα τυχαίο κείμενο το οποίο
αποτελείται από τις συνεχόμενες τριάδες που διαβάστηκαν.'''
import random
import os  # to clear screen and get filenames


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


# Filenames
base = os.getcwd()
filepath = base+"/blablablabla.txt"


def readFile(path):
    '''Returns a string of all the contents of a file at [path].'''
    f = open(path, "r")
    t = f.read()
    f.close()
    return t


def getTriplets(text):
    '''Gets a 5 triplets of characters from a text and makes a list of them.'''
    L = []
    for j in range(5):
        i = random.randint(0, len(text)-3)
        L.append(text[i]+text[i+1]+text[i+2])
    return L


def generateText(triplets):
    '''Given a list of characters, generates a text from them.'''
    S = ""
    print("Here's a text comprising of these triplets of characters: ")
    for t in triplets:
        print(t, end=" ")
    print(":")
    print()
    for i in range(random.randint(25, 500)):
        S += triplets[random.randint(0, len(triplets)-1)]
    print(S)
    print()


def run():
    '''Runs program to generate random texts.'''
    print("This program gets 5 triplets of characters from a hardcoded given text({}) and\
 generates a random text from those given triplets.".format(filepath))
    f = readFile(filepath)
    cont = True
    while cont:
        generateText(getTriplets(f))
        c = input("Do you want to continue?(N for No)\n").lower().startswith("n")
        if c:
            cont = False
    input("Enter to Clear Screen and rerun!")
    clear()


# Run
run()
