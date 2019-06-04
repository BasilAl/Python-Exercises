# To Fix: When inputting on the same occupied position, keeps printing without
# clearing the screen and lines add up. Need to rework buffprint/boardprint
# functions.

'''Γράψτε ένα πρόγραμμα το οποίο παίζει το παιχνίδι SOS με τον χρήστη σε τετράγωνο
10*10. Ο υπολογιστής δεν χρειάζεται να παίζει έξυπνα (επιλέγει τυχαίο τετράγωνο κάθε
φορά) αλλά πρέπει να παίρνει είσοδο από τον χρήστη κάθε φορά που παίζει. Τα
γράμματα ‘S’, ‘O’, ‘S’ μπαίνουν εναλλάξ. Να μετράει πόσες φορές κατάφερε να
συμπληρώσει την λέξη «SOS» ο χρήστης και πόσες ο υπολογιστής και να εντοπίζει
ποιος νίκησε.'''

import random
import os  # to clear screen
import time
try:
    # Plays a different song each time and sets the start animation timer accordingly.
    winsong = True
    a = random.randint(1, 3)
    if a == 1:
        import song
        songtime = 10
    elif a == 2:
        import song1 as song
        songtime = 29
    else:
        import song2 as song
        songtime = 17
except:
    print("Winsound library not found. You'll be denied the pleasure of the best music available to humans of this age.")
    time.sleep(2)
    winsong = False
    songtime = 0
import threading
import display


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def makeBoard():
    '''Makes an empty 10*10 board. '''
    B = [[" " for i in range(10)] for j in range(10)]
    return B


def printBoard(board):
    '''Takes a 10*10 board and prints it in a nice way.'''
    global pScore
    global cScore
    # print(" Welcome to the SOS Game! ")
    print("Current Scores: Player: {}  || Computer: {}".format(pScore, cScore))
    print("==========================")
    print("|Y\Χ|0|1|2|3|4|5|6|7|8|9||")

    for i in range(10):
        print("|"+str(i)+" |", end="")
        for j in range(10):
            print("|"+board[i][j], end="")
        print("||")
    print("==========================")


def getFreeSpace(table, c=(-1, -1)):
    '''Returns the coordinates of a random free space of a given table.
    If coords are given(c[0],c[1]>=0) returns True/False if given position
    is free'''
    if c[0] >= 0 and c[1] >= 0:
        if table[c[0]][c[1]] == " ":
            return True
        else:
            return False

    exists = False
    for row in table:
        for i in row:
            if i == " ":
                exists = True
    if exists == False:
        buffprint("Game Over! There is no free space left!")
        return False
    else:
        i = random.randint(0, len(table)-1)
        j = random.randint(0, len(table[0])-1)
        while table[i][j] != " ":
            i = random.randint(0, len(table)-1)
            j = random.randint(0, len(table[0])-1)
        return (i, j)


def evalTable(tab):
    '''Evaluates how many "SOS" there are on the table.
    Used to evaluate score, counting the amount of "SOS" in 2 states
    of the table: before and after a move.'''
    S = 0
    for i in range(10):
        for j in range(10):
            if tab[i][j] == "O":
                try:
                    if tab[i-1][j] == "S" and tab[i+1][j] == "S":
                        S += 1
                    if tab[i-1][j-1] == "S" and tab[i+1][j+1] == "S":
                        S += 1
                    if tab[i-1][j+1] == "S" and tab[i+1][j-1] == "S":
                        S += 1
                    if tab[i][j-1] == "S" and tab[i][j+1] == "S":
                        S += 1
                except:
                    pass
    return S


def computerMove(board):  # (c,l)=((a,b),"S")
    '''Calculates the computer's move and returns the board state '''
    global currentPlayer
    global cScore
    l = {0: "S", 1: "O"}[random.randint(0, 1)]
    c = getFreeSpace(board)
    temps = evalTable(board)
    # score = evalPosition(board, c, l)  # score=(score,scored)
    # cScore += score[0]
    board[c[0]][c[1]] = l
    ds = evalTable(board)-temps
    cScore += ds
    # if score[0] > 1:
    if ds > 1:
        buffprint(
            "The computer marks {} on {}, scores {} points and goes again!".format(l, c, ds))  # score[0] if old version
    # elif score[0] == 1:
    elif ds == 1:
        buffprint("The computer marks {} on {}, scores 1 point and goes again!".format(l, c))
    else:
        buffprint("The computer marks {} on {}.".format(l, c))
    if getFreeSpace(board):
        # if score[0] > 0:
        if ds > 0:
            # buffprint("The computer scores, so it goes again!")
            newBoard(board)
            computerMove(board)
        else:
            buffprint("Now it's the player's turn")
            currentPlayer = "P"
    else:
        buffprint("Game Over! The Results are:")
    return board


