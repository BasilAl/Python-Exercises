'''Γράψτε ένα πρόγραμμα το οποίο δημιουργεί έναν πίνακα με 0 και 1 για διαστάσεις
ορθογωνίου και πλήθος άσσων που παίρνει από το χρήστη.'''

import random
import os  # to clear screen


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


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


def getnnInt(prompt=""):
    '''Returns a non-negative integer given by user(makes sure it's an int)'''
    try:
        a = int(input(prompt))
        if a < 0:
            print("Give me a non-negative integer.  ")
            return getpInt()
    except ValueError:
        print("Give me a non-negative integer.  ")
        return getpInt()
    return a


def makeMatrix():
    '''Makes a MxN matrix with M,N specified by user and fills it with 0s'''
    M = getpInt("Give me the number of rows(M of MxN).  ")
    N = getpInt("Give me the number of columns(N of MxN).  ")

    T = [[0 for i in range(N)] for j in range(M)]
    return T


def printMatrix(matrix):
    '''Prints a matrix'''
    M = len(matrix)
    N = len(matrix[0])
    for row in matrix:
        if len(row) != N:
            print("This is not a {}x{} matrix. ".format(M, N))
            return -1
    for row in matrix:
        for c in row:
            print(str(c)+" ", end="")
        print()


def addRandOnes(matrix, amount):
    '''Adds [amount] of 1s in a given matrix at random positions'''
    M = len(matrix)
    N = len(matrix[0])
    for row in matrix:
        if len(row) != N:
            print("This is not a {}x{} matrix. ".format(M, N))
            return -1
    count = amount
    while count > 0:
        if count > M*N:
            print("Count exceeds Matrix capacity! ")
            print("Setting Count to {}! ".format(M*N))
            count = M*N
        m = random.randint(0, M-1)
        n = random.randint(0, N-1)
        if matrix[m][n] == 0:
            matrix[m][n] = 1
            count -= 1


def run():
    print("This program makes a 2-dimensional matrix filled with 0s with dimensions \
specified by the user, then randomly replaces zeroes with as many 1s as specified \
by the user(minimum 1).")
    while True:
        T = makeMatrix()
        a = getnnInt("How many 1s do you want to add to your matrix?  ")
        addRandOnes(T, a)
        printMatrix(T)
        input("Enter to Clear Screen and rerun.")
        clear()


# Run
run()
