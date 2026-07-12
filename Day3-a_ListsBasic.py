# Learn about Lists in Python
""" 
Imagine you go shopping.
Instead of buying one item, you buy several.
Instead of creating four separate variables:

item1 = "Bread"
item2 = "Milk"
item3 = "Eggs"
item4 = "Apples"
Python lets you store them in one variable called a list
"""

# Create a Shopping list and print 
ShoppingList = ['Fruits',"Vegitables","Kmart"]   # to check single and double qoutes do not make difference
#print("List of all items in the list = " + ShoppingList[])
# Print an items at specific location which is called an index 
print(ShoppingList[0])   # this means at indix 0  - rememebr index starts from 0 and always use []
print("Print item at Index 0 = " + ShoppingList[0]) # You can not add print of senetence with a List 
#Line16 Erro: To achieve above which is not possible adding a print txt to a List - Try below print separately 

print("This is my Shopping list:")
print(ShoppingList)

# Another solution - If you really want the whole list in one sentence:
# Convert the List to Text
print("My shopping list is : " + str(ShoppingList))