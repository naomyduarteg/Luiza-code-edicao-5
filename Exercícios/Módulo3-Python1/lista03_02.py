#programa que pede nome, cidade e ano de nascimento e retorna cada um destes valores em uma linhda, além de quantos anos o usuário terá em 2030
nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade de nascimento: ")
ano = int(input("Digite seu ano de nascimento: "))
print(f'{nome}')
print(f'{cidade}')
print(f'{ano}')
print(f'Em 2030 você terá {2030 - ano} anos.')