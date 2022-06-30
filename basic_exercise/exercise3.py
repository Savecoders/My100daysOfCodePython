categories = ["proteina", "carbohidrato", "lacteos"]
info = ["arroz-c", "arroz-p" "queso-l", "leche-l",
        "huevos-p", "lentejas-p", "tallarin-p"]

cat = input("Ingrese la categoria que busca: ")

if cat in categories:
    for eat in info:
        if eat[len(eat)-1] == cat[0]:
            print(eat)
else:
    print("no existe")
