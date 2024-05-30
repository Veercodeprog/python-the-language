# literals in python:
# a literal is a data which is given in a variable or constant.
# literals can be of any data type.
#in python, there are five types of literals:
#1. string literals
#2. numeric literals
#3. boolean literals
#4. special literals
#5. literal collections

#string literals:
# a string literal is a sequence of characters surrounded by quotes.
# in python, we can use single quotes(''), double quotes("") or triple quotes(''') to define a string.
# triple quotes are used to define multi-line strings.
# example:
# 'hello'
# "hello"
# '''hello'''
# 'hello' is a string literal.	
# "hello" is a string literal.
# '''hello''' is a string literal.
# unicode literals is a string literal with a 'u' prefix.
# example:
# u"hello"
#raw string literals is a string literal with an 'r' prefix.
# example:/
# r"hello"

#numeric literals:
# a numeric literal is a numeric value that can be assigned to a variable.
# example:
# 10
# 10.5
# 10 is a numeric literal.
# 10.5 is a numeric literal.
#types of numeric literals:
#1. integer literals
#2. float literals
#3. complex literals
#4. binary literals
#5. octal literals
#6. hexadecimal literals
#7. scientific notation

a= 0b1010 #binary literal
b= 100 #decimal literal
c= 0o310 #octal literal
d= 0x12c #hexadecimal literal

#float literals:
float_1 = 10.5
float_2 = 1.5e2 #1.5 * 10^2
float_3 = 3.14E-2 #3.14 * 10^-2

#complex literals:
x = 3.14j
print(x, x.imag, x.real)

#boolean literals:
# a boolean literal can have any of the two values: True or False.

a = True + 4
b = False + 10
print("a:", a, "b:", b)

#special literals:
# python has one special literal: None.
# None is used to specify that the field has not been created and variable is declared but not assigned any value.
a= None
print(a)
