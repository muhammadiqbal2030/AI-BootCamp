# More about Lists but understanding of Indexing in Lists

Line = "=================="
fruit = "Banana"
print(fruit[-1])     # Negative Idex starts from most right and keep going 
print(Line)
print(fruit[-2])
print(Line)
print(fruit[-3])
print(Line)

print("New Prgram starts from here")
print(Line)
numbers = [10,20,30,40]
print(numbers[-1])

print("New Prgram starts from here")
print(Line)
name = "Iqbal"
print(name[0] + name[-1])

#print(name[0] * name[-1])   # this will give error - Why----Read and understand properly  ? 
print(Line)
""" Simple Rule - Whenever you see *, ask yourself: Is the thing on the right a number?
"A" * 5
Right side = number ✅
Works.

"A" * "B"
Right side = string ❌
Error.

[1, 2] * 4
Right side = number ✅
Works.

[1, 2] * [3]
Right side = list ❌
Error.
"""

print([1, 2] * 2)

print(Line)
name1 = "Python"
print(name1[len(name1)-1])
# Explain above: 
"""
First, Python calculates: len(name)

The string is: Python

How many letters?
P y t h o n
6 letters
So:
len(name)
becomes: 6
Step 2
Now Python substitutes that value.
The code becomes: name[6 - 1]

Notice something very important.
Python does not do: name[6]
first.
It follows the expression exactly as written.
Step 3:
Python calculates:
6 - 1
which equals: 5
Now the code becomes: name[5]
Step 4:
Index the string.
Character : P  y  t  h  o  n
Index     : 0  1  2  3  4  5
Index 5 is "n"
So the output is: n
This is the key difference
You wrote:
len(name) is 6 which means name[6] then -1
That's not how Python reads it.
Python reads:
name[len(name)-1]
like this:
name[(len(name)-1)]
The calculation inside the square brackets happens first.
Think of it like normal maths.
Example:
print(10 * (5-2))
Python does:
5-2 = 3
Then:
10 × 3 = 30
It doesn't do:
10 × 5 = 50
50 - 2 = 48
The brackets tell Python what to calculate first.
The square brackets [] for indexing work similarly: Python first evaluates the expression inside them to get the index.
"""