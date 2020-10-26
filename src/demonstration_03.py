"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt: str) -> int:
    # Your code here
    # check to make sure that 'txt' makes sense as an integer
    # the 'isnumeric' function checks if a string can be represented     
    # as a number
    #  if 'txt' is a valid number:
    if txt.isnumeric() is True:
        # take the string input and conver it to a integer
        # the 'int' function does this for us in Python
        # call the 'int' function, pass it the 'txt' input 
        converted_int = int(txt)
        # return the converted result
        return converted_int
    # what dp we dp of 'txt' is not valid number
    else:
        # we'll return an error indicating that 'txt' is not a valid number
        # use string interpolation to print out the actual value of 'txt'
        # use f-strings in Python
        return f"'{txt}' is not a valid number"

    # return int(txt)
    return converted_int or f"'{txt}' is not a valid number"

print(string_int("1000"))
print(string_int("hi"))
