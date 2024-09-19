# number = int(input("Enter a number: "))
#
#
# def prime_number(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
#
# print(prime_number(number))

# fruits = ['apple', 'banana']
# fruits[fruits.index('banana')] = 'almond'
# print(fruits)

#
# my_list = [1, 2, 3, "Hi", [5, 6]]
#
# print(my_list[4][0], my_list[4][1], my_list[3][0])
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
#
# for i in matrix:
#     for j in i:
#         print(j)

# x = [1, 2, 3, "Hello"]
# y = [4, 5, 6, 7]
# print(x + y)
# print(y + x)
# print(x * 3)
#
# x = ["A", "BF", "Rg"]
# print(len(x))
# print(max(x))
# print(min(x))
# # print(sum(x))
#
#
# my_list = [1, 2, 'Hi', 79]
# my_list.remove('Hi')
# print(my_list)
# my_list.pop(2)
# print(my_list)
#
# my_list.clear()
# print(my_list)
# del my_list
# print(my_list)

# my_list.append(4)
# print(my_list)
# my_list.insert(1, 6)
# print(my_list)
#
# my_list[3] = 'Hi'
# print(my_list)

# my_num = [1, 6, 7, 2, 4, 5]
# my_num.sort(reverse=True)
# my_num.reverse()
# print(my_num)


# my_list_one = []
# for i in range(10):
#     my_list_one.append(i)
#
# print(my_list_one)
#
# my_list_two = list(range(10))
# print(my_list_two)


# my_list = [i ** 2 for i in range(1, 10) if i % 2 == 0]
# print(my_list)


# my_dict = {'name': 'Nini', 'last_name': 'kvinikadze'}


# keys_list = list(my_dict.keys())
# values_list = list(my_dict.values())
# my_set = set()
# my_set.update(keys_list, values_list)
# print(my_set)

# print(my_dict.items())

# for i, j in my_dict.items():
#     print(i, '->', j)


# my_dict = {'name': 'Nini', 'last_name': 'kvinikadze'}
# copy_dict = my_dict.copy()
# copy_dict.clear()
# print(copy_dict)
# print(my_dict)
# copy_dict = my_dict
# copy_dict.clear()
# print(copy_dict)
# print(my_dict)

my_dict = {'fruit': {1: 'apple', 2: 'orange', 3: 'pear'}, 'food': 'bread'}
print(my_dict.get('fruit')[2])
print(my_dict.get('fruit').get(2))
