# Learn more about Lists when we store integers inside a list
# on this stage , start thinking about a computer language is giving instructions to CPU to do something 
# Example: Python is asking CPU to store list in NumberList1 and NumberList2 , how Python asks through Python's compiler
Line = "==================="
NumberList1 = [4,6,8,10]
NumberList2 = [3,5,7,9]
print(Line)
print((NumberList1) + (NumberList2))   # here + is an operator according to Python rules, it concetnates 
print(Line)
print("Concatenate List1 & List2: " + str((NumberList1)) + str((NumberList2)))   # adding one type to 2nd type not allowed unless you make both same
print(Line)

# lets add a string variable and use it with list
Title1 = "This is list # 1"
Title2 = "This is list # 2"

#print(Title1 + " =" + NumberList1) # this will give error - why because Title1 one is String variable and NumberList1 is list of integer
print(Line)
print(Title1 + " =" + str(NumberList1))

# lets assign list to a variable and practice 
List1 = NumberList1
List2 = NumberList2

print(Line)
print("Print NumberList1 through List1 Variable & NumberList2 through Lis2 variable =")
print(List1 + List2)

# Lets try Maths with individual items with in same list or different lists
print(Line)
print("Addtion of item0 in list1 & item2 in list2 = ")
NumberList1[0] + NumberList2[2]   # You will not recieve an error or results after this-- why because you have not told Python to display it
# lets do above one this way
Result = NumberList1[0] + NumberList2[2]   
print(Result)