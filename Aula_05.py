"""
Faixas?
-até 2000 - 20%
-2000 a 3500 -15%
-3500 e 5000 - 10%
- acima 5000 5%
"""

salario_atual= float(input("Informe o seu salário atual:"))
if salario<2000:
    print("O seu salário receberá um aumento de 20%")
    novo_salario=salario_atual*1.2
    valor_do_aumento_em_real = novo_salario - salario_atual
    print("O valor do aumento em R$")
    print("O seu novo salário é R$",novo_salario)
elif 2000<=salario_atual<3500:
    print("O seu salário receberá um aumento de 15%")
    novo_salario= salario_atual*1,5
    print("O seu novo salário é R$", novo_salario)
elif 3500 <=salario_atual < 5000:
    print("O seu salário receberá um aumento de 10%")
    novo_salario = salario_atual * 1,0
    print("O seu novo salário é R$", novo_salario)