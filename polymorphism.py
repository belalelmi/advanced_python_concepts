# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

''' 4 pillars of OOP
4) polymorphism
3) inheritance
2) abstraction
1) encapsulation
'''

# Polymorphism with class methods:

# The below code shows how Python can use two different class types, in the same way.
# We create a for loop that iterates through a tuple of objects.
# Then call the methods without being concerned about which class type each object is.
# We assume that these methods actually exist in each class.


class USA():
    def capital(self):
        print("Washington, D.C is the capital of the US.")

    def language(self):
        print("English is the most widely spoken language in the USA.")

    def type(self):
        print("USA is a developing country.")


class Canada():
    def capital(self):
        print("Toronto is the capital of the world.")

    def language(self):
        print("English is the primary language of Canada.")

    def type(self):
        print("Canada is a developed country.")


obj_cad = Canada()
obj_usa = USA()
for country in (obj_cad, obj_usa):
    country.capital()
    country.language()
    country.type()
