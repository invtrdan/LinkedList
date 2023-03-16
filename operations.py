from LinkedList import Node, LinkedList

##################################################
#                    Creation                    #
##################################################
'''
Time Complexity
    - One Node: O(1)
    - Multiple Nodes: O(n)
Space Complexity
    - One Node: O(1)
    - Multiple Nodes: O(n)
'''
def createDefaultList():
    head = Node("A")
    head.next = Node("B")
    head.next.next = Node("C")
    head.next.next.next = Node("D")
    return head # A -- > B --> C --> D

# OR

def createDefaultList():
    return Node("A", Node("B", Node("C", Node("D")))) # A -- > B --> C --> D
    
##################################################
#                   Traversal                    #
##################################################
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

def printList(head):
    if head == None: # If the LinkedList is empty
        return
    temp = head # Assign ref to the head of the LinkedList to a temp variable
    while temp != None:
        print(str(temp.data)+"-->", end = '')
        temp = temp.next
    print(str(None))

##################################################
#                   Insertion                    #
##################################################
'''
Time Complexity
    - At Head: O(1)
    - Any other position: O(position)
Space Complexity: O(1)
'''
def insertNode(data, head = None, position = 0):
    if head == None:
        return Node(data)
    if position == 0: # inserting at the head - use construcor
        return Node(data, head) # new node posits to the prev head

    temp = head
    prev = None
    count = 0

    while temp != None and count < position:
        prev = temp
        temp = temp.next
        count += 1
    node = Node(data, temp)
    prev.next = node
    return node

##################################################
#                    Deletion                    #
##################################################

def deleteNodeWithValue(value):
    if head == None:
        raise "Empty List."
    if head.data == value:
        head = head.next
        return
    temp = head
    prev = None

    while temp != None and temp.data != value:
        prev = temp
        temp = temp.next
    if temp == None:
        raise "Value not in list"

##################################################
#                    Reverse                     #
##################################################

