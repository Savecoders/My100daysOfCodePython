# multiply without symbol 

def recursion(number_one: float, number_two: float) -> float:
  if number_one == 0 or number_two == 0 :
    return 0
  
  if number_two > 0:
    return number_one + recursion(number_one, number_two - 1 )
  
  if number_two < 0:
    return -(number_one - recursion(number_one, number_two + 1 ))


#* Result: print(recursion(2, -3))


# enter first name, last name and printer in reverse order

#name = input("Enter your name: ")
#last_name = input("Enter your last name: ")

reverse = lambda string : string[::-1]

#* Result: print(reverse(name))
#* Result: print(reverse(last_name))


# enter a function that return the lesser number

number_list = [4,3,21,7,2]

lesser = lambda num: min(num)

#* Result: print(lesser(number_list))


# enter a function that return volume of a sphere

sphere = lambda radio: (4/3) * 3.1416 * ( radio ** 3 )

#* Result: print(sphere(12))


# enter a function that else adult or child

isAdult = lambda age : age <= 21

#* Result: print(isAdult(22))


# enter a function that if the number is odd or even

isDigit = lambda num : "number is even" if  num % 2 == 0 else "number is odd" 

print(isDigit(12))


# to write a function that enter a quantity infinity of numbers until
# to read Stop and later return the sum of the numbers

""" sum_numbers = 0

while True:
  letter = input("Enter a number: ")

  if letter.lower() == "stop":
    break
  else:
    try:
      sum_numbers += int(letter) 
    except:
      print("Invalid number")
      exit() """
  

#* print(sum_numbers)


# to write a function that enter name, last name add a file.txt

def addNames(name: str, lastName: str):
  with open("namecompleted.txt", "a") as file:
    file.write(f"{name} {lastName} \n")
    file.close()


addNames("Jose", "Carlos")
