'''
map() -> used to apply one operation to an iterable

eg - list(map(operation_to_be_operated_on_iterable, iterable))

l = [1,2,3,4,5]
new_l = list(map(str, l))
newer_l = list(map(lambda x:x+10, l))
print(new_l) # ['1', '2', '3', '4', '5']
print(newer_l) # [11, 12, 13, 14, 15]
'''

'''
filter() -> used when we need only some items from an iterable

eg - list(filter(operation_to_be_operated_on_iterable, iterable))

l = [1,2,3,4,5]
new_l = list(filter(lambda x : x % 2, l))
print(new_l) # [1, 3, 5]
'''

'''
reduce() -> we use this function to get a single output from an iterable like finding sum, product etc of an array

eg - reduce(operation_to_be_operated_on_iterable, iterable)


from functools import reduce
l = [1,2,3,4,5]
arr_sum = reduce(lambda x, y : x+y, l)
print(arr_sum)


def dummy_lambda(x,y):
    return x+y

new_arr_sum = reduce(dummy_lambda, l)
print(new_arr_sum)
'''

'''
accumulate() -> similar to reduce but return an iterator not a single value

eg - accumulate(iterable, operation_to_be_operated_on_iterable)

from itertools import accumulate

l = [1,2,3,4,5]
new_iterator = accumulate(l, lambda x, y: x * y)
print(new_iterator.__next__())
print(new_iterator.__next__())
print(new_iterator.__next__())
print(new_iterator.__next__())
print(new_iterator.__next__())
'''

'''
custom sort -> we apply lambda function in key paramter to acheive custom sort

l.sort(key=some_function)

l = [1,2,3,4,5,6,7,8,9,10]
l.sort(key=lambda x: -x)
print(l)
'''

# sort odd numbers in desc order and even numbers in asc order
from functools import cmp_to_key

def sort_odd_desc_even_asc(a, b):
    # both are even then pick smaller one
    if a % 2 == 0 and b % 2 == 0 and a<b:
        return -1
    
    # both are odd then pick larger one
    if a % 2 and b % 2 and a<b:
        return 1
    
    # if a is odd and b is even then we say a is smaller
    if a % 2:
        return -1
    
    return 1

def sort_only_even_numbers(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return -1
    
    if a % 2 == 0:
        return -1
    if b % 2 == 0:
        return -1
    
    return 0

l = [1,2,3,4,5,6,7,8,9,10]
# l.sort(key=cmp_to_key(sort_odd_desc_even_asc))
# print(l)
l.sort(key=cmp_to_key(sort_only_even_numbers))
print(l)

