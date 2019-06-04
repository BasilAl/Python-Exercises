'''Γράψτε ένα πρόγραμμα το οποίο θα αφαιρεί τα κενά, τους χαρακτήρες αλλαγής
γραμμής και τα tabs από το περιεχόμενο ενός αρχείου.'''

import os  # for filepath


# Replace file with whatever filename in the folder..
file = "blablabla.txt"
base = os.getcwd()+"/"
filepath = base+file


def readFile(path):
    '''Returns a string of all the contents of a file at [path].'''
    f = open(path, "r")
    t = f.read()
    f.close()
    return t


def removeWhiteSpace(text):
    '''Removes whitespace and newlines from a string.'''
    return text.replace(" ", "").replace("\t", "").replace("\n", "")


def overwriteFile(path, text):
    '''Writes [text] to file at [path], replacing anything already written.'''
    f = open(path, "w")
    f.write(text)
    f.close()


# Run
print("This program removes whitespace and newlines from a given text(hardcoded).\n")
overwriteFile(filepath, removeWhiteSpace(readFile(filepath)))
print("Whitespace and newlines removed from {}".format(file))