def playerMove(board):
    ''''Lets player make a move and returns board state.'''
    global currentPlayer
    global pScore

    def getpInput(board):
        try:
            buffprint("Please give me a Letter(S or A) and a set of coordinates\
in this format: '[Letter] [Row] [Column]' for example 'S 5 3'")
            In = input().split(" ")
            if In[0].upper() != "S" and In[0].upper() != "O":
                raise ValueError
            l = In[0]
            c = (int(In[1]), int(In[2]))
            if getFreeSpace(board, c) == False:
                raise SyntaxError  # not a syntax error but whatever works :P
        except ValueError:
            buffprint("Please, give the input in the correct format.")
            return getpInput(board)
        except SyntaxError:
            buffprint("That space is taken, please change your coordinates.")
            return getpInput(board)
        return (l, c)

    (l, c) = getpInput(board)
    temps = evalTable(board)
    # score = evalPosition(board, c, l)
    # pScore += score[0]
    board[c[0]][c[1]] = l.upper()
    ds = evalTable(board)-temps
    pScore += ds
    # if score[0] > 1:
    if ds > 1:
        buffprint("You marked {} on {} and scored {} points! Go again!".format(
            l, c, ds))  # Was score[0]
    # elif score[0] == 1:
    elif ds == 1:
        buffprint("Toy marked {} on {} and scored 1 point! Go again!".format(l, c))
    else:
        buffprint("You marked {} on {}.".format(l, c))
    if getFreeSpace(board):
        # if score[0] > 0:
        if ds > 0:
            # buffprint("You scored points, so you go again!")
            newBoard(board)
            playerMove(board)
        else:
            buffprint("Now it's the computer's turn")
            currentPlayer = "C"
    else:
        print("Game Over! The Results are:")
    return board

    # The following functions help with displaying the game in a nice way
printBuffer = []


def buffprint(string):
    if len(printBuffer) > 30:
        printBuffer.remove(printBuffer[0])
        # printBuffer.remove(printBuffer[0])
    a = string
    time.sleep(0.15)
    print(a)
    printBuffer.append(a)


def newBoard(board):
    clear()
    printBoard(board)
    for l in printBuffer:
        print(l)


def boardprint(board, text):
    newBoard(board)
    buffprint(text)


def clearBuffer():
    printBuffer.clear()


def PlayGame():
    '''Runs the game'''
    global currentPlayer
    global pScore
    global cScore
    playAgain = True
    if winsong == True:
        b = threading.Thread(target=song.play)
        b.start()
    display.display(songtime)
    time.sleep(2)

    while playAgain:
        '''
        # too annoying
        if not b.isAlive():
            b = threading.Thread(target=song.play)
            b.start()
        '''
        pScore = 0
        cScore = 0
        clearBuffer()
        board = makeBoard()
        newBoard(board)
        players = {1: "P", 2: "C"}
        startingPlayer = players[random.randint(1, 2)]

        if startingPlayer == "P":
            buffprint("You go first!")
        else:
            buffprint("The Computer Goes First!")
        currentPlayer = startingPlayer
        cont = True  # For base game loop

        while cont and getFreeSpace(board):
            '''
            if not b.isAlive():
                b = threading.Thread(target=song.play)
                b.start()
            '''
            if currentPlayer == "C":
                time.sleep(0.5)
                board = computerMove(board)
                newBoard(board)
            else:
                time.sleep(0.1)
                # board = computerMove(board)  # for debugging
                board = playerMove(board)
                newBoard(board)
        print("Final Score:")
        print("Player Score: {}".format(pScore))
        print("Computer Score: {}".format(cScore))
        if pScore > cScore:
            print("You win! Congrats!")
        elif cScore > pScore:
            print("You lost to a random bot? That's actually sad.")
        else:
            print("Draw!")
        if input("Do you wanna play again?(N for no)").lower().startswith("n"):
            playAgain = False


