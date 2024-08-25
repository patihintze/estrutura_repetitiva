x = int(input("Quantos numeros voce vai digitar? "))
dentro = 0
fora = 0
for i in range (x):
    num = int(input("Digite um número: "))
    if num >= 10 and num <= 20:
        dentro+=1
    else: fora+=1
print(f"Dentro: {dentro}")
print(f"Fora: {fora}")