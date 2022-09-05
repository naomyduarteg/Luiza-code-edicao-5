'''1. Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
classe onde teremos o retorno do documento, o retorno do nome e
verificação de tipo de pessoa, onde um método irá receber como
parâmetro “F” ou “N” para trazer fumante ou não fumante.
Feito isso, crie uma instância e retorne esses valores.
2. Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método
exclusivo para a classe e acesse-o
3. Escreva uma classe “PessoaJurica” e herde Pessoa, agora
modificando o comportamento, retorne o cnpj. Crie uma instância e
acesse os dados'''


class Pessoa:

    def __init__(self, pessoa, cpf, nome, idade):
        self.pessoa = pessoa 
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.__tipo = None 
    
    def set_fumante(self, tipo): 
        self.__tipo = tipo

    def get_fumante(self): 
        if self.__tipo == 'N':
            return f'Não-fumante'
        elif self.__tipo == 'F':
            return f'Fumante'
        else:
            return f'Não informou se é fumante ou não.'

    def __repr__(self):
        return f'Tipo de pessoa: {self.pessoa}. CPF: {self.cpf}.  Nome: {self.nome}. Fumante? {self.get_fumante()}'


class PessoaFisica(Pessoa):

    def __init__(self,pessoa, cpf, nome, idade):
        super().__init__(pessoa, cpf, nome, idade)

class PessoaJuridica(Pessoa):

    def __init__(self,pessoa, cpf, nome, idade, cnpj):
        super().__init__(pessoa, cpf, nome, idade)
        self.cnpj = cnpj
    
    def __repr__(self):
        return f'Tipo de pessoa: {self.pessoa}. CNPJ: {self.cnpj}.  Nome: {self.nome}. Fumante? {self.get_fumante()}'

#istâncias 

#pessoa1 = Pessoa('Física', 666666666, 'Jade', 45)
#pessoa1.set_fumante('F')
#print(pessoa1)
#pessoa2 = PessoaFisica('Física', 77777777, 'Karla', 39)
#pessoa2.set_fumante('N')
#print(pessoa2)
pessoa3 = PessoaJuridica('Jurídica', 66666666666, 'Larissa', 45, 6666666666)
pessoa3.set_fumante('N')
print(pessoa3)
