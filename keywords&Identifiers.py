# a keyword in programming language is a reserved word that has a special meaning to the compiler/interpreter.
# python has 33 keywords:
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield
#we cant use these keywords as variable names,function names or any other identifier names.

import keyword
print(keyword.kwlist)

# a python identifier is a name used to identify a variable,function,class,module or other object.
#rules for writing identifiers:
#can only start with a letter or an underscore.
#1. identifiers can be a combination of letters in lowercase(a-z) or uppercase(A-Z),digits(0-9) or an underscore(_).
#2. an identifier cannot start with a digit.
#3. keywords cannot be used as identifiers.
#4. special symbols like !,@,#,$,% are not allowed in identifiers.
#5. an identifier can be of any length.
#6. identifiers are case-sensitive.
#7. an identifier can start with an underscore(_).
#8. an identifier starting with an underscore(_) has a special meaning.
#9. an identifier starting with two underscores(__) indicates a strongly private identifier.
#10. an identifier starting and ending with two underscores(__) is a language-defined special name.