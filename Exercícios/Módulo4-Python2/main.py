'''Crie um arquivo main.py, importe a classe “Quadrado”, crie uma nova
instância e acesse seus métodos.'''

from ex5 import Quadrado

def main():
    quad = Quadrado(42)

    print(f'A área do quadrado é {quad.get_area()}')
    print(f'O perímetro do quadrado é {quad.get_perimetro()}')


if __name__ == "__main__":
    main()