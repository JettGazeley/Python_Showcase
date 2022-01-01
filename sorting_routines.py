#Jett Gazeley
#2020-04-28
#Sorting Routines

#import random library
import random

###
def ascending_selection_sort(data):
  for i in range (0,len(data)-1):
    smallest = i
    #see if there is a smaller number further in the array
    for index in range (i+1,len(data)):
      if data[index] < data[smallest]:
        #swap values - note in many languages a swap function would need to be built
        #but python allows the exchange of data in the following method.
        data[index], data[smallest] = data[smallest],data[index]
###
def descending_selection_sort(data):
  for i in range (0,len(data)-1):
    smallest = i
    #see if there is a smaller number further in the array
    for index in range (i+1,len(data)):
      if data[index] > data[smallest]:
        #swap values - note in many languages a swap function would need to be built
        #but python allows the exchange of data in the following method.
        data[index], data[smallest] = data[smallest],data[index]
###
def ascending_bubble_sort(nums):
  """
  This function will sort the list of numbers using bubble
  sorting. It will compare each value to the next value in
  the list; if the first is value larger, the function will
  swap their positions.
  """
  #  loop to control number of passes
  for x in range(len(nums)):
    #  loop to control number of comparisons for length of list-1
    for i in range(0,len(nums)-1):
      #  compare side-by-side elements and swap them if
      #  first element is greater than second element
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i] #Note python allows a swap to occur in this fashion.
  return nums
###
def descending_bubble_sort(nums):
  """
  This function will sort the list of numbers using bubble
  sorting. It will compare each value to the next value in
  the list; if the first is value larger, the function will
  swap their positions.
  """
  #  loop to control number of passes
  for x in range(len(nums)):
    #  loop to control number of comparisons for length of list-1
    for i in range(0,len(nums)-1):
      #  compare side-by-side elements and swap them if
      #  first element is greater than second element
      if nums[i] < nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i] #Note python allows a swap to occur in this fashion.
  return nums
###
def ascending_insertion_sort(data):
  for i in range (1, len(data)): 
    insert = data[i]
    move_item = i

    while move_item > 0 and data[move_item - 1] > insert:
      data[move_item] = data[move_item - 1]
      move_item -= 1
    
    data[move_item] = insert
###
def descending_insertion_sort(data):
  for i in range (1, len(data)): 
    insert = data[i]
    move_item = i

    while move_item < 0 and data[move_item - 1] < insert:
      data[move_item] = data[move_item - 1]
      move_item -= 1
    
    data[move_item] = insert
###
def ascending_quick_sort(data, low, high):
  if low < high:
    split_point = ascending_partition(data, low, high)
    ascending_quick_sort(data, low, split_point - 1)
    ascending_quick_sort(data, split_point + 1, high)
    
def ascending_partition(data2, first, last): 
  pivot_value = data2[first] #pivot
  left_mark = first + 1 #index of smaller element
  right_mark = last 
  done = False
  while not done:
    while left_mark <= right_mark and data2[left_mark] <= pivot_value:
      left_mark = left_mark + 1

    while data2[right_mark] >= pivot_value and right_mark >= left_mark:
      right_mark = right_mark - 1

    if right_mark < left_mark:
      done = True
    else:
      data2[left_mark], data2[right_mark] = data2[right_mark],data2[left_mark]

  data2[first],data2[right_mark] = data2[right_mark], data2[first]
  
  return right_mark
###
def descending_quick_sort(data, low, high):
  if low > high:
    split_point = descending_partition(data, low, high)
    descending_quick_sort(data, low, split_point - 1)
    descending_quick_sort(data, split_point + 1, high)
    
