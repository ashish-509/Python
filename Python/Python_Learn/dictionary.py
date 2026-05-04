
# A dictionary is a built-in data type that represents a collection of key-value pairs. Dictionaries are enclosed in curly braces `{}`.

# keys are immutable and unique whereas values can be immutable, mutable and duplicates in dictionaries.

dict_name = {} #Creates an empty dictionary 
person = { "name": "John", "age": 30, "city": "New York"}
print(person["name"])


# items() retrieves all key-value pairs as tuples and converts them into a list of tuples. Each tuple consists of a key and its corresponding value.

info = list(person.items())
print(info)






# A set is an unordered collection of unique elements. Sets are enclosed in curly braces `{}`. They are useful for storing distinct values and performing set operations.

empty_set = set() #Creating an Empty Set 
fruits = {"apple", "banana", "orange"}

