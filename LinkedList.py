class Node:
    '''
    Represents an individual element in the Linked List
    '''
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_linked_list(self):
        '''
        Prints a representation of the Linked List.
        '''
        if self.head is None: # If the Linked List is empty
            print('The Linked List is empty.')
            return

        itr = self.head # Assign the head to an iterator variable (itr)
        linked_list_string = ''
        while itr:
            linked_list_string += str(itr.data) + '-->'
            itr = itr.next
        linked_list_string += 'None'
        
        print(linked_list_string)

    def insert_at_start(self, data):
        '''
        Inserts a Node (node) at the start of the Linked List
        The next pointer points to the previous head of the Linked List
        The head pointer points to the new node
        '''
        node = Node(data, self.head)
        self.head = node

if __name__ == '__main__':
    pass