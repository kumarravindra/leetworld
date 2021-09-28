"""
A dictionary is a collection which is unordered, changeable and indexed
We can create a dictionary with dict() function as well
like myDict = dict()
print(myDict)
another way, myDict = {}
create dictionary with real values
myDict = {1: 'One', 2: 'two'}
another dict
englishToSpanish = {"one":"uno", "two":"dos", "three":"tres"}
to get the values we pass the keys
"""
englishToSpanish = {"one": "uno", "two": "dos", "three": "tres"}
print(englishToSpanish["two"])

"""
Dictionary in table : python dictionary are implemented using hash table 
hash table is a way of doing key-value lookups, you store the values in an array, and then use a hash function to find the index
of the array cell that corresponds to your key-value pair

englishToSpanish = {"one":"uno", "two":"dos", "three":"tres"}
one  --> hash() --> 1592767626893995073  --> index = 3, it will store this pair ("one": "uno") in index 3 on an array, 
there may be conflict or collision but if there is any, then conflicted value will be stored as linkedlist in same index 
Update dictionary
"""
myInfo = {"Name": "Ravin", "Age": 24}
myInfo["Age"] = 25
print(myInfo)
myInfo["Address"] = "123 Local Dr, GreatCity"
print(myInfo)

"""
How to traverse through a dictionary
there is one way by creating a method and loop through with it
"""
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
print(traverseDict(myInfo))

"""
Search element in dictionary, there are few ways to search an element in dict
we will try linear search, meaning we need to look at each and every element of dictionary and see if we find 
element which we are looking for
"""
def seachDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'value does not exist'
print(seachDict(myInfo, 25))

"""
Delete or Remove an element from a dictionary
we can use pop() method, or popitem() method ( this method pick any random pair and delete it.
another method is clear() method, it delete all pairs of dictionary
we can use del method to delete any pair such as del myInfo['age'], del can also delete entire dictionary
"""

"""
Dictionary Methods
"""
myDict = {"name": "ravi", "age": 25, "address": "san jose", "education", "master"}
