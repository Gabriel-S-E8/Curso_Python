#for utilizando linha
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elemento in lista:
    print(elemento)

#for utilizando tupla
tupla = (1, 2, 3,)
for elemento in tupla:
    print(elemento)

#for utilizando dicionario

pessoa = {
    "nome": "Gabriel",
    "idade": 22,
    "altura": 1.80,
    "cidade": "Sao Paulo"}

for elemento in pessoa.keys():
    print("\n", elemento)

for elemento in pessoa.values():
    print(elemento)

for elemento, valor in pessoa.items():
    print(f"{elemento}: {valor}")


# range(): intervalo numerico
print(list(range(0, 11)))

for numero in range(5):
    print("Numero: \n", numero)

print(lista)
print
for indice in range(0, len(lista)):
    print("Indice", indice)
    print("Elemento", lista[indice])

    if indice == 9:
        lista[indice] = 8
    else:
        lista[indice] = 0
print (lista)

#enumerate()
lista_enumerate = ["a", "b", "c", "d",]

for indice, valor in enumerate(lista_enumerate):
    print(f"Indice: {indice}: {valor}")

