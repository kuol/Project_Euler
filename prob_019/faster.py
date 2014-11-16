def main():
    print countDays(100,12,31)    

def countDays(Y,M,D):
    """Count how many Sundays, Mondays, Tuesdays... 
       from 01/01/1900 to M/D/(1900+Y)

       Parameters
       ----------
       Y: int
          How many years ahead of 1900. e.g.
       M: int
          Which month
       D: int
          Which day
      
       Returns
       -------
       count: list of int, size = 7
              Stores how many Sundays, Mondays, .... between 01/01/1900 
              to M/D/(1900+Y)
    """
    # Store how many first days of a month is Sunday, Monday ...
    count = [0]*7
    days = [31,28,31,30,31,30,31,31,30,31,30,31]

    count[1] = 1
    current = 1 
    for i in xrange(Y):
        leap = True if (i%100 and i%4 == 0) or (i%400==0) else False
        for j in xrange(M):
            if j == 1: # 0:Jan, 1:February
                offset = 29 if leap else 28
            else:
                offset = days[j]
            current = (offset%7 + current) % 7
            count[current] += 1
    return count


if __name__ == '__main__':
    main()
