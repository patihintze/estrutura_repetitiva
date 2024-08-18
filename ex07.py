numero = int(input("Digite um número inteiro: "))
soma = 0
while numero != 0:
    if numero % 2 != 0:
        numero += 1
    soma = 0
    for i in range(5):
        soma += numero
        numero += 2
    
    print(f"SOMA: {soma}")
    numero = int(input("Digite um número inteiro: "))
