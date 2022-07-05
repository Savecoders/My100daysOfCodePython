
class Drink:
    # SELF is equal to this in JS

    # created methods
    def __init__(self, name):
        # ENCAPSULATION is to protect arguments
        # in this case it's name
        # the argument needs to have two _
        # example: __name = name
        self.__name = name

    def getDetails(self):
        return "the drink is " + self.__name


# INHERITANCE class methods
class Beer(Drink):

    # the Statci Element for class
    Count = 0

    def __init__(self, name, brand, alchol):
        # SUPER invokes methods father of the constructor
        # in this case is name
        super().__init__(name)
        self.__brand = brand
        self.__alchol = alchol
        Beer.Count += 1

    # POLYMORPHISM
    # is the ability of the methods to
    # reuse the method to be able to modify it

    def getDetails(self):
        return super().getDetails() + " of the brand: " + self.__brand + " the alchol: " + str(self.__alchol)

    # created static methods
    # it's imposible to modify the method
    @staticmethod
    def getClassInfo():
        return "have been created " + str(Beer.Count) + " Objects"


# MULTIPLE INHERITANCE IN PYTHON
class Product:
    def __init__(self, cost, price):
        self.cost = cost
        self.price = price

    def getGain(self):
        return self.price - self.cost


class Soda(Drink, Product):

    def __init__(self, name, brand, sugar, cost, price):
        # the other form the produce inherited from this class
        # use the Name from class and not use Super()
        # and invoke the self
        Drink.__init__(self, name)
        Product.__init__(self, cost, price)
        self.__brand = brand
        self.__sugar = sugar

    def getDetails(self):
        return super().getDetails() + " of the brand: " + self.__brand + " the sugar: " + str(self.__sugar)


drink = Drink("agua")

print(drink.getDetails())

# this "drink" is invalid because, the argument is protected by encapsulation
# print(drink.__name)

beer1 = Beer("Pale ale", "Minerva", 4.5)

# thanks to the INHERITANCE
# this getDetails method is called for Beer
# Because of the class Drink is father form the class Beer

print(beer1.getDetails())

# print the static element
print(Beer.getClassInfo())

soda = Soda("SodaZero", "Coca Cola", 4.5, 2, 3.5)

print(soda.getDetails())
print(soda.getGain())
