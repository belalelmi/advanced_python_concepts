#set, dictionary


# mylist2 = {char for char in 'hello world'}
# print(mylist2)


# mylist3 = {num for num in range(0, 100)}
# mylist3 = {num*2 for num in range(0, 100)}
# print(mylist3)


# mylist4 = {num**2 for num in range(0, 100) if num % 2 == 0}
# print(mylist4)
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)


my_dict2 = {k: k*2 for k in [1, 2, 3]}
print(my_dict2)
