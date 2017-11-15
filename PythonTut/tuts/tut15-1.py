'''
Created on Nov 13, 2017

@author: aleksandar.novic
'''

import re


def spacing():
    print("")
    

#match 0 or 1 specific thing
randStr = 'cat cats'

regex = re.compile("[cat]+s?")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

spacing()


randStr = "doctor doctors doctor's"


regex = re.compile("[doctor]+['s]*")

matches = re.findall(regex,randStr)

for i in matches:
    print(i)

spacing()
'''Problem'''

randStr = '''just some words
and some more\r
and more more
'''

regex = re.compile("[\w\s]+[\r]?\n")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

spacing()
'''DIFFERENCE BETWEEN GREEDY AND LAZY MATCHING
    in general lazy grabbing means grab the smallest match possible
    greedy is the opposite 
'''
    
randStr = "<name>Life on Mars</name><name>Freaks and Geeks</name>"

#greedy
regex = re.compile("<name>.*</name>")

#lazy
regex = re.compile("<name>.*?</name>")

#just data in tags
regex = re.compile("<name>(.*?)</name>")


matches = re.findall(regex, randStr)

for i in matches:
    print(i)
spacing()


'''WORD BOUNDARIES'''

#\b start as well as the end of the word
randStr = "ape at the apex"

regex = re.compile(r"\bape\b")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)

spacing()



'''STRING BOUNDARIES'''

# ^ is the beginning of the string
# $ the end of a string


randStr = "match everything up to @"

regex = re.compile(r"^.*[^@]")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

spacing()


randStr = "@ get this string"

regex = re.compile(r"[^@\s].*$")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)

spacing()

randStr = '''ape is big
turtle is slow
cheetah is fast'''

regex = re.compile(r"(?m)^.*?\s")

matches = re.findall(regex, randStr)
print(len(matches))

for i in matches:
    print(i)

spacing()


'''SUBEXPRESSIONS'''

randStr = "My number is 412-444-1212"

regex = re.compile(r"412-(.*)")

matches = re.findall(regex, randStr)
print(len(matches))

for i in matches:
    print(i)

spacing()


'''PROBLEM TO SOLVE'''

randStr = "412-555-1212 412-555-1213 412-555-1215"

regex = re.compile(r"412-(.{8})")

matches = re.findall(regex, randStr)
print(len(matches))

for i in matches:
    print(i)

spacing()

'''MULTIPLE SUBEXPRESSIONS'''

randStr = "My number is 412-555-1215"

regex = re.compile(r"412-(.*)-(.*)")

matches = re.findall(regex, randStr)
print(len(matches))

print(matches[0][0])
print(matches[0][1])

for i in matches:
    print(i)

spacing()









