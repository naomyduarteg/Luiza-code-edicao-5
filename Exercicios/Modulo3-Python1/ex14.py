#coletar a idade de duas pessoas e retornar True se a primeira idade for maior que a segunda
idade1, idade2 = input('Entre com os valores das idades: ').split()

if idade1 > idade2:
    print('True')

#por meio de uma função

def idade_comp(idade1,idade2):
    if idade1 > idade2:
        return True
