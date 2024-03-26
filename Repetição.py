"""
Estruturas de Repetição(comandos de repetição)
- while(enquanto)
Enquanto a condição não for atendida a ordem fica se repetindo.
"""
while True:
    nota = float(input("Informe a nota do aluno"))
    if 0 < nota <= 10:
        print("Nota Válida!")
        break
    else:
        print("Nota inválida!")