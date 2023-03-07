class Node:
    '''
    Represents an individual element in the Linked List
    Parameters: data, next
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
        Time Complexity: O(n)
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
        1. Creates a new node with the data
        2. Assignes the current head as the next element in the Linked List
        3. Sets the new node as the head of the Linked List
        
        Time Complexity: O(1)
        '''
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_index(self, index, data):
        '''
        Inserts a node with data at a specific index location.
        '''
        if index < 0 or index >= self.get_length(): # Validate the index
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_start(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_at_end(self, data):
        '''
        Inserts a new Node at the end of the Linked List
        1. Iterates through the entire Linked List
        2. Point the next pointer of the last element to a new Node which points to None

        Time Complexity: O(n)
        '''
        if self.head is None: # If the Linked List is empty
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def create_new_linked_list(self, values):
        '''
        Takes a list of values, creates a new Linked List
        '''
        self.head = None
        for val in values:
            self.insert_at_end(val)

    def get_length(self):
        '''
        Returns the length of the Linked List
        '''
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def delete_index(self, index):
        '''
        Removes the element at the particular index
        Time Complexity: O(n) (worst case) 
        '''
        if index < 0 or index >= self.get_length(): # Validate the index
            raise Exception('Invalid Index')
        if index == 0: # Remove the head
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def remove_all(self, value):
        '''
        Removes all occurences of value from the Linked List.
        Returns the new head of the Linked List.
        '''
        if self.head is None:
            return 'The Linked List is empty.'
        itr = self.head
        while itr:
            if itr == self.head and itr.data == value: # If the value is at the head of the Linked List
                if itr.next == None: #If there is only one Node in theh Linked List
                    self.head = None
                    return self.head
                itr = itr.next
                self.head = itr
            else:
                if itr.data != value:
                    prev = itr
                    itr = prev.next
                if itr == None: # If we are at the end of the Linked List
                    return self.head
                prev.next = itr.next
                itr = itr.next
    
    def remove_nth_from_end(self, n):
        '''
        Removes the element at the nth index from the end of the Linked List
        '''
        length = self.get_length()
        if length == 0:
            return 'The Linked List is Empty'
        index = length - n
        print('index:',index)
        self.delete_index(index)
    

                    



if __name__ == '__main__':
    #####################################################################################################
    #                                              Testing                                              #
    #####################################################################################################
    ll1 = LinkedList() # Create Linked List 1
    ll2 = LinkedList() # Create Linked List 2
    ll3 = LinkedList() # Create Linked List 3
    ll4 = LinkedList() # Create Linked List 4
    ll5 = LinkedList() # Create Linked List 5
    ll6 = LinkedList() # Create Linked List 6
    
    # Test creating an empty Linked List
    assert ll1.print_linked_list() == None, 'print_linked_list fails for empty Linked List'

    # Test inserting at the start of a Linked List
    print('\nInsert 2 at the start of Linked List 1') # Inserting at the start of an empty Linked List
    ll1.insert_at_start(2)
    assert ll1.print_linked_list() == '2-->None', 'either print_linked_list or insert_at_start fails for inserting at the start of an empty Linked List'

    print('\nInsert 1 at the start of Linked List 1')
    ll1.insert_at_start(1)
    assert ll1.print_linked_list() == '1-->2-->None', 'either print_linked_list or insert_at_start fails for inserting at the start of a Linked List'

    # Test inserting at the end of a Linked List
    print('\nInsert 3 at the end of Linked List 1')
    ll1.insert_at_end(3)
    assert ll1.print_linked_list() == '1-->2-->3-->None', 'either print_linked_list or insert_at_start fails for inserting at the end of a Linked List'

    print('\nInsert A at the end of Linked List 2') # Inserting the end of an empty Linked List
    ll2.insert_at_end('A')
    assert ll2.print_linked_list() == 'A-->None', 'either print_linked_list or insert_at_start fails for inserting to the end of an empty linked list'

    # Test creating a new Linked List from a list of values
    print("\nCreate a new Linked List (Linked List 3) from a list (['Jeanette', 'Camille', 'Danielle'])")
    values = ['Jeanette', 'Camille', 'Danielle']
    ll3.create_new_linked_list(values)
    assert ll3.print_linked_list() == 'Jeanette-->Camille-->Danielle-->None', 'either print_linked_list or create_new_linked_list fails'

    # Testing get_length()
    print('The length of Linked List 3 is:', ll3.get_length())
    assert ll4.get_length() == 0, 'get_length() does not work on an empty Linked List' # Testing get_length() on an empty Linked List
    assert ll3.get_length() == 3, 'get_length() does not work'

    #Test delete_index()
    print('\nDeleting the element at the head of a Linked List (Linked List 1)')
    print('before:')
    ll1.print_linked_list()
    ll1.delete_index(0)
    print('after:')
    assert ll1.print_linked_list() == '2-->3-->None', 'delete_index() does not work as expected when deleting the head of a Linked List.'

    print('\nDeleting the element at the end of a Linked List (Linked List 1)')
    print('before:')
    ll1.print_linked_list()
    ll1.delete_index(1)
    print('after:')
    assert ll1.print_linked_list() == '2-->None', 'delete_index() does not work as expected when deleting the end of a Linked List.'

    print('\nDeleting an element in a Linked List (Linked List 3)')
    print('before:')
    ll3.print_linked_list()
    ll3.delete_index(1)
    print('after:')
    assert ll3.print_linked_list() == 'Jeanette-->Danielle-->None', 'delete_index() does not work as expected when deleting an element in a Linked List.'

    # Test insert_at_index()
    print('\nInserting an element at index 1 (Linked List 3)')
    print('before:')
    ll3.print_linked_list()
    ll3.insert_at_index(1,'Camille')
    print('after:')
    ll3.print_linked_list()

    # Test remove_all()
    print('\nTesting removing all of the occurences of a value from the Linked List.')
    lst = [1,1,1,1,1,1]
    value = 1
    ll5.create_new_linked_list(lst)
    print('before:')
    ll5.print_linked_list()
    print('value:', value)
    ll5.remove_all(value)
    print('after:')
    ll5.print_linked_list()

    # Test remove_nth_from_end()
    print('\nTesting removing the nth index from the end.')
    lst = [1,2,3,4,5,6]
    n = 1
    ll6.create_new_linked_list(lst)
    print('before:')
    ll6.print_linked_list()
    print('nth index from the end:', n)
    ll6.remove_nth_from_end(n)
    print('after:')
    ll6.print_linked_list()


    print('\nAll tests pass :)' + '\n')
    #####################################################################################################