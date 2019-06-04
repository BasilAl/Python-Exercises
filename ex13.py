'''Γράψτε ένα πρόγραμμα που θα δέχεται από τον χρήστη έναν αριθμό n. Ο αριθμός θα
πρέπει να είναι θετικός, διαφορετικά το πρόγραμμα θα εμφανίζει αντίστοιχο μήνυμα και
θα ζητάει ξανά αριθμό μέχρι να δοθεί θετικός αριθμός. Στη συνέχεια υπολογίζει την
ακολουθία x_n: 2n+1 αν ο n είναι μονός, x_n/2 αν ο n είναι μονός και εμφανίζει το
πλήθος των όρων μέχρι η ακολουθία να φτάσει το 1.'''


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


def calc(n):
    '''Xn=3n+1, if x odd // Xn=n/2, if x even.'''
    count = 0
    terms = [n]
    trmf = True
    if n <= 1:
        return (0, str(n))
    else:
        while n > 1:
            if n % 2 == 0:
                n = int(n/2)
                # print(n)
                count += 1
            else:
                n = int(3*n+1)
                # print(n)
                count += 1
            if trmf == True:
                terms.append(n)
            if len(terms) > 100:
                trmf = False
                terms = "Terms too many to print out"
        return (count, terms)


def run():
    print("This program calculates the terms of the sequence: \
\nX(n) =3n+1, if n is odd\n    |\n     =n/2, if n is even \nand prints the \
number of iterations it took to terminate at 1.(And the terms that led to that, if they are less than 101.) \n")
    while True:
        a = getpInt("Give me a positive integer.\n")
        print("Amount of terms till Collatz terminates for {}: {}\n".format(a, calc(a)[0]))
        print("And the terms that lead to this are:")
        for i in calc(a)[1]:
            print(str(i), end=" ")
        print()


# run
run()
