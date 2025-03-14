#dicionario exemplo

pessoa = {
    "nome": "Gabriel",
    "idade": 22,
    "altura": 1.80,
    "cidade": "Sao Paulo"}

print(pessoa)

print(pessoa["nome"])
print(pessoa["idade"])

pessoa["sobrenome"] = "Ferreira"
print(pessoa)

pessoa["idade"] = 23
print(pessoa)


#removendo um par chave-valor
del pessoa["sobrenome"]
print(pessoa)

# pessoa.clear()
# print(pessoa)

#Metodos: keys(), values(), items()
chaves = pessoa.keys()
print("chaves", chaves)

#transformando em uma lista pois os metodo retornan um dicionario
chaves = list(pessoa.keys()) 
print("primeira chave", chaves[0])

valores = list(pessoa.values())
print("valores", valores)
print("primeiro valor", valores[0])

itens = list(pessoa.items())
print("itens", itens)

print("primeiro item", itens[0])
print("valor do primeiro item", itens[0][1])

