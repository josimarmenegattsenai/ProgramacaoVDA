salario = float(input("Digite seu salario Atual: "))
x = salario * 0.15
aumento = salario + x
imposto = aumento * 0.08
salariofinal = aumento - imposto
print("O Salario sem aumento era: ", salario)
print("O Salario com aumento ficou: ", aumento)
print("O Salario final ficou: ", salariofinal)
