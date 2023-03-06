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
        return linked_list_string

    def insert_at_start(self, data):
        '''
        Inserts a new Node at the start of the Linked List
        '''
        node = Node(data, self.head)
        self.head = node

if __name__ == '__main__':
    #####################################################################################################
    #                                              Testing                                              #
    #####################################################################################################
    ll1 = LinkedList() # Create Linked List 1
    assert ll1.print_linked_list() == None, 'print_linked_list fails for empty Linked List'

    print('\nAdd 2 to the start of the Linked List')
    ll1.insert_at_start(2)
    assert ll1.print_linked_list() == '2-->None', 'either print_linked_list or insert_at_start fails for Linked List with one Node'

    print('\nAdd 1 to the start of the Linked List')
    ll1.insert_at_start(1)
    assert ll1.print_linked_list() == '1-->2-->None', 'either print_linked_list or insert_at_start fails for Linked List with two Nodes'

    print('\nAll tests pass :)' + '\n')
    #####################################################################################################