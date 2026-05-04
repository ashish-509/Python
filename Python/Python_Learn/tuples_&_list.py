
# Tuples are immutable.
# Tuples are written inside ()

tuple1 = ("Ashish", "11", "79.5")

print(tuple1)
print(tuple1[0])
print(tuple1[-1])

# tuple1[-2] = "xi"  # It gives error as : 'tuple' object does not support item assignment
print(tuple1[-2])

# sorting in tuple
tuple2 = (1,5,3,6,2,0)
tuple3 = sorted(tuple2)
print(tuple3)




# A list is a built-in data type that represents an ordered and mutable collection of elements. Lists are enclosed in square brackets [] and elements are separated by commas.

list1 = ["Ak", "12", "79"]

print(list1)
print(list1[0])
print(list1[-1])

list1[-2] = "xii"
print(list1[-2])



# slicing

print (list1[1:3])

# concatenating other iotems to list
list1 = list1 + ["Nepali, Lalitpur"]
print(list1) 

# or concatenation can also be accomplished as : 
list1.extend(["Mahalaxmi", "Engineering"])
print(list1)

# or as : 
# list1 = list1.append(["yes", "90"])
# print(list1)

list1.append(["yes", "90"])
print(list1)


# help (list1)  # to get more operations that can be performed on list


# inserting an element 
my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 6) # inserts element 6 at 2nd index. Syntax : list_name.insert(index, element) 
print(my_list)

