#list, set, dictionary

mylist = []

for char in 'hello world':
    mylist.append(char)
print(mylist)


mylist2 = [char for char in 'hello world']
print(mylist2)


mylist3 = [num for num in range(0, 100)]
mylist3 = [num*2 for num in range(0, 100)]
print(mylist3)


mylist4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(mylist4)
