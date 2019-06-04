'''Γράψτε ένα πρόγραμμα το οποίο επισκέπτεται μία ιστοσελίδα HTML που παίρνει από
τον χρήστη και α) εμφανίζει τον τίτλο του header, β) βρίσκει πόσες κεφαλίδες <h1>,
<h2> και <h3> υπάρχουν και γ) βρίσκει πόσες αλλαγες γραμμής από br υπάρχουν.'''

import urllib.request
#url = "http://www.unipi.gr/unipi/el/"
#url = "http://www.google.com"
#url = "https://gunet2.cs.unipi.gr"
url = "https://sarantakos.wordpress.coaam"
#url = "https://www.python.org"
#url = "https://students.cs.unipi.gr"


def getResponse(url):
    '''Returns a string of the response, decoded to unicode for easier manipulation'''
    try:
        return urllib.request.urlopen(url).read().decode('utf-8')
    except:
        print("Some error occured: Check the url you gave or your internet connection.")


def parseResponse(text):
    '''Parses a url response and searches for the title, and also counts <h1>,<h2>,<h3> tags
    as well as the number of newlines(<br>) and prints them all'''
    try:
        brcount, h1c, h2c, h3c = 0, 0, 0, 0
        brcount = text.count("<br")
        h1c = text.count("<h1")
        h2c = text.count("<h2")
        h3c = text.count("<h3")
        c = text.index("<title")
        d = text.index("</title")
        subt = text[c:d]
        a = subt.index(">")
        title = subt[a+1:d]
        print("Title : {}".format(title))
        print("<h1> count: {}".format(h1c))
        print("<h2> count: {}".format(h2c))
        print("<h3> count: {}".format(h3c))
        print("<br> count: {}".format(brcount))
    except:
        pass


# Run
print("Gets the Title, line count and header(h1,h2,h3) count for {}".format(url))
parseResponse(getResponse(url))
