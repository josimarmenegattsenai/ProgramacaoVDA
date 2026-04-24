dia_entrega = int(input("digite o dia da entrega do produto :"))
mes_entrega = int(input("digite o mes da entrega do produto :"))

dias_acumulados = 10

for mes in range(1, mes_entrega):
    dias_acumulados += 30
total_dias = dias_acumulados + dia_entrega
print(f"o produto sera entregue em  {total_dias} dias:")