num = int(input("Quantos números serão digitados: "))
soma = 0
for i in range (num):
    x = int(input("Digite um número: "))
    soma += x
print(f"Soma: {soma}")