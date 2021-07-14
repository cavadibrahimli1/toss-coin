#You are trying to decide if you should play the following game:

#You are given \$5$5 for free.
#You keep flipping a fair coin until you get two tails in a row.
#Before each flip including the first one, you pay a \$1$1 fee.
#If the number of flips exceeds 5,5, the \$1$1 fee must keep coming out of your own pocket
#You decide to play the game if the expected result is a profit. Should you play the game?
#Hint: The expected number of times you must pay \$1$1 is the expected number of tosses needed to get two tails in a row.

import random
trylist = []
profit = []
winCount = 0
loseCount = 0

for i in range(1000):
        trylist.append(random.randint(1,2))
        trylist.append(random.randint(1,2))

        if (trylist[len(trylist)-2] == 2) and (trylist[len(trylist)-1] == 2):
                profit.append(5-len(trylist))
                trylist.clear()
for l in profit:
    if l > 0:
        winCount += 1
    if l < 0:
        loseCount += 1

if winCount > loseCount:
    print("Play")
elif winCount < loseCount:
    print("Nope")
