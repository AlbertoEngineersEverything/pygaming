import os

f = open('readmyself.py', 'r')
for line in f:
    print(line.rstrip('\n'))
f.close()
################
f = open('readmyself.py', 'r')
for line in f:
    print(line)
f.close()
