###
# Name: Jett Gazeley
# Student Number: 20216732
# 1. Binary Search or Linear Search? 50 points
###


import Q1_1
import random
from timeit import default_timer as timer


def search_test(list_test):
    ''' This function will run the tests for the 3 different S Values'''

    # K Values starting from 10 up to 500
    for i in range(10, 500, 10):
        k_list = list(range(i+1))

        # test for algorithm a
        start = timer()

        for j in range(len(k_list)):
            Q1_1.algorithm_a(list_test, k_list[j])

        end = timer()
        time_algorithm_a = (end - start)

        # test for algorithm b
        # Sort the lists for each n value
        start = timer()

        #Sort the list for the binary search
        sorting = Q1_1.mergesort(list_test)

        for k in range(len(k_list)):
            Q1_1.algorithm_b(sorting, k_list[k])

        end = timer()
        time_algorithm_b = (end - start)

        #Return length of k list if algorithm b beats algorithm a
        if time_algorithm_a > time_algorithm_b:
            return i


if __name__ == "__main__":

    # create lists for each n size
    list_1000 = []
    list_5000 = []
    list_10000 = []

    # S lists
    #Create a random array of integers for each "n" value
    for i in range(0, 1000):
        odd_rand_num1000 = random.randrange(0, 1000, 2)
        list_1000.append(odd_rand_num1000)

    for i in range(0, 1000):
        odd_rand_num5000 = random.randrange(0, 5000, 2)
        list_5000.append(odd_rand_num5000)

    for i in range(0, 1000):
        odd_rand_num10000 = random.randrange(0, 10000, 2)
        list_10000.append(odd_rand_num10000)


    #Output results from test
    print("For n = 1000, the smallest value of k where Algorithm B is faster is about:",
          search_test(list_1000))
    print("For n = 5000, the smallest value of k where Algorithm B is faster is about:",
          search_test(list_5000))
    print("For n = 10000, the smallest value of k where Algorithm B is faster is about:",
          search_test(list_10000))
