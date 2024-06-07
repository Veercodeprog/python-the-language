# List vs array
# 1. List is a collection of items. It is ordered and changeable. Allows duplicate members.
# Array is a collection of items. It is ordered and changeable. Allows duplicate members.
# 2. Array are homogeneous collections of items, specifically of the same data type.whereas
# list can be heterogenous(can contain different data types ) as well.
# 3. Array stores data in a contiguous memory location. List stores references to the objects in memory
# data in a list is stored in a non-contiguous memory location.
# 4. Arrays are faster and more efficient than lists.
# 5. Lists are more flexible than arrays.

# lists are mutable

List = [1, 2, 3, 4, 5]
L = []  # empty list
L2 = ["hello", 4, 5.5, True]  # heterogenous list

# multi-dimensional list
# 2d list

L3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L4 = [1, 2, 3, [4, 5, 6], [7, 8, 9]]

# 3d list
L5 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [
    [10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# list function is used to convert any iterable to list

L6 = list("hello")
print(L6)
L7 = [1, 2, 3, [4, 5, 6]]

# to extract 4 from L7
print(L7[3][0])
print(L7[-1][0])

L8 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# to extract 7 from L8
print(L8[1][1][0])

# to append an element to the list
L9 = [1, 2, 3]
L9.append(4)  # [1, 2, 3, 4]
print(L9)

# to extend a list

L10 = [100, 200, 300, 400, 500, 'hello']
# [100, 200, 300, 400, 500, 'hello', 600, 700, 800, 900]
L10.extend([600, 700, 800, 900])
print(L10)

# [100, 200, 300, 400, 500, 'hello', [600, 700, 800, 900]]
L10.append([600, 700, 800, 900])

# [100, 200, 300, 400, 500, 'hello', 600, 700, 800, 900, 'g', 'o', 'a', 't']
L10.extend('goat')
print(L10)

# [100, 200, 'hello', 300, 400, 500, 'hello', 600, 700, 800, 900, 'g', 'o', 'a', 't']
L10.insert(2, 'hello')
# del is to delete the list or element from the list

# del L10 # deletes the list
# del L10[2] # deletes the element at index 2
# L10.remove(200) # removes the element 200 from the list

# List operations
L11 = [1, 2, 3, 4, 5]
L12 = [6, 7, 8, 9, 10]
L13 = L11 + L12
L14 = L11 * 3
for i in L11:
    print(i)

# functions
# len() - returns the length of the list
# max() - returns the maximum element in the list
# min() - returns the minimum element in the list
# sum() - returns the sum of the elements in the list
# sorted() - returns the sorted list
# reversed() - returns the reversed list
# sort() - sorts the list in ascending order
# reverse() - reverses the list

sample = "how are you"
print(sample.split())
L15 = sample.split()  # ['how', 'are', 'you']
L16 = " ".join(L15)  # how are you

# Tuples
# Tuples are immutable
# Tuples are faster than lists
# Tuples are used when the data cannot be changed

T1 = (1, 2, 3, 4, 5)
T2 = ("hello", 4, 5.5, True)
# single element tuple should have a comma at the end
T3 = (1,)  # type(T3) = tuple
T4 = (1)  # type(T4) = int

T5 = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')

# can not edit the tuple
# just like strings, tuples can be concatenated, repeated, sliced, and indexed
# but not modified
# deleting and accessing elements in a tuple is same as list
# functions are same as list

# Sets
# rules of sets:
# 1. sets  do not allow duplicate elements
# 2. sets are unordered i.e no indexing /slcing
# 3. sets dont allow mutable elements or data types
# 4. sets are mutable
# 5. sets are faster than lists
S1 = {1, 2, 3, 4, 5}  # type(S1) = set
S2 = {}  # empty dictionary not set
S3 = set()  # empty set
S4 = {"hello", 4, 5.5, True}  # heterogenous set

# sets dont allow mutable elements or data types
# i.e sets cant contain lists, dictionaries, or other sets
# but can contain tuples as they are immutable

S4 = {(1, 2), (3, 4), (5, 6)}  # set of tuples
# S5 = {[1, 2, 3], "Hello"}  # error because of list in set
# 3d and 2d sets are not possible

# sets allow add, remove, discard, pop, clear, update, union,
# intersection, difference, symmetric difference
# add - adds an element to the set
# remove - removes an element from the set
# discard - removes an element from the set
# pop - removes an element from the set
# del - deletes the set
# clear - clears the set
# update - adds multiple elements to the set
# union - returns the union of two sets
# intersection - returns the intersection of two sets
# difference - returns the difference of two sets i.e elements in set1 but not
# in set2
# symmetric difference - returns the symmetric difference of two sets
# issubset - returns true if the set is a subset of another set
# issuperset - returns true if the set is a superset of another set
# isdisjoint - returns true if the set has no common elements with another set

S1.add(6)  # {1, 2, 3, 4, 5, 6}
S1.remove(6)  # {1, 2, 3, 4, 5}
S1.discard(6)  # {1, 2, 3, 4, 5}
S1.pop()  # removes a random element from the set
# basically pop deleted the last element from the set based on the address

# +, *, len(), max(), min(), sum(), sorted(), reversed() are not possible in sets

# functions in sets
# len() - returns the length of the set
# max() - returns the maximum element in the set
# min() - returns the minimum element in the set
# sum() - returns the sum of the elements in the set
# sorted() - returns the sorted set
# reversed() - returns the reversed set


# Dictionaries: Dictionaries are used to store data values in key:value pairs
# dictionaries are mutable
# {'Name': 'Nitish', 'Gender': 'Male'}
# rules of dictionaries
# 1. dictionaries has no indexing
# 2. dictionaries is a mutable types
# 3. keys-> immutable, values-> they can be mutable
# 4. keys should be unique

# immutable -: List/sets/ dictionary
# mutable -: Strings/tuple/int/float/boolean/complex

D = {}  # empty dictionary
D1 = {'Name': 'Nitish', 'Gender': 'Male'}

# D2 = {[1, 2, 3]: "Nitish"} # error because list is mutable
D3 = {(1, 2, 3): "Nitish"}  # works because tuple is immutable
# 2d and 3d dictionaries are possible

# 2d dictionary
D4 = {'Name': {'First': 'Nitish', 'Last': 'Kumar'},
      "college": "IIT", "Branch": "CSE"}

# accessing elements in dictionary
# 1. using keys
# 2. using get() function
# 3. using items() function
# 4. using keys() function
# 5. using values() function

D4['Name']  # {'First': 'Nitish', 'Last': 'Kumar'}
D4.get('Name')  # {'First': 'Nitish', 'Last': 'Kumar'}
# dict_items([('Name', {'First': 'Nitish', 'Last': 'Kumar'}), ('college', 'IIT'), ('Branch', 'CSE')])
D4.items()
D4.keys()  # dict_keys(['Name', 'college', 'Branch'])
# dict_values([{'First': 'Nitish', 'Last': 'Kumar'}, 'IIT', 'CSE'])
D4.values()

# editing elements in dictionary
D4["Name"]["First"] = "deepak"

# add a new key value pair
# {'Name': {'First': 'deepak', 'Last': 'Kumar'}, 'college': 'IIT', 'Branch': 'CSE', 'Age': 22}
D4["Age"] = 22

# deleting elements in dictionary
# 1. del dictionary[key]: deletes the key value pair
# 2. pop: removes the key value pair
# 3. popitem: removes the last key value pair
# 4. clear: clears the dictionary
# 5. del dictionary: deletes the dictionary
print("IIT" in D4)  # False
print("First" in D4)  # False
D4.keys()  # dict_keys(['Name', 'college', 'Branch', 'Age'])
# dict_values([{'First': 'deepak', 'Last': 'Kumar'}, 'IIT', 'CSE', 22])
D4.values()
