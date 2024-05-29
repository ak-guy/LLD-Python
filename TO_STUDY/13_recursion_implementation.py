'''
question : how does recursion works

answer : for that to explain we need to understand what happens when we call a funtion.


take example, we are creating a function multiply and then calling it

def multiply(a, b):
    product = a * b
    return product

result = multiply(4, 5)
print(result)


Step 1: Define multiply function.
Step 2: Call multiply(4, 5).
Step 3: Create a new stack frame for multiply with local variables and parameters.
Step 4: Pass arguments 4 and 5 to a and b.
Step 5: Execute the function body:
Compute product = a * b → product = 4 * 5 → product = 20.
Step 6: Return product, which is 20.
Step 7: Assign 20 to result and print it.
'''