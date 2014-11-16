words = [3, #one
        3, #two
        5, #three
        4, #four
        4, #five
        3, #six
        5, #seven
        5, #eight
        4, #nine
        3, #ten
        6, #eleven
        6, #twelve
        8, #thirteen
        8, #fourteen
        7, #fifteen
        7, #sixteen
        9, #seventeen
        8, #eighteen
        8, #nineteen
        6, #twenty
        6, #thirty
        5, #forty
        5, #fifty
        5, #sixty
        7, #seventy
        6, #eighty
        6] #ninety
#        7 #hundred
#        8 #thousand

#numbers end  with 1 to 19 -- without counting "xx hundred and" part
a = sum(words[:19])*10 
# numbers end with 20 ~ 99 -- without counting "xx hundred and" part
b = sum(words[19:])*10*10 + sum(words[:9])*80

# numbers from 1 ~ 999 -- only counting "xx hundred (and)" part
c = sum(words[:9])*100 + 10*900 - 3*9 

thousand = 3 + 8 

print a + b + c + thousand























