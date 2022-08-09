# read the file.txt, get names and return
# number of times it repeats
import pandas as pd
import json

def read_file(filename: str) -> list[str]:
  try:
    with open(filename, "r") as f:
          lines = f.readlines()
          lines = [line.strip() for line in lines]
          return lines
  except:
    return "not fond of the file"


def separedNames(read_file: list[str]) -> list[str]:
  return list(map(lambda names: names.split(' ') , read_file))


# get names from list and return dict for number of times it repeats
def getDictNames(list_names: list[str]) -> dict:
  first_name, middle_name, last_name = {},{},{}
  
  def colapsedNames(dict_name, list_name, index, poss):
    return dict_name[list_name[index][poss]] + 1 if list_name[index][poss] in dict_name else 1

  for i in range(len(list_names)):
    first_name[list_names[i][0]] = colapsedNames(first_name, list_names, i, 0)
    middle_name[list_names[i][1]] = colapsedNames(middle_name, list_names, i, 1)
    last_name[list_names[i][2]] = colapsedNames(last_name, list_names, i, 2)

  return {
    "FirstName": first_name,
    "Middle_names": middle_name,
    "Last_names": last_name
  }



file = read_file("to.txt")
list_names = separedNames(file)
dict_names = getDictNames(list_names)

# print(dict_names)

# print(json.dumps(dict_names, sort_keys=False, indent=len(list_names)))

dataFrame = pd.DataFrame(dict_names)

dataFrame.fillna(0)

print(dataFrame.fillna(0))