def descending_partition(data2, first, last): 
  pivot_value = data2[first] #pivot
  left_mark = first + 1 #index of smaller element
  right_mark = last 
  done = False
  while not done:
    while left_mark <= right_mark and data2[left_mark] <= pivot_value:
      left_mark = left_mark + 1

    while data2[right_mark] >= pivot_value and right_mark >= left_mark:
      right_mark = right_mark - 1

    if right_mark > left_mark:
      done = True
    else:
      data2[left_mark], data2[right_mark] = data2[right_mark],data2[left_mark]

  data2[first],data2[right_mark] = data2[right_mark], data2[first]
  
  return right_mark
###

#Begin Mainline
num_select = int(input("How many numbers do you want to generate? "))
nums = []

for i in range (0,num_select):
  nums.append(random.randint(0,1000)) 

sort_select = int(input("What type of sort do you wish to perfom?\n1 - Selction Sort\n2 - Bubble Sort\n3 - Insertion Sort\n4 - Quick Sort\n"))

order_select = int(input("What order do you want the numbers sorted in?\n1 - Ascending\n2 - Descending\n"))



if sort_select == 1 and order_select == 1:
#print out unsorted list
  for count in range (0,len(nums)):
    print(nums[count] , end = " ")
      
  print("\n---------------------------------")
  ascending_selection_sort(nums)

  #print out sorted list
  print("After sorting using the Selection Sort, the array is:")
  for count in range (0,len(nums)):
    print(nums[count] , end = " ")


elif sort_select == 1 and order_select == 2:
   #print out unsorted list
  for count in range (0,len(nums)):
    print(nums[count] , end = " ")   
  print("\n---------------------------------")
  descending_selection_sort(nums)
  #print out sorted list
  print("After sorting using the Selection Sort, the array is:")
  for count in range (0,len(nums)):
    print(nums[count] , end = " ")


elif sort_select == 2 and order_select == 1:
    #print out unsorted list
  print ("\nUnsorted list:")
  for count in nums:
      print (count, " ", end="")
  nums = ascending_bubble_sort(nums)
  #print out sorted list
  print ("\n\nAfter sorting using the Bubble Sort, the array is: ")
  for count in nums:
      print(count, " ", end="")
  print()


elif sort_select == 2 and order_select == 2:
    #print out unsorted list
  print ("\nUnsorted list:")
  for count in nums:
      print (count, " ", end="")
  nums = descending_bubble_sort(nums)
  #print out sorted list
  print ("\n\nAfter sorting using the Bubble Sort, the array is: ")
  for count in nums:
      print(count, " ", end="")
  print()


elif sort_select == 3 and order_select == 1:
    #print out unsorted list
  for count in range (0, len(nums)):
    print(nums[count] , end= " ")

  print("\n---------------------------------")
  ascending_insertion_sort(nums)

  #print out sorted list
  print("After sorting using the Insertion Sort, the array is:")
  for count in range (0, len(nums)):
    print(nums[count] , end= " ")


elif sort_select == 3 and order_select == 2:
    #print out unsorted list
  for count in range (0, len(nums)):
    print(nums[count] , end= " ")

  print("\n---------------------------------")
  descending_insertion_sort(nums)

  #print out sorted list
  print("After sorting using the Insertion Sort, the array is:")
  for count in range (0, len(nums)):
    print(nums[count] , end= " ")


elif sort_select == 4 and order_select == 1:
    #print out unsorted list
  for count in range (0,len(nums)): 
    print(nums[count] , end = " ")
      
  print("\n---------------------------------")
  ascending_quick_sort(nums, 0, len(nums) - 1)

  #print out sorted list
  print("After sorting using the Quick Sort, the array is:")
  for count in range (0,len(nums)): 
    print(nums[count] , end = " ")


elif sort_select == 4 and order_select == 2:
   #print out unsorted list
  for count in range (0,len(nums)): 
    print(nums[count] , end = " ")
      
  print("\n---------------------------------")
  descending_quick_sort(nums, 0, len(nums) - 1)

  #print out sorted list
  print("After sorting using the Quick Sort, the array is:")
  for count in range (0,len(nums)): 
    print(nums[count] , end = " ")
