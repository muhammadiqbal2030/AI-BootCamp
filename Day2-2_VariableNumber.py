A = 40
B = 'My name is Iqbal'
#C = 'i am' + A   # can not add two different variable in one variable
C = 'i am' 
#print(B + "," + C + A )

""" Explanation error on Line5:  String + String + String + Number
"My name is Iqbal" + "," + "i am" + 40
It gives an error similar to:

TypeError: can only concatenate str (not "int") to str
Solution: 
Convert the number to a string using str().
print(B + ", " + C + " " + str(A))
Here, str(A) converts the integer 40 into the text "40".
"""
print(B + ", " + C + " " + str(A))