# Decorator

def my_decorator(func):
    def wrap_function():
        print('***********')
        func()
        print('***********')
    return wrap_function


@my_decorator
def hello():
    print('hello world')


@my_decorator
def bye():
    print('bye bye world')


hello()
bye()
