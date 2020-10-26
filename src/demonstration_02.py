"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes: int) -> int:
    # Your code here
    # there are 60 seconds in a mintue
    # we need to take 'minutes' and mulitply by 60
    # in order to perform the conversion
    seconds = minutes * 60
    # return the conerted result
    return str(seconds)

    # return minutes * 60

print(convert(5))