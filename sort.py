#text_file = open('file2.txt','w')
#
##initialize an empty list
#word_list= []
#
##iterate 4 times
#for i in range (1, 5):
#    print("Please enter data: ")
#    line = input() #take input
#    word_list.append(line) #append to the list
#
#
#text_file.writelines(word_list) #write 4 words to the file#
#text_file.close() #don’t forget to close the file


#ques A,1
"""
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [1,7,4,2]
bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" % arr[i])
"""
#ques 2
"""
def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [1,7,2,4]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])
"""
#que
"""
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['a','s','h','u','t','o','s','h']
x = 'z'
print("element found at index "+str(linearsearch(arr,x)))
"""
#Ques
"""
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
# Test array
arr = [7, 8, 11, 15, 2]

x = 2
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print("It is present at index", (result))
else:
    print("It is not present in array")
"""
#ques quick sort
"""
def partition(arr, low, high):
    i = (low - 1)
    #print(i)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            #print(i)
            arr[i], arr[j] = arr[j], arr[i]
    #print(i+1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #print(i+1)
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [43,46,50,1,2]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:",arr)
"""
#interpolation search
"""
def interpolationSearch(arr, n, x):
    low = 0
    high = (n - 1)
    while low <= high and x >= arr[low] and x <= arr[high]:
        mid = low + int(
            ((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def test(x):
    arr = [2,10, 12, 13, 16, 18, 19, 20]
    n = len(arr)
    index = interpolationSearch(arr, n, x)
    if index != -1:
        print( "The element", x, "is at the index", index)
    else:
        print( "Element", x, "not found!")
test(2)
"""

"""
def TowerOfHanoi(n, source, destination, auxilliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxilliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxilliary, destination, source)
n = 3
TowerOfHanoi(n, 'A', 'B', 'C')
"""