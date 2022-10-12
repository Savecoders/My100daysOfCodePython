
menu = """
  Welcome to the change calculator.
  1 - Pesos colombian
  2 - Pesos argentine
  3 - Pesos mexican
  
  select an option: """

option = int(input(menu))

valueDolar = 3875

if option == 1:
    print("You selected Colombian pesos")
    valueDolar = 3875
elif option == 2:
    print("You selected Argentine pesos")
    valueDolar = 65
elif option == 3:
    print("You selected Mexican pesos")
    valueDolar = 24
else:
    print("Invalid option, defaulting to Colombian pesos")


pesos = float(input("How many pesos do you have? "))


dolar = pesos / valueDolar

# print two decimals after the point with {:.2f}
print("You have ${:.2f} dolars".format(dolar))
