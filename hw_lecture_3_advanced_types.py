#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(f' The id of int_a is {id(int_a)} \n', f'The id of str_b is {id(str_b)} \n',
      f'The id of set_c is {id(set_c)} \n', f'The id of lst_d is {id(lst_d)} \n',
      f'The id of dict_e is {id(dict_e)}')

#2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.extend([4, 5])
print(f' The id of set_c is {id(lst_d)}')

#3. Define the type of each object from step 1.
print(f'The object type of int_a is {type(int_a)}')
print(f'The object type of str_b is {type(str_b)}')
print(f'The object type of set_c is {type(set_c)}')
print(f'The object type of lst_d is {type(lst_d)}')
print(f'The object type of dict_e is {type(dict_e)}')

#4*. Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(2, 3))

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(5, 6))

# 7. By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches.".format(apples=20, peaches=30))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(25, 32))

# 9. With f-strings and variables
apples = 56
peaches = 33
print(f"Anna has {apples} apples and {peaches} peaches.")

# 10. With % operator
apples = 1004
peaches = 123
print("Anna has %d apples and %d peaches." % (apples, peaches))

# 11*. With variable substitutions by name (hint: by using dict)
fruits_dict = {
    "apples_key" : 3,
    "peaches_key" : 5,
}

print("Anna has {apples_key} apples and {peaches_key} peaches.".format(**fruits_dict))

# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# # (2)
#list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
lst = [num**2 if num % 2 == 1 else num**4 for num in range(10)]
print(lst)

# 13. Convert (2) to regular for with if-else
lst_2 = []
for num in range(10):
    if num % 2 == 0:
        lst_2.append(num // 2)
    else:
        lst_2.append(num * 10)
print(lst_2)

#
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# # (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# # (5)
#dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# # (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

# 14. Convert (3) to dict comprehension.
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)

# 15*. Convert (4) to dict comprehension.
d_comprehension = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_comprehension)

# 16. Convert (5) to regular for with if.
dict_1 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_1[x] = x ** 3
print(dict_1)

# 17*. Convert (6) to regular for with if-else.
dict_2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_2[x] = x ** 3
    else:
        dict_2[x] = x
print(dict_2)

# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y

# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_lmb = list(map(lambda num: num * 2, lst_to_sort))
print(lst_lmb)

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(lambda x, y: x ** y, list_A, list_B))
print(list_C)

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(lst_to_sort)

filtered_lst = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(filtered_lst)

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)

negative_numbers = list(filter(lambda num: num < 0, b))
print(negative_numbers)

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

common_values = list(filter(lambda common: common in list_1, list_2))
print(common_values)