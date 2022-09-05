'''Crie um professor de classe com atributos nome, idade e salário, onde
o salário deve ter um método privado que não pode ser acessado fora
da classe.
a. Crie um método para acessar o método privado, onde é passada
a identificação do usuário se ele pode ou não acessar'''

class Professor:

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario

    def acesso_privado(self, usuario):
        self.usuario = usuario
        if self.usuario == 'diretor':
            return f'Acesso permitido. Salario informado igual a R${self.__salario}'
        elif self.usuario == 'diretora':
            return f'Acesso permitido. Salario informado igual a R${self.__salario}'
        else:
            return f'Você não tem acesso aos salários.'
        
#teste com a instância
prof1 = Professor('Odair', 55, 2500)
print(prof1.acesso_privado('diretora'))