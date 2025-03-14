#funcoes

def saudacao(nome, idade):
    print(f"Olá, {nome}. Vocês tem {idade} anos.")
    
print("\n Chamando a função saudacao: ")

saudacao("alice", "18")

# função com retorno

def quadrado(numero):
    resultado = numero ** 3
    
    return resultado

print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(9)

print(resultado_quadrado)

# funcao com multiplos parametros
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

print("Resultado da soma", soma(1, 2))


