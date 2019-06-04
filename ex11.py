'''Γράψτε ένα πρόγραμμα το οποίο διαβάζει ένα αρχείο κειμένου και αφού βρει τα
στατιστικά εμφάνισης του κάθε γράμματος και να τα εμφανίζει ταξινομημένα κατά
αύξουσα σειρά με βάση το πόσες φορές εμφανίζεται το κάθε γράμμα.'''

# Replace filepath with whatever.
import os  # for path names

# Filenames
base = os.getcwd()+"/"


file = 'lotr1.txt'
#file = 'lotr2.txt'
#file = 'lotr3.txt'
#file = 'lotrall.txt'
filepath = base+file


def readFile(path):
    '''Returns a string of all the contents of a file at [path].'''
    f = open(path, "r", encoding='utf-8')
    t = f.read()
    f.close()
    return t


def parseText(text):
    '''Parses a text and generates a dictionary of all characters
    and the amount of times they appear in the text.'''
    d = {}
    # Changed to .lower() to not differentiate upper and lower case of same letter.
    for i in text:
        if i.lower() in d:
            d[i.lower()] += 1
        else:
            d[i.lower()] = 1

    return d


def processData(dict):
    '''Processes a dictionary whose keys are the characters
    that appear in a text and the corresponding values are the
    times each character appears, filters out common symbols
    and prints a list of (hopefully)only letters in increasing
    frequency of occurence'''
    commonSymbols = ["¬", "`", '"', "!", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
                     "[", "]", "{", "}", "#", "~", ";", ":", "'", "@", ",", "<", ".", ">", "/", "?", "|", "\\", "\n",
                     "\t", "\b", " ", "\r", "’", "”", "“", "﻿", "—", "®"]  # the "﻿" character here is actually an invisible char that popped up while parsing an e-pub and not the string denoting nothing.
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    commonChars = commonSymbols+digits
    # Clear dict of non-letters
    for c in commonChars:
        try:
            dict.pop(c)
        except KeyError:
            pass
    cList = []
    for l in dict:
        cList.append((dict[l], l))
    cList.sort()
    print("These are the characters found in the given text, in order of increasing occurence: \n")
    print("Letter : Occurence \n")
    for i in range(len(cList)):
        print("   {}   :   {}  ".format(cList[i][1], cList[i][0]))


def Run(filepath):
    f = readFile(filepath)
    d = parseText(f)
    print("Current text file: {}".format(filepath))
    processData(d)


# Run
Run(filepath)
