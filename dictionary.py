# Dictionary => built-in data structure used to store data in the form of key-value pairs.
"""Key: A unique identifier used to access a value. Keys must be immutable types
 		(e.g., strings, numbers, or tuples).
   Value: The data or object associated with a key. Values can be of any data type.
"""

# Declaring a dictionary
d={1:"one",2:"two",3:"three",4:6,5:120.53}

# Accessing data
# Using keys
print(d[1])
print(d[2])
print(d[3])
# returns error if argument isn't in the range

# Using get() function
print(d.get(3))
# returns None if argument isn't in the range

#----------------------------------------------------------------------------------------------------------------------#

D={1:"ONE",4:"T",5:100,10:120.67,12:[1,2,3],"VIT":1}
print(D)
print(D[1])
print(D["VIT"])
print(D[10])

# Updating a dictionary
D[1]="One"
print(D)
D["VIT"]="BHOPAL"
print(D)

# Length of dictionary
print(len(D))

# Dictionary methods
print(any(D))
print(all(D))

# Printing dictionary elements
print(D.keys())
print(D.values())
print(D.items())

# Update function
D1={1:"ONe",2:"Two",3:"Three",4:"Four",5:"Five",}
D2={6:"Six",7:"Seven",8:"Eight",9:"Nine"}
print(D1)
print(D2)
D1.update(D2)  #dictionary 1 is updated using dictionary 2
print(D1)
# existing keys get their updated values while new keys get added

