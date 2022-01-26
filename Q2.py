###
# Name: Jett Gazeley
# Student Number: 20216732
# 2. Implementing Stack: 15 points
###

class ListNode:
    def __init__(self, value):
        ''' initalize data, and next for the linked list node'''
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        ''' initalize the head, tail, and size of the linked list'''
        self.head = None

        self.tail = None
        self.size = 0
    
    def push(self, value):
        ''' Used to push a new element onto the top of the stack'''
        new_node = ListNode(value)

        # remember to check edge case, while you are inserting into an empty linkedlist
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    
    def pop(self):
        ''' Used to return and remove the top element of the stack'''
        if self.size == 0:
            print("Can't remove from empty linked list")
            return
        else:
            self.head = self.head.next
            self.size -= 1


    def __str__(self):
        ''' Used to output the results of the linked list'''
        output = []
        node = self.head
        
        while node:
            output.append(node.data)
            node = node.next
        # note: str(item) is needed because item could be integer
        return "->".join([str(item) for item in output])




class Stack:
    def __init__(self):
        ''' Create an empty stack '''
        self.data = []
        self.head = None

    def is_empty(self):
        ''' This function checks whether the current Stack instance is
        empty. It should return true if the Stack is empty '''
        if len(self.data) == 0:
            print("Stack is empty")
            return True
        else:
            print("Stack is not empty")
            return False

    def push(self, element):
        ''' This function should takes a data item as input and add it into the Stack '''
        self.data.append(element)

    def top(self):
        ''' This function should return the data item on the top of the current
        Stack without modifying the Stack '''
        return self.data[-1]

    def pop(self):
        ''' This function should return the data item on the top of the current 
        Stack and remove it from the Stack '''
        return self.data.pop()

    def size(self):
        ''' This function should return the number of data items in the Stack '''
        return len(self.data)




def array_test():
    ### Array based implementation ###

    #Create a stack object
    stack = Stack()

    #Test for push
    stack.push(5)
    
    #Test for top as it should return 5
    print(stack.top())

    #Print stack size to showcase size of 1
    print(stack.size())

    #Test for pop as it returns 5
    print(stack.pop())

    #Print stack size to showcase size of 0
    print(stack.size())

    #Test for is_empty
    stack.is_empty()


def linked_list_test():
    ### Linked List based implementation ###
    linked_list = LinkedList()

    linked_list.push(4)
    print(linked_list)

    linked_list.pop()
    print(linked_list)


if __name__ == "__main__":
    array_test()
    linked_list_test()

    