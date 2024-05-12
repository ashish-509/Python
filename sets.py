# Unlike lists and tuples, they are unordered. This means sets do not record element position. Sets only have unique elements.
# We place the elements of sets inside the curly brackets.

album_list = ['Sushant KC', 'Pramod Kharel', 'Michael Jackson', 'Sushant KC', 'Atif Aslam']
album_set = set(album_list)
print(album_set)

# Adding element to the set
album_set.add("Ashmita Adhikari")
print(album_set)

# Removing element from set
album_set.remove('Ashmita Adhikari')
print(album_set)

# Finding element in set
if ('Sushant KC' in album_set):
    print('You are fan of Sushant KC.')
else:
    print('You are not fan of Sushant KC.')


recent_album_set = {'Sushant KC', 'Swopna Suman', 'Samir Shrestha', 'Ashmita Adhikari'}
favorite_album_set = {'Arijit Singh', 'Sushant KC', 'Pramod Kharel'}

# Intersection of 2 sets
intersection_set = recent_album_set & favorite_album_set
print(intersection_set)

# Union of 2 sets 
union_set = recent_album_set.union(favorite_album_set)
print(union_set)

# Finding whether a given set is a subset of another set or not.
print(favorite_album_set.issubset(union_set))   # True





