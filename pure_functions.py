# Example 1
def multiply_by2(listt):
    new_list = []
    for item in listt:
        new_list.append(item*2)
    return new_list


# Example 2
def multiply_by2(item):
    return item*2


print(multiply_by2([2, 4, 6]))


##################################################################################################

# map, filter, zip, & reduce
a = [1, 2, 3]
x = map(multiply_by2, a)
print(list(x))
