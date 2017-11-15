'''
Created on Nov 12, 2017

@author: aleksandar.novic
'''

import re

def spacing():
    print("")
    print("")
    print("")

if re.search("ape", "The ape was at apex"):
    print("there is an ape")

allApes = re.findall("ape.", 'the ape was at apex')

for i in allApes:
    print(i)

theStr = "The ape was at apex"

for i in re.finditer("ape.", theStr):
    locTuple = i.span()
    
    print(locTuple)
    
    print(theStr[locTuple[0]:locTuple[1]])

animalStr = "cat rat mat pat"
allAnimals = re.findall("[crmfp]at", animalStr)
for i in allAnimals:
    print(i)
print("")

someAnimals = re.findall("[^c-mC-M]at", animalStr)

for i in someAnimals:
    print(i)

spacing()

owlfood = 'rat cat mat pat'

regex = re.compile('[cr]at')
owlfood = regex.sub('owl', owlfood)
print(owlfood)

spacing()

randStr = "F.B.I. I.R.S. CIA"
print("Matches:", len(re.findall('.\..\..\.', randStr)))

spacing()

#MATCH FOR WHITESPACE

randStr = '''this is a long string
that goes
in many lines
'''

print(randStr)
regex = re.compile('\n')
randStr = regex.sub(' ', randStr)
print(randStr)

''' osim za whitespace moze i za sledece:
\b : backspace
\f : form feed
\r : carrige return
\t : tab
\v : vertical tab
windows only \r\n za newline
'''

''' numbers

\d : [0-9] sve sto je od 0 do 9
\D : [^0-9] sve sto NIJE 0-9
'''
randStr = '12345'
print('Matches:', len(re.findall('\d', randStr)))
print('Matches:', len(re.findall('\d{2}', randStr))) #match za vise brojeva


numStr = '123 12345 123456 1234567'

print('MAtches:', len(re.findall('\d{5,7}', numStr)))

''' now matching any SINGLE LETTER OR NUMBER
\w : [a-zA-z0-9_]
\W : [^a-zA-Z0-9_]
'''
phNum = '412-555-1212'

if re.search('\w{3}-\w{3}-\w{4}', phNum):
    print('Its a phone num')

if re.search('\w{2,20}', 'Ultraname'):
    print('Is a valid name')

'''shortcut for whitespace
\s : [\f\n\r\t\v]
\S : [^\f\n\r\t\v]
'''

if re.search('\w{2,20}\s\w{2,20}', 'Tomas Tomashin'):
    print('it is valid')

print('matches:', len(re.findall('a+', 'a as ape bug')))

'''PROBLEM'''

emailStr = 'aleks.origin@gmail.com asdf@goog.com zub.rs oop1@k.co'

#ovako ne valja
print('email matches:', len(re.findall("\w[a-zA-Z._%+-]{1,20}@\w[a-zA-Z0-9.-]{2,20}.\w[a-z]{2,3}", emailStr)))
#ovako valja
print('email matches:', len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", emailStr)))
#                                       ^^^^^^^^^















