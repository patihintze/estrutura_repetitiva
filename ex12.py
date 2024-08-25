x = int(input("Quantos numeros voce vai digitar? "))
for i in range(x):
    num = int(input("Digite um número: "))
    if num % 2 != 0 and num < 0:
        print("Impar negativo")
    elif num % 2 != 0 and num > 0:
        print("Impar positivo")
    elif num % 2 == 0 and num < 0:
        print("Par negativo")
    elif num % 2 == 0 and num > 0:
        print("Par positivo") 
    elif num == 0:
        print("Nulo")