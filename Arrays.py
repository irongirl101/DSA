#Lowest Value in an array 

l = [7,12,9,11,3]

#time complexity = O(n)
def lowest_value(l):
    min = l[0]
    for i in l:
        if i<min:
            min = i 
    return min 

#time complexity = o(n^2)
def bubble_sort(l): 
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l 

#time complexity = o(n^2)
def selection_sort(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i+1,len(l)):
            if l[j]< l[min] :
                min = j
        value = l.pop(min)
        l.insert(i,value)
    return l 
print(selection_sort(l))





