# write a function that enter firstname, middlename 
# and lastname inside a file.txt

def addNames(name: str, middlename: str, lastName: str):
  with open("to.txt", "a") as file:
    file.write(f"{name} {lastName} {lastName} \n")
    file.close()


addNames("Jose", "Carlos", "Herrera")
