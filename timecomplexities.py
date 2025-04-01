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


'''
Counting sort is O(n+k) ~ O(n) 
however not effective at all 

'''