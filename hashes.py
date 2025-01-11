#hashes lesgooo 

#a hash table hash values have its own seperate algorithm, presumably using premade algs sintead of creating your own . 
#typically act like key value pairs, mainly used for locating stuff.  

def hash(value): #this is a function that will help me in making a hash value + used for finding the hash value of a certain thing. 
    s=0
    for i in value:
        s+=ord(i)
    return s//10 

l = ['A','B','C','D','E'] #can be a key-value pair as well, depends on your usecase. 


#this calculates the hash value, and checks if its there in that position. 
def contains(value):
    n = hash(value)
    return l[n] == value

def add(value):
    n = hash(value)
    i = l[n]
    if value != i:
        l.append(value)



