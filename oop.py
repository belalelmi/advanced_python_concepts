''' object oriented programming concepts '''


class PlayerCharacter:
    ''' classes allow us to create blueprints (objects) that
    hve their own methods and attributes '''

    # class object attribute
    membership = True

    #  __init__ is called a dunder method or a magic method
    def __init__(self, name, age):
        ''' creating player attrributes '''
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('bhe', 81)

print(player1.age)
print(player1.run())
print(player1.shout())

player1.run()
