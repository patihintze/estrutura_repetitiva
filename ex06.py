cod = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))
alcool = 0
gasolina = 0
diesel = 0

while cod != 4:
    match cod:
        case 1:
            alcool +=1

        case 2:
            gasolina +=1
        case 3:
            diesel +=1
    cod = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

print(f"Alcool = {alcool}")
print(f"Gasolina = {gasolina}")
print(f"Diesel = {diesel}")