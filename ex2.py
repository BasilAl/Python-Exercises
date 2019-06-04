'''Γράψτε ένα πρόγραμμα το οποίο θα παίρνει ως είσοδο έναν ακέραιο και θα επιστρέφει
το άθροισμα των ψηφίων του μέχρι να βρει μονοψήφιος. Παράδειγμα: Για είσοδο 86245
επιστρέφει 8+6+2+4+5=25=>2+5=7.'''


def getInt():
    '''Gets an integer from user input and returns that integer cast as a string'''
    a = input("Give me an integer. \n")
    a = a.replace("-", "")  # if a is negative, strips the sign.
    try:
        b = int(a)
    except ValueError:
        return getInt()
    return a


def evalSum(a):
    '''Prints the sum of digits of a number(cast in str) in a recurrent manner.'''
    A = []
    for d in a:
        A.append(int(d))
    S = 0
    for i in A:
        S += i
    for d in range(len(a)-1):
        print(a[d], end="+")
    print(a[len(a)-1]+"="+str(S))
    if S > 9:
        print("=>", end=" ")
        evalSum(str(S))


def run():
    print("Prints the sum of an integer's digits, recurrently, until it's a single digit number. ")
    while True:
        a = getInt()
        evalSum(a)


# Run
run()
