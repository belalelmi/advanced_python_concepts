from functools import reduce


# lambda param: action(param)


my_list = [10, 20, 30, 21, 99]
# Example 1


# def multiply_by2(listt):
#     new_list = []
#     for item in listt:
#         new_list.append(item*2)
#     return new_list


# # Example 2
# def multiply__by2(item):
#     return item*2


# def only_odd(item):
# return item % 2 != 0


# print(multiply_by2([2, 4, 6]))


##################################################################################################

# map, filter, zip, & reduce

# a = [1, 2, 3]
# x = map(multiply_by2, a)
# print(list(x))


# w = [1, 2, 3]
# x = map(multiply__by2, w)
# print(list(x))


# b = [1, 2, 3, 5, 6, 7, 8, 9, 877, 655, 444]
# x = filter(only_odd, b)
# print(list(x))


# c = [1, 2, 877, 655, 444]
# joint = zip(c, my_list)
# print(list(joint))


# def accumulator(acc, item):
#     return acc + item

# print(reduce(accumulator, my_list, 0))

print(list(filter(lambda item: item % 2 != 0, my_list)))
