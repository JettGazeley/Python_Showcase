# Returns index of x if it is present 
# in arr[], else return -1 
# Returns index of x in arr if present, else -1 
def binary_search (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)//2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1

#Begin Mainline
psalms_file = []
f = open('psalms.txt', 'r')
count = 0
for line in f:
  count+=1
  if count % 2 != 0: #use this if statement to only append the psalm numbers into the 2d list
    psalms_file.append(line.split())

# import chain 
from itertools import chain 

# converting 2d list into 1d 
# using chain.from_iterables 
psalms_file = list(chain.from_iterable(psalms_file)) 
  
# printing flatten_list 
#print ("final_result", str(psalms_file))

#convert the elements in the list into integers
for i in range(len(psalms_file)):
    psalms_file[i] = int(psalms_file[i])

#Ask for user input
psalm_num = int(input("What psalm number would you like to see? (1-99) "))

# Function call 
result = binary_search(psalms_file, 0, len(psalms_file)-1, psalm_num) 
 
if result != -1: 
  #print ("Element is present at index %d" % result) 
  
  with open("psalms.txt") as f:
    content = f.readlines()
  content = [x.strip() for x in content]

  #output back to the user
  print("\nPsalm",psalm_num,"\n")
  print(content[result*2 +1])

else: 
    print ("Element is not present in array")
