'''Γράψτε ένα πρόγραμμα το οποίο δημιουργεί έναν πίνακα οι διαστάσεις του οποίου
δίνονται ως είσοδο από το χρήστη. Ο πίνακας θα «γεμίζει» με τυχαίους ακέραιους
αριθμούς και το πρόγραμμα θα βρίσκει και θα εμφανίζει σε ποιο στοιχείο του πίνακα
βρίσκεται ο μεγαλύτερος αριθμός.'''

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
    maxlen = 0
    for row in matrix:
        for c in row:
            if len(str(c)) > maxlen:
                maxlen = len(str(c))

    for row in matrix:
        for c in row:
            if str(c).startswith("-"):
                print(str(c)+" "*(2+maxlen-len(str(c))), end="")
            else:
                print(" "+str(c)+" "*(1+maxlen-len(str(c))), end="")
        print()


def randFill(matrix, min=-10, max=10):
    '''Fills a matrix with random numbers'''
    M = len(matrix)
    N = len(matrix[0])
    for row in matrix:
        if len(row) != N:
            print("This is not a {}x{} matrix. ".format(M, N))
            return -1
    for i in range(M):
        for j in range(N):
            matrix[i][j] = random.randint(min, max)
    return matrix


def findMax(matrix):
    M = len(matrix)
    N = len(matrix[0])
    for row in matrix:
        if len(row) != N:
            print("This is not a {}x{} matrix. ".format(M, N))
            return -1
    max = matrix[0][0]
    maxList = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] > max:
                max = matrix[i][j]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == max:
                maxList.append((i, j))

    printMatrix(matrix)
    print("The maximum of the above matrix is {} at the following positions(Counting from (1,1)) :".format(max))
    for i in maxList:
        print(i, end="")
    print()


def run():
    print("This will fill a MxN matrix(dimensions specified by user) with random\
    numbers(ranging from -1000 to 1000) and report the maximum and it's position")
    while True:
        T = randFill(makeMatrix())
        printMatrix(T)
        findMax(T)
        input("Enter to Clear screen and rerun.")
        clear()


# Run
run()
