# Store how many first days of a month is Sunday, Monday ...
count = [0]*7
days = [31,28,31,30,31,30,31,31,30,31,30,31]

count[1] = 1
current = 1 
for i in xrange(100):
    leap = True if (i%100 and i%4 == 0) or (i%400==0) else False
    for j in xrange(12):
        if j == 1: # 0:Jan, 1:February
            offset = 29 if leap else 28
        else:
            offset = days[j]
        current = (offset%7 + current) % 7
        count[current] += 1
print count

