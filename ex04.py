while True:
    print("Digite os valores das coordenadas X e Y: ")
    x = int(input())
    y = int(input())
    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif x > 0 and y < 0:
        print("Q4")
    if not x != 0 and y != 0:
        break

