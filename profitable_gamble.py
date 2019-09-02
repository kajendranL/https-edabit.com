#Profitable Gamble
def profitable_gamble(prob, prize, pay):
	if prob*prize>pay:
		return True
	else:
		return False
print("#Profitable Gamble")    
print(profitable_gamble(0.2, 50, 9)) # True
print(profitable_gamble(0.9, 1, 2)) # False
print(profitable_gamble(0.9, 3, 2)) # True		
