x = int(input("Quantos casos voce vai digitar? "))
for i in range(x):
    print("Digite tres numeros: ")
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    print(f"Media: {media:.1f}")