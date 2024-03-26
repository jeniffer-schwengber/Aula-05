while True:
    login = str(input("Crie o seu login:"))
    senha = str(input("Crie uma senha:"))
    if login == senha:
        print("Erro! Login e senha não podem ser iguais!")
    else:
        print("login e senha criados com sucesso!")
        break