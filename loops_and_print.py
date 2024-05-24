def enumerate_list(list):
    lista_1 = []
    lista_2 = []
    for elemento in list:
        if elemento != "":
            lista_1.append(elemento)
            print(lista_1)
    for index, element in enumerate(lista_1):
            lista_2.append(f"{index}. {element}")
    return lista_2
colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_list(colors))

def enumerate_backwards(list):
    lista_1 = []
    lista_2 = []
    for elemento in list:
        if elemento != "":
            lista_1.append(elemento[::-1])
            print(lista_1)
    for index, element in enumerate(lista_1):
            lista_2.append(f"{index}. {element}")
    return lista_2
colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_backwards(colors))
