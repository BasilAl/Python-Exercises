'''Γράψτε ένα πρόγραμμα το οποίο θα αναζητάει σε ένα αρχείο κειμένου μια λέξη που θα
δίνει ο χρήστης και θα στην αντικαθιστά με μια άλλη λέξη που θα δίνει, επίσης, ο
χρήστης σε όλο το αρχείο.'''
# Replace filepath with whatever.
import os  # for path names

base = os.getcwd()
filepath = base+"/blablabla.txt"


def readFile(path):
    '''Returns a string of all the contents of a file at [path].'''
    f = open(path, "r")
    t = f.read()
    f.close()
    return t


def replaceText(text, word, repl):
    '''Replaces a [word] in a given text with [repl]'''
    return text.replace(word, repl)


def overwriteFile(path, text):
    '''Writes [text] to file at [path], replacing anything already written.'''
    f = open(path, "w")
    f.write(text)
    f.close()


def run(file, word, replace):
    '''Replaces [word] in [file] with [replace]'''
    print("This will replace every '{}' in {} with '{}'.".format(word, file, replace), end='\n\n')
    f = readFile(file)
    r = replaceText(f, word, replace)
    overwriteFile(file, r)
    print("Successfully replaced words in text.")


# Run
run(filepath, "foo", "bar")
