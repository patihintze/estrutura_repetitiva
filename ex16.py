casos = int(input("Quantos casos de teste serao digitados? "))
qtd_sapo = 0
qtd_coelho = 0
qtd_rato = 0

for i in range(casos):
    qtd_cobaia = int(input("Quantidade de cobaias: "))
    tipo_cobaia = input("Tipo de cobaia: ")

    match tipo_cobaia:
        case "C":
            qtd_coelho += qtd_cobaia
        case "R": 
            qtd_rato += qtd_cobaia
        case "S":
            qtd_sapo += qtd_cobaia
    total = qtd_coelho + qtd_sapo + qtd_rato

print(f"Total de cobaias = {total}")
print(f"Total de coelhos = {qtd_coelho}")
print(f"Total de ratos = {qtd_rato}")
print(f"Total de sapos = {qtd_sapo}")
print(f"Percentual de coelhos: {qtd_coelho / total * 100:.2f}")
print(f"Percentual de ratos: {qtd_rato / total * 100:.2f}")
print(f"Percentual de sapos: {qtd_sapo / total * 100:.2f}")