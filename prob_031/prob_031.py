#/User/kuol/anaconda/bin/python

def f(m, coin):
	if m == 0:
		return 1
	else:
		i = 0
		while(m < coin[i]):
			i = i + 1
		if len(coin) > i+1:
			return f(m - coin[i], coin[i:]) + f(m, coin[i+1:])
		else:
			return f(m - coin[i], coin[i:])


coin = [200,100,50,20,10,5,2,1]
money = 200

#coin = [10,5,2,1]
#money = 10

#coin = [3,2,1]
#money = 3

print "Total number of ways to change is: %d" %f(money, coin)
