senha_user = int(input("Digite a senha: "))
senha_correta = 2002

while senha_user != senha_correta:
    senha_user = int(input("Senha inválida. Tente novamente: "))
print("Acesso permitido.")