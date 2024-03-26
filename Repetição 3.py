"""

Variavel Composta: aceita mais de um valoe.
lista= ["arroz! , "feijão", "carne"
"""

#lista = [ "arroz", "feijão", "carne"]
#print(lista)
#
#nomes = ["Jãoo", "Pedro", "Maria", "Ana"]
#print(nomes)


notas=[ ]
while True:
    nota = int(input("Digite uma nota:"))
    if 0 < nota <= 10:
        notas.append(nota)
    else:
        print("Nota Invalida!")
        break
        print(notas)
        