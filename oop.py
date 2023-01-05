''' object oriented programming concepts '''


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


# player1 = PlayerCharacter('bhe', 10)
# print(player1.age)
# print(player1.run())
print(PlayerCharacter.adding_things(2, 4))
