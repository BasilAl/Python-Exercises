'''Γράψτε τον κώδικα μιας συνάρτησης που θα ονομάζεται maxminIntervals η οποία
παίρνει σαν είσοδο μια λίστα από διαστήματα και επιστρέφει το διάστημα (ή τα
διαστήματα) με το μεγαλύτερο και το διάστημα με το μικρότερο μήκος.
Παραδείγματα:
maxminIntervals ( [[1,2], [6, 10], [10, 15] ] ) Επιστρέφει max=[10, 15] min=[1,2]
maxminIntervals ( [[1,4], [5, 10], [3, 5] ] ) Επιστρέφει max=[5, 10] min=[3,5]
maxminIntervals ( [[1,5], [10, 20], [1, 6], [16, 20], [5, 11]] ) Επιστρέφει max=[10,
20] min=([1,5], [16, 20]).'''


import random


def getIntervals():
    '''Ask user to generate a list of integer intervals'''
    def getInterval():
        '''Returns an integer interval as set by user'''
        def getUpper(l):
            try:
                b = int(input("Give the interval's upper bound: \n"))
            except ValueError:
                print("Type in an integer, please.  ")
                return getUpper(l)
            if b < l:
                print("The upper bound can't be lower than the lower bound. ")
                return getUpper(l)
            else:
                return b
        try:
            a = int(input("Give the interval's lower bound: \n"))
        except ValueError:
            print("Type in an integer, please. ")
            return getInterval()
        b = getUpper(a)
        return [a, b]
    getMore = True
    A = []
    while getMore:
        A.append(getInterval())
        f = input("Would you like to add more intervals?(N for no)\n")
        if f.lower().startswith("n"):
            getMore = False
    return A


def randomIntervals(lower=0, ran=100, amount=10):
    '''Generate [amount] integer intervals with min value [lower] and
    a diameter of up to [ran] above the minimum value(max width: ran,
    intervals ranging from [1,2] to [99,199] for example)'''
    A = []
    for i in range(amount):
        a = random.randint(lower, ran)
        b = random.randint(a+1, a+ran)
        c = [a, b]
        A.append(c)
    return A


def maxminIntervals(intlist):
    '''Prints the intervals with min and max diameters'''
    max = 0
    min = intlist[0][1]-intlist[0][0]
    for i in intlist:
        t = i[1]-i[0]
        if t > max:
            max = t
        if t < min:
            min = t
    maxInts = []
    minInts = []
    for i in intlist:
        t = i[1]-i[0]
        if t == min:
            minInts.append(i)
        if t == max:
            maxInts.append(i)
    print("The max diameter is {}, for these intervals:".format(max))
    for i in maxInts:
        print(i)
    print("\nThe min diameter is {}, for these intervals:".format(min))
    for i in minInts:
        print(i, end=" ")
        print()


def getInt(prompt=""):
    '''Returns an integer given by user(makes sure it's an int)'''
    try:
        a = int(input(prompt))
    except ValueError:
        print("Give me an integer.  ")
        return getpInt()
    return a


def getpInt(prompt=""):
    '''Returns a positive integer given by user(makes sure it's an int)'''
    try:
        a = int(input(prompt))
        if a <= 0:
            print("Give me a positive integer.  ")
            return getpInt()
    except ValueError:
        print("Give me a positive integer.  ")
        return getpInt()
    return a


def run(mode="random"):
    '''Generates random integer intervals if mode="random" or asks the user\
    to generate his own intervals if mode="user", then from this set of intervals\
    prints the ones with the maximum and minimum diameter'''
    if mode == "random":
        l = getInt("Give me the lowest value.  ")
        ran = getInt("Give me a maximum diameter.  ")
        amount = getpInt("How many intervals would you like me to generate?  ")
        A = randomIntervals(l, ran, amount)
        maxminIntervals(A)
    elif mode == "user":
        A = getIntervals()
        maxminIntervals(A)
    else:
        m = input('Invalid Mode - Give "user" or "random".  ')
        run(mode=m)


# Run
print("This program generates(or asks the user for) a list of intervals(of the type [a,b] with a<b)\
 and prints the intervals with the maximum and minimum length.\n\
In the case of random, it asks for a lowest value and a max diameter because it\
  felt to me that this way the intervals produced would be nicer. The diameter is \
  max_value - min_value, for those not familiar.\n")
while True:
    i = input("Would you like to create your own intervals(U) or have them \
generated randomly(R)?").lower()
    while not (i.startswith("u") or i.startswith("r")):
        i = input("Please select (U)ser or (R)andom mode.").lower()
    if i.startswith("u"):
        run(mode="user")
    else:
        run(mode="random")
