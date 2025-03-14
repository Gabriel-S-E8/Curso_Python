# declaração
nome = "Gabriel"
sobrenome = "Ferreira"

#declarando de multiplas linhas
nome_Completo = """Gabriel
Ferreira"""

# concatenação
nome_completo = nome + " " + sobrenome

print(nome_completo)
print(nome_Completo)

#quebra de linha
nome_completo_quebrado = "Gabriel \
Ferreira"

print(nome_completo_quebrado)

#formatação
print("Nome Completo (1a forma):", nome_completo)
print("Nome Completo (2a forma):" + nome, sobrenome)
print("Nome Completo (3a forma):" + "Gabriel" + "Ferreira")
print("Nome Completo (4a forma):" + "Gabriel", "Ferreira")
print("Nome Completo (5a forma):", nome_Completo)
print("Nome Completo (6a forma):", nome_completo_quebrado)
print("Nome Completo (7a forma):%s " % nome_completo)
print("Nome Completo (8a forma):%s %s" % (nome, sobrenome))
print("Nome Completo (9a forma):%s %s" % ("Gabriel", "Ferreira"))
print(f"Nome Completo (10a forma):{nome} {sobrenome}")
print("Nome Completo (11a forma):{0} {1}".format(nome, sobrenome))
