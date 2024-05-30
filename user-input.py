first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
print(first_number )
print(second_number)
print(first_number + second_number)

#important property of input function is that it always returns a string.so we need to convert it to integer or float before performing any arithmetic operation and it is called typecasting or type conversion.
#typeconversion are of two types:
#implicit type conversion (done by python interpreter)
#explicit type conversion (done by the programmer)
#explicit type conversion is done using the following functions:
#int() - converts to integer
#float() - converts to float
#str() - converts to string
#complex() - converts to complex
#bool() - converts to boolean
#list() - converts to list
#tuple() - converts to tuple
#set() - converts to set
#dict() - converts to dictionary
#chr() - converts to character
#ord() - converts to integer
#bin() - converts to binary
#hex() - converts to hexadecimal
#oct() - converts to octal
#eval() - evaluates the expression
#frozenset() - converts to frozenset
#bytes() - converts to bytes
#bytearray() - converts to bytearray
#memoryview() - converts to memoryview

result = int(first_number) + int(second_number)
print(result)