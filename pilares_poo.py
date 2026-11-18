# Heranca

print("\nExemplo de herança:")

# Superclasse; classe base ou classe pai
class Animal:
    # def cria uma funcao, ou dentro de uma classe, um metodo
    # __init__ e o metodo construtor: roda automaticamente quando um objeto e criado
    # self = o proprio objeto; nome = valor passado na criacao
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return

    # Metodo "generico": existe so para os filhos sobrescreverem
    def emitir_som(self):
        # "pass" significa "nao faca nada": serve para deixar o metodo vazio
        # sem dar erro, ja que cada animal emite um som diferente
        pass


# HERANCA: Cachorro(Animal) significa que Cachorro herda de Animal
# Ou seja, Cachorro ja tem __init__, nome e andar() sem precisar escrever de novo
class Cachorro(Animal):
    # POLIMORFISMO (sobrescrita): o metodo tem o mesmo nome do pai (emitir_som), mas aqui ele faz uma coisa diferente
    def emitir_som(self):
        return "Au au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"