import operator
from collection import defaultdict
print "No of transactions: "
nTransaction = input()

# Take User input for all the transactions
print "Enter the %s transaction(s) :"  %(nTransaction)
transactions = []
eachItem = set()
countEachItem = {}
transactionBasedOnPriority = []


class Node:
     def __init__(self, value):
        self.data = value
        self.childs = []

class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node , data):
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # Else Add the child 
            node.childs = self.insert(node.left, data)
        return node


    def search(self, node, data):
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)



def comparePriority(x, y):
    global countEachItem
    return countEachItem[x] - countEachItem[y]

i = 0
while i<nTransaction:
    transactions.append(raw_input())
    i+=1

# Make a list of each item present in the transaction
for transaction in transactions:
    eachItem.update((list(transaction)))

# Prepare a dictionary of each item
for item in eachItem:
    countEachItem[item] = 0

# Count the number of occurrence of each item
for item in eachItem:
    for transaction in transactions:
        countEachItem[item] += transaction.count(item)

for transaction in transactions:
        transactionBasedOnPriority.append(''.join(sorted(transaction,  cmp = comparePriority)))

print "Update transactions based on Priority :", transactionBasedOnPriority
# We have transaction based on the priority
# Next task is to create FP Tree


