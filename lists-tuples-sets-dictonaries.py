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
