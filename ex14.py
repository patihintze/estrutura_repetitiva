x = int(input("Quantos casos voce vai digitar? "))
for i in range(x):
    n1 = float(input("Entre com o numerador: "))
    n2 = float(input("Entre com o denominador: "))
    if n2 == 0:
        print("Divisão impossível.")
    else: 
        divisao = n1 / n2
        print(f"Divisão: {divisao}")