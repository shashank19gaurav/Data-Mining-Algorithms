#This is a very basic implementation of Dynamic Itemset Implementation
# 4 item set needs to be mantained.
# Frequent
solidSquare = {}
# Suspected Frequent
dashedSquare = {}
# Infrequent
solidCircle = {}
# Suspected Infrequent  
dashedCircle = {}

transactions = []


from itertools import combinations
perms = [''.join(p) for p in combinations('ABCCD', 2)]
print perms


# No of steps before everything is calcualted again
print "Value of M? :"
M = int(raw_input())
    
print "Minimum Support? :"
minSupport = int(raw_input())

print "Count of transactions?:"
transactionCount = int(raw_input())

print "Itemsets ?:"
print "Note: Each character is considered as one item set"
while transactionCount!=0:
    transactions.append(raw_input()) 
    transactionCount = transactionCount - 1



# Add all the invidual items in the
i = 0
while i < len(transactions):
    j = 0
    while j<len(transactions[i]):
        if transactions[i][j] in dashedSquare:
            # dashedSquare[transactions[i][j]] = dashedSquare[transactions[i][j]] + 1
            pass
        else:
            dashedCircle[transactions[i][j]] = 0
        j = j+1
    i = i + 1

currentTransaction = 0
while len(dashedSquare)>0 or len(dashedCircle)>0:
    mCounter = 0
    while mCounter < M:
        if currentTransaction == len(transactions):
            currentTransaction = 0
        for eachKey in dashedSquare.keys():
            if transactions[currentTransaction].count(eachKey):
                dashedSquare[eachKey] = dashedSquare[eachKey] + transactions[currentTransaction].count(eachKey)
        for eachKey in dashedCircle.keys():
            if transactions[currentTransaction].find(eachKey):
                dashedCircle[eachKey] = dashedCircle[eachKey] + 1
        currentTransaction = currentTransaction + 1
        mCounter = mCounter + 1
    # Do all the calculation here
    print dashedCircle
    print dashedSquare
    for eachKey in dashedCircle.keys():
        if dashedCircle[eachKey] > minSupport:
            solidSquare[eachKey] = dashedCircle[eachKey]
            del dashedCircle[eachKey]
    for eachKey in dashedSquare.keys():
        if dashedSquare[eachKey] > minSupport:
            solidSquare[eachKey] = dashedSquare[eachKey]
            del dashedSquare[eachKey]
    break
print solidSquare

