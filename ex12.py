'''Γράψτε ένα πρόγραμμα το οποίο διαβάζει ένα αρχείο κειμένου και α) θα υπολογίζει και
εμφανίζει από πόσους χαρακτήρες, πόσες γραμμές και πόσες λέξεις αποτελείται το
αρχείο και β) θα αντικαταστήσει όλους τους χαρακτήρες με κεφαλαίους.'''

import os  # for path names

base = os.getcwd()+"/"
#file = "blablablabla.txt"
#file = "bla.txt"
#file = "lotrall.txt"
file = "lotr1.txt"
#file = "lotr2.txt"
# file = "lotr3.txt"
filepath = base+file


def readFile(path):
    '''Returns a string of all the contents of a file at [path].'''
    f = open(path, "r", encoding="utf-8")
    t = f.read()
    f.close()
    return t


def parseText(text):
    '''Parses the text and counts it's characters, lines, and (hopefully in an accurate way)words.'''
    commonSymbols = ["¬", "`", '"', "!", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
                     "[", "]", "{", "}", "#", "~", ";", ":", "'", "@", ",", "<", ".", ">", "/", "?", "|", "\\", "\n",
                     "\t", "\b", " ", "\r"]
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = commonSymbols+digits
    wc = 0
    lc = 1
    cc = len(text)
    for c in text:
        if c == "\n":
            lc += 1
    for i in range(len(text)):
        if text[i] not in symbols:
            continue
        wc += 1
    '''Counting words this way counts word separators that are more than a character
    long like ", " or ". " as 2 words, since in effect it counts separators and not
    words themselves. So I'll remove double and triple consecutive separators, with hopes
    that it'll reduce the error margin on large texts. '''
    # double symbols
    doubles = 0
    for i in range(len(text)-1):
        if (text[i] in symbols) and (text[i+1] in symbols):
            doubles += 1
    # triple symbols
    '''
    triples=0
    for i in range(len(text)-2):
        if (text[i] in symbols) and (text[i+1] in symbols) and (text[i+2] in symbols):
            triples+=1
    '''
    '''Funny thing here: I expected that a triple char separator would be counted twice as a double
     as well, but since a triple counted twice as a double, i am seemingly left with doubles only
     if I subtract the triples from the doubles? not sure what's happening but this seems to be
     getting the most accurate results, accross multiple test texts.'''
    extras = doubles  # -triples
    wc -= extras
    return (cc, lc, wc)
    #print(doubles, triples)
    # print()
    # print(wc,lc,cc)


def run():

    print("This program reads a text and prints the text's character count, \
line count and word count(to the best of my ability). ")
    print("Text source: {}".format(filepath))
    a = parseText(readFile(filepath))
    print("Char Count = {}".format(a[0]))
    print("Line Count = {}".format(a[1]))
    print("Word Count = {}".format(a[2]))
    if a[0] < 10000:
        print("\n\nFull Text follows below:\n")
        print(readFile(filepath))


# Run
run()
