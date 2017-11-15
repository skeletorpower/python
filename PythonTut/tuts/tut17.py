'''
Created on Nov 14, 2017

@author: aleksandar.novic
'''

import re

def spacing():
    print('')

'''BACK REFERENCE'''

randStr = 'the cat cat fell out the window'

regex = re.compile(r"(\b\w+)\s+\1")

matches = re.findall(regex, randStr)

print('matches:', len(matches))

for i in matches:
    print(i)

spacing()


randStr = "<a href = '#'><b>The link</b></a>"

regex = re.compile(r"<b>(.*?)</b>")

randStr = re.sub(regex, r"\1", randStr)

print(randStr)

spacing()



randStr = "412-555-1212"

regex = re.compile(r"([\d]{3})-([\d]{3}-[\d{4}])")

randStr = re.sub(regex, r"(\1)\2", randStr)

print(randStr)

spacing()



'''1st PROBLEM'''

randStr = "https://www.youtube.com http://www.google.com"

regex = re.compile(r"(https?://([\w.]+))")

randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)

print(randStr)


'''LOOK AHEAD'''

#(?=expression)

randStr = "one two three four"

regex = re.compile(r"\w+(?=\b)")

matches = re.findall(regex, randStr)
for i in matches:

    print(i)

spacing()
'''LOOK BEHIND'''

#(?<=expression)

randStr = "1. Bread 2. Apples 3. Lettuce"

regex = re.compile(r"(?<=\d.\s)\w+")

matches = re.findall(regex, randStr)
for i in matches:

    print(i)















