# Decorator

def my_decorator(func):
    def wrap_function():
        print('***********')
        func()
        print('***********')
    return wrap_function


def hello():
    print('hello world')


def bye():
    print('bye bye world')


hello2 = my_decorator(hello)
hello2()

# similar to doing the following

my_decorator(hello)()

# this looks confusing & thus is it better
# to use the @decorator tag: see the first decortor file -> decorator.py
