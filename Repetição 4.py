"""
Faça um progra,a que fique pedindo numeros quasiquer e aramaza em uma lista chamada numeros.
Caso o numero seja maior que 50, o program é encerrado.
"""
lista = []
while True:
    numero = int(input("Digite um numero:"))
    if 0 < numero <= 50:
        lista.append(numero)
    else:
        print("Lista Encerrada")
        break
    print(lista)
