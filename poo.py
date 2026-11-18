# POO (Programacao Orientada a Objetos)

# Classe de exemplo
class Person:
    # Metodo construtor: roda automaticamente quando um novo objeto e criado
    # self = o proprio objeto; name e age = valores passados na criacao
    # "-> None" indica que esse metodo nao retorna nada
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # Metodo (uma funcao que pertence a classe)
    def greeting(self):
        # Retorna um texto (f-string) com o nome e a idade do objeto inseridos
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Objetos
# Cria um objeto (instancia) da classe Person, passando os valores por posicao
person1 = Person("Alice", 30)
# Chama o metodo greeting do person1 e guarda o texto retornado em uma variavel
message = person1.greeting()
print(message)

# Outra maneira de fazer
person2 = Person(name="Rodrigo", age=32)
message = person2.greeting()
print(message)