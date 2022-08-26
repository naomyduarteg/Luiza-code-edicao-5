#calculando o valor do emprestimo com base na formula: valor_final = valor_emprestimo+(valor_emprestimo*taxa*tempo)

valor_emprestimo = float(input())
taxa = float(input())
tempo = int(input())
print(f'Valor final a pagar: R${valor_emprestimo+(valor_emprestimo*taxa*tempo)}')