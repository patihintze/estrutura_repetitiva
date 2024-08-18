print("Digite as idades: ")
somaidade = 0
cont = 0
idade = int(input())
if idade < 0:
    print("Impossível calcular.")
else:
    while idade >= 0:
        somaidade += idade
        cont += 1
        idade = int(input())
    media = somaidade / cont
    print(f"Media: {media:.2f}")