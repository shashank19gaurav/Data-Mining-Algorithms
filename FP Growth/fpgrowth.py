import operator
# from collection import defaultdict
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
        self.value = value
        self.count = 0
        self.childs = []
        self.parent = None
        
    def addChild(self, node):
        self.childs.append(node)
        pass

    def insertTransaction(self, transactionString):
        # Two case - 1. Root Node , 2. Other Node
        # 1. Other Node
        if len(transactionString) == 0:
            return
        if self.value == "Root":
            # print "Root Me Aaaya and Value hai", transactionString
            # Check if any of the child has the same value as the first value of the transaction
            # If exists then increase its count and recursively call this function on the child node
            for child in self.childs:
                if child.value == transactionString[:1] :
                    # Found a child with the same value
                    # Increasing its count
                    child.count += 1
                    # Append the rest of the transaction to its child
                    child.insertTransaction(transactionString[1:])
                    return

            # No child found, Make new nodes with the all the new transaction
            childNode = Node(transactionString[:1])
            childNode.parent = self
            self.childs.append(childNode)
            if len(transactionString) > 0:
                childNode.insertTransaction(transactionString[1:])

        else:
            # print "Root ke bete me Aaaya and Value hai", transactionString
            # The current node is not a root node
            # Check value accordingly
            if self.value == transactionString[:1] :
                self.count +=1
                # Check if further down, the string matches or not
                print "Checking in child of ", self.value, "for ", transactionString
                for child in self.childs:
                    if child.value == transactionString[1:2] :
                        # Found a child with the same value
                        # Increasing its count
                        child.count += 1
                        # Append the rest of the transaction to its child
                        child.insertTransaction(transactionString[1:])
                        return
                childNode = Node(transactionString[1:2])
                childNode.parent = self
                self.childs.append(childNode)
                if len(transactionString) > 0:
                    childNode.insertTransaction(transactionString[2:])
            else:
                parent = self.parent
                childNode = Node(transactionString[:1])
                childNode.parent = parent
                parent.childs.append(childNode)
                if len(transactionString) > 0:
                    childNode.insertTransaction(transactionString[1:])

    def generateFrequentSet(self, item):
        if self.value == item:
            return self.value + " - " + str(self.count)

        else:
            frequentItemSet = []
            for child in self.childs:
                if item in child.generateFrequentSet(item):
                    frequentItemSet.append(child.generateFrequentSet(item))

            return frequentItemSet



class Tree:
    def __init__(self):
        self.node = Node("Root")

    def updateWithTransaction(self, transactionString):
        self.node.insertTransaction(transactionString)

    def findFrequentItemSetForItem(self, item):
        print self.node.generateFrequentSet(item)

def comparePriority(x, y):
    global countEachItem
    return countEachItem[y] - countEachItem[x]

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

tree = Tree()

for transaction in transactionBasedOnPriority:
    tree.updateWithTransaction(transaction)

# Tree generated
# No go till the end of the tree
# List all the transactions and finally merge them back together
# 

for item in eachItem:
    tree.findFrequentItemSetForItem(item)

