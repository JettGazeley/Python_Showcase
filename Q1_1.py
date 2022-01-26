###
# Name: Jett Gazeley
# Student Number: 20216732
# 1. Binary Search or Linear Search? 50 points
###


### Linear Search Algorithm###
def algorithm_a(S, x):
    ''' This function will linearly search in the array S for the value x. 
    If x is present then return its location, else return -1 '''
    for i in range(len(S)):
        if S[i] == x:
            return True
    return False


### Binary Search Algorithm ###
def algorithm_b(S, x):
    lo = 0
    hi = len(S) - 1
    mid = 0
    while lo <= hi:
        mid = (hi + lo) // 2

        #Element is present at the mid
        if S[mid] == x:
            return True

        #If x is smaller, ignore the left half
        elif S[mid] > x:
            hi = mid - 1

        #Else, ignore the right half
        else:
            lo = mid + 1
    return False


### The two functions below will be used for Merge Sort ###
def mergesort(a):
    ''' Continuously split the array in half until you are left with the individual items.
    Pairs of individual items are put together to make a sorted list of length 2.
    These lists are merged together as well, and so on until you have a sorted array.
    '''
    if len(a) == 1:
        return a

    else:

        #Find mid of array
        n = len(a)//2

        # Divide the array elements
        array_one = a[:n]
        array_two = a[n:]

        #Sort the two new arrays
        array_one = mergesort(array_one)
        array_two = mergesort(array_two)

        return merge(array_one, array_two)


def merge(a, b):
    ''' Used in correlation to the mergesort function above '''
    c = []
    #Copy the data of the arrays into two temp arrays
    while len(a) and len(b) != 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])

    #Checking if any elements remain after the merge
    while len(a) != 0:
        c.append(a[0])
        a.remove(a[0])

    while len(b) != 0:
        c.append(b[0])
        b.remove(b[0])

    return c
