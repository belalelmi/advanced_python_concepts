'''Abstraction in python is defined as a process of handling complexity by hiding unnecessary information
from the user. This is one of the core concepts of object-oriented programming (OOP) languages.'''


class PlayerCharacter:
    ''' classes allow us to create blueprints (objects) that
    hve their own methods and attributes '''

    # class object attribute
    membership = True

    #  __init__ is called a dunder method or a magic method
    def __init__(self, name='anonymous', age='0'):
        ''' creating player attrributes '''
        if age > 18:
            self.name = name   # attributes
            self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('bhe', 90)
