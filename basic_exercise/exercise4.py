
lst_datos = [
    'GQH-0023;exceso velocidad;12/1',
    'GQH-0023;doble fila;12/06',
    'GQH-0024;carril metrovia;12/2'
]

lst_valores = [
    'exceso velocidad/127.5',
    'doble fila/42.5',
    'carril metrovia/425',
]


def obtener_placas(list_datos: list, mes: int):
    arr_list_placas = []
    for placa in list_datos:
        arr_list_placas.append(placa.split(';'))
    return list(filter(lambda arr: int(arr[2].split('/')[1]) == mes, arr_list_placas))


def calcular_multas(placa: str, list_datos: list, list_valores: list) -> list:

    list_placas = list(
        filter(lambda data: data.split(';')[0] == placa, list_datos))
    arr_list_placas = []

    for placas in list_placas:
        arr_list_placas.append(placas.split(';'))

    hash_val = {}

    for valor in list_valores:
        multa, val = valor.split('/')
        hash_val[multa] = val

    cantidad_de_multas = 0
    valor_pagar = 0

    for placas in arr_list_placas:
        if placas[0] == placa:
            cantidad_de_multas += 1
            valor_pagar += float(hash_val[placas[1]])

    return [cantidad_de_multas, valor_pagar, ]


def top_n(list_datos: list, list_valores: list, n) -> list:
    arr_list_placas = []

    for placas in list_datos:

        placa = placas.split(';')[0]

        if not placa in arr_list_placas:

            arr_list_placas.append(placa)

    placas = list(
        map(lambda placa:
            [placa, calcular_multas(placa, list_datos, list_valores)[1]], arr_list_placas))

    placas_sort = sorted(placas, key=lambda x: x[1], reverse=True)

    return placas_sort[slice(0, n)]


print(obtener_placas(lst_datos, 1))
print(calcular_multas('GQH-0023', lst_datos, lst_valores))
print(top_n(lst_datos, lst_valores, 2))
