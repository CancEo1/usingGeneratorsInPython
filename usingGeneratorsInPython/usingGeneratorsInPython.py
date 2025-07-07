# Purpose: demonstrate the use of generators in Python.
# a generator is a special type of iterator that allows you to iterate over a sequence of values
# without storing them in memory all at once.

# you can define a generator using the def keyword, but instead use a yield statement
# 
def my_generator(n):
    print("@@@@@@ Example 1 @@@@@@")
    # initialize counter
    value = 0
    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value
        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(6):
    # print each value produced by the generator
    print(value)

# create the generator object
print("@@@@@@ Example 2 @@@@@@")
squares_geneerator = (i * i for i in range(5))

# iterate over the generator object produced by squares_geneerator
for i in squares_geneerator:
    print(i)

# this generator will help with the assignment where we have to use a program to find the fibonaccir sequence
def fibonacci_numbers(nums):
    print("@@@@@@ Example 3 @@@@@@")
    # initialize the first two fibonacci numbers
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
# using the generator to print the first 10 fibonacci numbers
def square(nums):
    for num in nums:
        yield num**2
print(sum(square(fibonacci_numbers(10))))  # Output: 4895