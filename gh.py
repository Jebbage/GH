def Deck(a,b=0,c=0,r=0):
	base = [a]*6 + [a+1,a-1]*5 + [a+2,a-2,0] + [2*a]*(b+1)
	deck = [card if card >= 0 else 0 for card in base]
	return deck + ["r"]*r

def AverageAttack(a,b=0,c=0,r=0,customDeck=None):
	deck = customDeck if customDeck != None else Deck(a,b,c,r)
	if deck.count("r") > 0:
		rollingAdd = AverageAttack(a+1, b, r-1)
	return sum([card if card != "r" else rollingAdd for card in deck])/float(len(deck))

def AverageAttackAdvantage(a,b=0,c=0,r=0,customDeck=None):
	deck = customDeck if customDeck != None else Deck(a,b,c,r)

	rolls = ["r"] * deck.count("r")
	nonRolls = [card for card in deck if card != "r"]

	m = len(nonRolls)
	n = len(rolls)
	zeroRollsCount = 0.5*m*(m-1)
	oneRollsCount = m*n
	twoRollsCount = 0.5*(n)*(n-1)

	zeroRollsTotal = sum([max(i,j) for n, i in enumerate(nonRolls) for j in nonRolls[n+1:]])
				#  = sum of the greater number of every pair of non-rolling cards
	oneRollsTotal = AverageAttack(a+1,b,c,0) * oneRollsCount
				# = sum of damage from each pair of non-rolling+rolling cards
	twoRollsTotal = AverageAttack(a+2,b,c,r-2) * twoRollsCount
				# = sum of expected damage of two rolling cards + continuing to draw
	
	allTotal = sum([zeroRollsTotal, oneRollsTotal, twoRollsTotal])
	allCount = sum([zeroRollsCount, oneRollsCount, twoRollsCount])
	return allTotal/allCount

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
