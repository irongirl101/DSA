#Lowest Value in an array 

l = [7,12,9,11,3]


#SORTING ALGS 

#time complexity = O(n)
def lowest_value(l):
    min = l[0]
    for i in l:
        if i<min:
            min = i 
    return min 

#time complexity = o(n^2)
#look at first 2 values, compare, if needed, swap. 
#go to next 2, etc etc 
#first loop is to do bubble sort that many times 
def bubble_sort(l): 
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l 

#time complexity = o(n^2)
#find lowest number, pop and insert at index 0
#first loop is the number of times this is needed for 
def selection_sort(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i+1,len(l)):
            if l[j]< l[min] :
                min = j
        value = l.pop(min)
        l.insert(i,value)
    return l 

#time complexity = o(n^2)
#outer loop => chooses each value 
#inner loop => goes through sorted part of the array to see where to insert that value ->
def insert_sort(l):
    for i in range(len(l)):
        insert = i 
        value = l.pop(i)
        for j in range(len(l),-1,-1):
            if l[j]> value:
                insert = j 
        l.insert(insert,value)
    return l 


#QUICKSORTTTTT
        #time complexity worst case is O(n^2)
        #notes about quick sort -> uses recursion, has a pivot value 
        #will come back to this 
        #quick sort is almost like binary search, excepting sorting 
'''Logic behind quicksort: an array of elements, gets split in the middle, and continues to get split until the lowest number is reached 
    ok so, 
    a pivot element is chosen, typically the last element
    and is divided into two halves acrosss the pivot element 


'''

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

#sorts the array by counting the number of times a value occurs in the array 
#only works for non negative integer values 
#the max number of same value must be less than the total number of values in the array
#time complexity O(n+k)
'''
Logic which i think is correct 
Find the max number in the list 
create a list of length using the max number , where each element for the time being is 0, and remove that value
now, going through the og list, increase the value in the counting list at that number's position 
this is countinued till the og array = [] 
then with the number, and the index, each number is added back to the array 
'''
def counting_sort(l): 
        if not l: 
            return []
        count_array =[] 
        #max value 
        max = l[0] 
        for i in range(len(l)):  
            if l[i] > max: 
                max = l[i]

        #creating countine array of that length 
        for i in range(max+1): 
            count_array.append(0)
        
        #counting how many times an element occurs anf decreasing the length of the list simulataneously 
        for i in range(len(l) - 1, -1, -1):  # Reverse iteration
            pos = l[i]
            count_array[pos] += 1
            l.pop(i)
        
        #adding back into array 
        for i in range(len(count_array)): 
            for j in range(count_array[i]): 
                l.append(i)
                

        return l

#Radix sort must be stable in order for it to sort properly 
#works for non negative integers only 
#radix sort can be implemented with other sorts, as long as its stable (i.e. like bubble sort or counting sort); 
#time complexity O(nk)
'''RADIX SORT MY LOGIC
create a 2D array [[],[],[]...], 9 sub arrays (indexing 0 to 9)

get the last digit of each number (i.e will be the position) i.e. mod by 10->gets the last digit; and divide by 10
keep those numbers at its respective position in the radix array, while removing from the original array 
then iteratively add them back into the og array,while removing from the radix 

'''
def radix_sort(l):
    radix = [[],[],[],[],[],[],[],[],[],[]]#array into which each number gets added to 
    max = arr[0]
    for i in l: 
        if max<i: 
            max = i
    exp = 1 #the 10th at which the number divides in order to get the modulus 
    while max//exp>0:
        while len(l)>0: 
            val = l.pop() #remvoing the value 
            ind = (val//exp)%10 #gets the index at which should be added in radix 
            radix[ind].append(val) 

        for i in radix: #going through radix 
            while len(i)>0: 
                val = i.pop() #popping out each value and then putting it back into og arr 
                l.append(val)
        exp*=10 
    return l

def radixSortWithBubbleSort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        radixArray = [[],[],[],[],[],[],[],[],[],[]]
        
        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
        
        for bucket in radixArray:#making bubble sort do the stabilization for you 
            bubble_sort(bucket)
        
        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        
        exp *= 10

def merge_sort(l):
    
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)
#print(bubble_sort([4,6,2,1,5,8]))

#print(counting_sort([2, 3, 0, 2, 3, 2]))








