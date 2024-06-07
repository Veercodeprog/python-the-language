# print function (most used)
# input function : output is always string ,we have to typecast it to other
# data types if needed.
# type function : to check the data type of a variable
# int function : to convert string to integer
# abs function : to get the absolute value of a number
# pow function : to get the power of a number
# min : used with iterables(lists, tuples, sets, etc) to get the minimum
# value in it.
# also can be used with strings.

input("Enter your name: ")
power = pow(2, 3)
min([1, 2, 3, 4, 5])
min("hello")
round(3.14)
divmod(9, 2)  # returns a tuple with quotient and remainder
bin(10)  # returns binary representation of a number
oct(10)  # returns octal representation of a number
hex(10)  # returns hexadecimal representation of a number
id(10)  # returns the memory address of a variable
ord('a')  # returns the ASCII value of a character
len("hello")  # returns the length of a strings
sum([1, 2, 3, 4, 5])  # returns the sum of elements in a lists
help(print)  # returns the documentation of a function
