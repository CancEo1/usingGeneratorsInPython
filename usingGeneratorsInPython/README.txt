A simple Python program that shows how to use generators.

In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
Generators are defined using the `yield` statement.
When the function is called, it does not execute the body immediately. Instead, it returns a generator object that can be iterated over.

We can also create a generator object from the generator function by calling the function like we would any other functions.
When we iterate over the generator object, the function body is executed until it hits a `yield` statement, which returns a value and pauses the function's execution.

Similar to a list comprehension, but instead of creating a list, it creates a generator object that can be iterated over to produce values one at a time.

The generator expression is a value that will be returned for each item in the iterable
(expression for item in iterable)
1. Easy to Implement
	Can be implemented in a clear and concise way as compared to their iterator class counterpart.
2. Memory Efficient
	Generators do not store their contents in memory, which makes them more memory efficient than lists.
3. Represent Infinite Stream
	excellent mediums to represent an infinite stream of data, cannot be stored in memory, and since they are lazy, they can be used to represent an infinite sequence of values.
4. Pipelining Generators
	Generators can be used to pipeline a series of operations, where the output of one generator is fed into the next generator. Example: Fibonacci Numbers

Source: Programiz "Python Generators"