#programa que divide o valor da conta de energia entre os moradores

valor = float(input('Insira o valor da conta de energia: '))
moradores = int(input('Insira a quantidade de moradores da casa: '))
print(f'Cada um deverá contribuir com R$ {round(valor/moradores, 2)} reais')