#understanding time complexities and their memory allocation 

#mainly searching algs and sorting algs 
l = [1,2,5,4,3,6,9,7]

#BUBBLE SORTS 
'''
Bubble Sort 
Time Complexity : o(n^2)
How?
n-1 * n/2 
n^2/ 2 - n/2 
n/2 is much smaller than n^2/2, so can be omitted 
n^2/2, 1/2 is omitted 
n^2 

n-1 is the worst case scenario for bubble sort 
n/2 is the average no. of ops 

best case will be o(n)
'''

def bubblesort(l):
    for i in range(len(l)-1): 
        for j in range(len(l)-1-i): 
            if l[j]> l[j+1]: 
                l[j],l[j+1] = l[j+1],l[j]
    return l  

#SELECTION SORT 
'''
it goes through the array (n-1) times 
average = n/2 
no;. of swaps = n 
(n-1) * n/2 + n 
n^2-n/2 +2n/2 
n^2 (+n/2 -> negligible) 

o(n^2) 

Best and worst case is O(n^2) as it alwawys scans through the list, even if sorted
It is not a stable sort, because it can alter the relative order of the elements, due to it swapping non adjacent elements can distrupt it. 
'''
def selection_sort(l):
    for i in range(len(l)-1): 
        min_ind = i 
        for j in range(i+1, len(l)): 
            if l[j]< l[min_ind]: 
                min_ind = j 
        value = l.pop(min)
        l.insert(i,value)
    return l 

#INSERTION SORT 
'''
O(n^2) 
n*n = n^2 
'''
def insert_sort(l):
    for i in range(len(l)):
        insert = i 
        value = l.pop(i)
        for j in range(len(l),-1,-1):
            if l[j]> value:
                insert = j 
        l.insert(insert,value)
    return l 

#COUNTING SORT 
'''
Counting sort is O(n+k) ~ O(n) 
however not effective at all 

'''

#QUICK SORT  
'''
Worst case time complexity would be O(n/2 * n) = O(n^2)
i.e. recursion is called n times, and on average does n/2 comparisons on average. 
However, on the overall average, quick sort is the fastest of the lot 
Why? the array always dvides itself into 2 halves each time, which means that not many recursive calls are needed, and quick sort can finish it quicker than the worst time scenario 
so, a log 2(n) is a better complexity. 
Howver, each array cannot be divided into two perfect halves each time, the average can be set to O(nlog2n)

Why is it so fast? Due to the recursive nature->the array will always be split into 2 somewhat equal halves So the number of recursive calls do not double, even if the number of values double.

'''

#RADIX SORT 
'''
n+n = 2n (n values are moved to and from the array )

O(2nk) ~ O(nk)
n - no of digits, k- number of digits in the highest value 

Worst case scenario O(n^2), when n = k 
Best case scenario O(nlogn), the same as quick sort. (i.e. k grows with n, k = log n)

'''