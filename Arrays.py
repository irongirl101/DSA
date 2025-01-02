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
print(selection_sort(l))


s






