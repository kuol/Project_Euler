#!/home/kuol/anaconda/bin/python
# use bash commands to remove all quotes: "
# cat names.txt | tr -d \" > new_names.txt
import numpy as np
names = np.genfromtxt('new_names.txt', delimiter=',', dtype='str')
names.sort()


def raw_score(string):
    return sum([ord(char)-64 for char in string.upper()])

score = 0
rank = 1
for i in range(len(names)):
    score = score + raw_score(names[i]) * rank
    rank = rank + 1

print "Total score is: %d" %score 

