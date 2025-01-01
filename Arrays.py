#Lowest Value in an array 

l = [7,12,9,11,3]

#time complexity = O(n)
def lowest_value(l):
    min = l[0]
    for i in l:
        if i<min:
            min = i 
    return min 

def bubble_sort(l): 
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l 





