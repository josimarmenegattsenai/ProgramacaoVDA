
qtd_blusas = int(input("Digite a quantidade de blusas: "))

metros_totais = qtd_blusas * 120
novelos = metros_totais // 125  # Divisão inteira (descarta o que vem após a vírgula)


if metros_totais % 125 > 0:
#    novelos += 1

print(f"Total de novelos necessários: {novelos}")