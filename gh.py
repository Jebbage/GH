import matplotlib.pyplot as plt

def Deck(a,b,c,r):
	base = [a]*6 + [a+1,a-1]*5 + [a+2,a-2,0] + [2*a]*(b+1)
	deck = [card if card >= 0 else 0 for card in base]
	return deck + ["r"]*r

def AverageAttack(a,b=0,c=0,r=0,customDeck=None):
	deck = customDeck if customDeck != None else Deck(a,b,c,r)

	total = 0
	count = 0
	calculateOnce = True
	for card in deck:
		if card != "r":
			total += card
		else:
			if calculateOnce:
				rollingAdd = AverageAttack(a+1, b, r-1)
				calculateOnce = False
			total += rollingAdd
		count += 1
	return float(total)/count

def AverageAttackAdvantage(a,b=0,c=0,r=0,customDeck=None):
	deck = customDeck if customDeck != None else Deck(a,b,c,r)

	total = 0
	count = 0
	calculateOnce = True
	for n, first in enumerate(deck):
		for second in deck[:n]+deck[n+1:]:
			if first == second == "r":
				if calculateOnce:
					valueOfRolling = AverageAttack(a+2, b, r-2)
					calculateOnce = False
				total += valueOfRolling
			if first != second == "r":
				total += first + 1
			if second != first == "r":
				total += second + 1
			if first != "r" and second != "r":
				total += max(first, second)
			count += 1

	return float(total)/count

def AverageAttackDisadvantage(a,b=0,c=0,r=0,customDeck=None):
	deck = customDeck if customDeck != None else Deck(a,b,c,r)
	nonRolls = [card for card in deck if card != "r"]
	nonRollAverage = float(sum(nonRolls))/len(nonRolls)

	total = 0
	count = 0
	for n, first in enumerate(deck):
		for second in deck[:n]+deck[n+1:]:
			if first == second == "r":
				total += nonRollAverage
			if first != second == "r":
				total += first
			if second != first == "r":
				total += second
			if first != "r" and second != "r":
				total += min(first, second)
			count += 1

	return float(total)/count