# Stacks in python 
stack= ['a','b','c','d']
print(stack)

stack.append('g')
print(stack)

stack.pop(1)
print(stack)


top_element=stack[-1]
print(top_element)
#search for an element in the stack
stack = [1, 2, 3, 4, 5]
number = 4
found = False

for element in stack:
    if element == number:
        found = True
        break

if found:
    print("Number is found")
else:
    print("Number not found")

#delete an element from the stack
stack = [1, 2, 3, 4, 5]
number_to_delete = 3
if number_to_delete in stack:
    stack.remove(number_to_delete)
    print(f"{number_to_delete} has been deleted from the stack.")
else:
    print(f"{number_to_delete} not found in the stack.")
    











































