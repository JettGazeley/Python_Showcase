###
# Name: Jett Gazeley
# Student Number: 20216732
# 3. Implement a CircularQueue: 35 points
###

class CircularQueue:
    def __init__(self, capacity):
        ''' initalize the queue, capacity, head, size and tail of the circular queue '''
        self.capacity = capacity
        self.total_queue = [None] * capacity 
        self.head = 0
        self.tail = -1
        self.size = 0

    def enqueue(self, element):
        ''' this function is used to enqueue new elements into the queue'''
        if self.size == self.capacity:
            print("Queue is full")

        else:
            self.tail = (self.tail + 1) % self.capacity
            self.total_queue[self.tail] = element
            self.size += 1

    def dequeue(self):
        ''' this function is used to remove an element from the queue '''
        if self.size == 0:
            print("Queue is empty")

        else:
            temp = self.total_queue[self.head]
            self.head = (self.head + 1) % self.capacity
        
        self.size -= 1
        return temp

    def print_queue(self):
        ''' This function returns the current state of the queue'''
        if self.size == 0:
            print("Queue is empty")

        else:
            element = self.head

            for i in range (self.size):
                print(self.total_queue[element])
                element = (element + 1) % self.capacity

if __name__ == "__main__":
    # Create an object called element and initialize the circular queue to have 5 spots
    element = CircularQueue(5)

    # Enqueue our test elements of 1 through 5
    element.enqueue(1)
    element.enqueue(2)
    element.enqueue(3)
    element.enqueue(4)
    element.enqueue(5)


    #Output the current queue
    print("Current queue")
    element.print_queue()

    element.dequeue()
    print("Element removed from queue")
    element.print_queue()

    element.enqueue(22)
    print("After adding 22 to the queue")
    element.print_queue()

    #Queue is full, and can't add element 35 into it
    element.enqueue(35)