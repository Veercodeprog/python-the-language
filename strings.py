# accessing substrings from a string
# strings are immutable in python
c = "hello"
print(c[0])  # h
print(c[-1])  # e
d = "hello world"
print(d[1:4])  # ell
# deleting a character from a strings
# del d[1]  # TypeError: 'str' object doesn't support item deletion
del d

# string operations

# 1. concatenation or arithmetical addition

a = "hello" + "- " + "world"
print(a)  # hello- world

print("*" * 10)  # **********
print("hello" * 3)  # hellohellohello

# .2. relational operators

# using ==, !=, <, >, <=, >=

# 3. logical operators
# using and, or, not

# 4.membership operators
# using in, not in

# string functions
# 1. len(): returns the length of a strings
# 2. lower(): returns the strings in lower case :
# 3. upper(): returns the strings in upper case
# 4. title(): returns the strings in title case
# 5. capitalize(): returns the strings in capital case
# 6. min(): returns the minimum value in a strings
# 7. max(): returns the maximum value in a strings
# 8. count(): returns the number of occurences of a character in a strings
# 9. sorted(): returns the sorted version of a strings
# 10. split(): returns the list of words in a strings
# 11. join(): joins the strings with a given delimiter
# 12. replace(): replaces a character with another character
# 13. find(): returns the index of a character
# 14. index(): returns the index of a character
# 15. isdigit(): returns True if the strings is a digit
# 16. title(): returns the strings in title case
# 17. isalnum(): returns True if the strings is alphanumeric
x = "hello my name {} and i am {} years old"
print(x.format("john", 23))
print(x)  # hello my name {} and i am {} years old
y = "    this is a string"
print(y.strip())  # this is a string
