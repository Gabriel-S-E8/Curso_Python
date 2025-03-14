#if, elif e else

#exemplo de "if"
print("Exemplo de if")
idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Maior de idade")
elif idade >= 12:
    print("adolescente")
else:
    print("Você é menor de idade.")


mensagem = "pode tirar a carteira de habilitação" if idade >= 18 else "Você \
não pode tirar a carteira de habilitação"

print(mensagem)