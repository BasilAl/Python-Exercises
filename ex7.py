'''Γράψτε μια συνάρτηση η οποία να ονομάζεται foundlist η οποία να παίρνει σαν είσοδο
μία λίστα μία υπολίστα και να επιστρέφει σχετικό μήνυμα για το αν η δοσμένη υπολίστα
βρίσκεται μέσα στην λίστα.'''

import os  # to clear screen


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def makeList():
    '''Makes a list from user input, where input must be in the form of a python list,
    that is a series of elements, separated by commas, bound by brackets([a,b,c,3,4,5]).'''
    a = input(
        "Give me a list in brackets with elements separated by commas([a,b,c,1,2,3]), please.\n")
    if a.startswith("[") and a.endswith("]"):
        L = a[1:(len(a)-1)].split(sep=",")
        return L
    else:
        print("Wrong input.")
        return makeList()


def foundList(List, SL):
    '''Given 2 lists, checks if the second is a sublist of the first.
    The original method would scan the items in the List and when it found one
    matching the first of the Sublist, would check the following len(SL) items
    to see if they form a sublist, and parse the whole list this way.
    The new version(only the last part of the if-else) checks if SL
    is a sublist on the first time it gets a first element match, and if not
    returns the same function for the rest of the original list. It's not really
    faster, rather more recursively sleek, this way.'''
    if len(List) < len(SL):
        return False
    elif len(List) == len(SL):
        if List != SL:
            return False
        else:
            return True
    else:
        slcount = SL.count(SL[0])
        lcount = List.count(SL[0])
        if slcount < lcount:
            return False
        elif slcount == lcount:
            tempList = List[(List.index(SL[0])):(List.index(SL[0])+len(SL))]
            return foundList(tempList, SL)
        else:
            if (foundList(List[(List.index(SL[0])):(List.index(SL[0])+len(SL))], SL)):
                return True
            else:
                return (foundList(List[(List.index(SL[0])+1):], SL))


'''
Deprecated - Reason: Not as sleek(recursively).
    else:
        sub = False
        for i in range(len(List)-len(SL)):
            if List[i] == SL[0]:
                sub = True
                for j in range(len(SL)):
                    if List[j+i] != SL[j]:
                        sub = False
        return sub
'''


def run():
    '''Gets a list from user input, then a second list and checks if
the  second list is a sublist of the first.'''
    print("This program requests a list to be made from user input,\
then a second list, and checks if the second is a sublist of the first.\n")
    while True:
        print("Let's make the first list: ")
        # L=getList()
        L = makeList()
        print("Ok, now let's make the second list: ")
        # SL=getList()
        SL = makeList()
        if foundList(L, SL):
            print("{} is a sublist of {}! ".format(SL, L))
        else:
            print("{} is NOT a sublist of {}!".format(SL, L))
        input("Enter to Clear Screen and rerun:")
        clear()


run()

#
#
#
# Deprecated code below:
#
#

# GetList is the original method that I used and I kept it for historic reasons.


def getList():
    '''Makes a list from user input. If an integer count is given, it'll stop spamming the user
    for every bit.'''
    L = []
    try:
        count = int(
            input("How many elements would you like the list to have?(0 to get prompted to continue adding.) "))
    except ValueError:
        count = 0
    if count <= 0:
        cont = True
        while cont:
            a = input("Give an element to push to the list. ")
            L.append(a)
            print("The list currently is:\n {}".format(L))
            c = input("Would you like to add more elements?(N for No) ")
            if c.lower().startswith("n"):
                cont = False
        return L
    else:
        for i in range(count):
            a = input("Give an element to push to the list. ")
            L.append(a)
            print("The list currently is:\n {}".format(L))
        return L
