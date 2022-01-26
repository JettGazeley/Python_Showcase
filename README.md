# Python_Showcase

## 1 Binary Search of Linear Search?
Files: Q1 1.py Q1 2.py
Q1 1.py:
This file contains the linear and binary search functions, as well as the associated merge sort function for the binary search.
No code is run from this file, as all the necessary functions are imported into
Q1 2.py
Q1 2.py:
This file runs the required tests for Algorithm A B.
To run the code for Question 1, simply type ”python3 Q1 2.py” inside of the zip
folder directory. This command will run the tests for the 3 different ”n” values.
Experiment Description:
To determine the smallest value of k, I started by making 3 ”n” value lists for
each ”n” value respectively. I would then call the search test function for each
”n value list I had created. This approach would give me three different tests
to compare.
For the linear search, no sorting algorithm is required so we simply start the
timer and call Algorithm A until it finds each k value generated.
The binary search is a similar process except that you also need to sort the list.
To do this, I start my timer and call my merge sort algorithm. Once the list
is sorted, we can then search for each generated value of k and end the timer
when it is done.
If the binary search was slower compared to the linear search, we repeat the
process and add an additional k value to search for. Once the binary search is
quicker, we return the number of elements in the k value list.
After running this test multiple times, I can say that:
For n = 1000, the smallest value of k where Algorithm B is faster is about: 100
For n = 5000, the smallest value of k where Algorithm B is faster is about: 80
For n = 10000, the smallest value of k where Algorithm B is faster is about: 70

## 2 Implementing Stack
Files: Q2.py
Similar to Q1 2.py, all you need to do is type ”python3 Q2.py” inside of the
zip folder directory. All of the tests for the array based list and linked list are
contained in that file. For the linked list tests, I was only able to test the push
and pop functions as these were the only ones I could get to function properly.

## 3 Implement a CircularQueue
Files: Q3.py
Just like the other files, just type ”python3 Q3.py” inside of the zip folder
directory. The tests for each of the functions takes place in that one document
so you’ll be good to go. Documentation for steps in the function are shown in
the Q3.py file.


## sorting_routines.py
The goal of this activity was to showcase different methods of sorting algorithms in Python

## psalms.py
The goal of this activity was to showcase different methods of searching algorithms in Python to get the selected Psalm from the attached file "psalms.txt"
