"""
Lambda function : Lambda functions in Python provide a concise way to create anonymous 
                  functions for simple tasks, often used in combination with higher-order functions.


Lambda functions are preferred over normal functions when:

The function is simple and can be written in a single line.
The function is used only temporarily or within another function.
You want to keep the code concise and avoid defining unnecessary named functions.
You need to pass a simple function as an argument to a higher-order function.
"""

add_ten = lambda x : x+10
add_two_numbers = lambda x, y: x + y

numbers = [1,2,3,4,5,6]
sq_numbers = list(map(lambda x:x**2, numbers))

ev_numbers = list(filter(lambda x : x % 2 == 0, numbers))



print(add_ten(5))
print(add_two_numbers(23,27))
print(sq_numbers)
print(ev_numbers)