PlayGame()


#
#
#
#
#
# Deprecated Code Below:
#
#
#
#
# DEPRECATED - Thought of a WAY faster way.
def evalPosition(board, c, l):  # Board,Coodrinates,letter
    '''When symbol [s] is inserted in [c](coords - a tuple), scans board around it and evaluates completed SOSes.
    also returns a set of scored coordinates, so that they can be maked for the user to see.'''
    score = 0
    scored = set()
    if l.upper() == "O":
        try:
            if board[c[0]+1][c[1]] == "S" and board[c[0]-1][c[1]] == "S":  # Horiz
                score += 1
                scored.add(c)
                scored.add((c[0]+1, c[1]))
                scored.add((c[0]-1, c[1]))
        except:
            pass
        try:
            if board[c[0]][c[1]+1] == "S" and board[c[0]][c[1]-1] == "S":  # Vert
                score += 1
                scored.add(c)
                scored.add((c[0], c[1]+1))
                scored.add((c[0], c[1]-1))
        except:
            pass
        try:
            if board[c[0]+1][c[1]+1] == "S" and board[c[0]-1][c[1]-1] == "S":  # Diag1
                score += 1
                scored.add(c)
                scored.add((c[0]+1, c[1]+1))
                scored.add((c[0]-1, c[1]-1))
        except:
            pass
        try:
            if board[c[0]-1][c[1]+1] == "S" and board[c[0]+1][c[1]-1] == "S":  # Diag2
                score += 1
                scored.add(c)
                scored.add((c[0]-1, c[1]+1))
                scored.add((c[0]+1, c[1]-1))
        except:
            pass

    elif l.upper() == "S":
        try:
            if board[c[0]+1][c[1]+1] == "O" and board[c[0]+2][c[1]+2] == "S":  # NE
                score += 1
                scored.add(c)
                scored.add((c[0]+1, c[1]+1))
                scored.add((c[0]+2, c[1]+2))
        except:
            pass
        try:
            if board[c[0]+1][c[1]] == "O" and board[c[0]+2][c[1]] == "S":  # E
                score += 1
                scored.add(c)
                scored.add((c[0]+1, c[1]))
                scored.add((c[0]+2, c[1]))
        except:
            pass
        try:
            if board[c[0]+1][c[1]-1] == "O" and board[c[0]+2][c[1]-2] == "S":  # SE
                score += 1
                scored.add(c)
                scored.add((c[0]+1, c[1]-1))
                scored.add((c[0]+2, c[1]-2))
        except:
            pass
        try:
            if board[c[0]][c[1]-1] == "O" and board[c[0]][c[1]-2] == "S":  # S
                score += 1
                scored.add(c)
                scored.add((c[0], c[1]-1))
                scored.add((c[0], c[1]-2))
        except:
            pass
        try:
            if board[c[0]-11][c[1]-1] == "O" and board[c[0]-2][c[1]-2] == "S":  # SW
                score += 1
                scored.add(c)
                scored.add((c[0]-1, c[1]-1))
                scored.add((c[0]-2, c[1]-2))
        except:
            pass
        try:
            if board[c[0]-1][c[1]] == "O" and board[c[0]-2][c[1]] == "S":  # W
                score += 1
                scored.add(c)
                scored.add((c[0]-1, c[1]))
                scored.add((c[0]-2, c[1]))
        except:
            pass
        try:
            if board[c[0]-1][c[1]+1] == "O" and board[c[0]-2][c[1]+2] == "S":  # NW
                score += 1
                scored.add(c)
                scored.add((c[0]-1, c[1]+1))
                scored.add((c[0]-2, c[1]+2))
        except:
            pass
        try:
            if board[c[0]][c[1]+1] == "O" and board[c[0]][c[1]+2] == "S":  # N
                score += 1
                scored.add(c)
                scored.add((c[0], c[1]+1))
                scored.add((c[0], c[1]+2))
        except:
            pass
    if score > 0:
        return (score, scored)
    else:
        return (0, 0)
