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

        #notes about quick sort -> uses recursion, has a pivot value 
        #will come back to this 
        #quick sort is almost like binary search, excepting sorting 
'''Logic behind quicksort: an array of elements, gets split in the middle, and continues to get split until the lowest number is reached 
    ok so, 


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
#the max number of same value must be less than the totall number of values in the array

'''
Logic which i think is correct 
Find the max number in the list 
create a list of length using the max number , where each element for the tune being is 0, and remove that value
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


arr = [4, 6, 2, 1, 5, 8]
quicksort(arr)
print(arr)
#print(bubble_sort([4,6,2,1,5,8]))

#print(counting_sort([2, 3, 0, 2, 3, 2]))








