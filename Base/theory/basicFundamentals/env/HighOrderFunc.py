
DATA = [
    {"name": "John", "age": 25, "organization": "Platzi",
        "job": "dev", "lenguage": "python"},
    {"name": "Javier", "age": 22, "organization": "Santander",
     "job": "dev", "lenguage": "python"},
    {"name": "Ricardo", "age": 35, "organization": "Google",
        "job": "data science", "lenguage": "java"},
    {"name": "Yesica", "age": 28, "organization": "Facebook",
        "job": "dsg", "lenguage": "javascript"},

]


def run():
    filterLenguage = list(filter(lambda x: x["lenguage"] == "python", DATA))
    names = list(map(lambda x: x["name"], filterLenguage))

    # use pipe operator to chain functions
    oldPeople = list(map(lambda diccionary: diccionary | {
                     "old": diccionary["age"] > 30}, DATA))
    print(oldPeople)


if __name__ == "__main__":
    run()
