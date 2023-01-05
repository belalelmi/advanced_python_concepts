class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)  # <------
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


# introspection using the dir method

wizard1 = Wizard('merlin', 323, 'asdsadsa@sdsa.com')

print(dir(wizard1))
