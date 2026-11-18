# @classmethod
# @staticmethod
# A diferença entre os dois é que o classmethod recebe a classe como primeiro argumento
# enquanto o staticmethod não recebe nenhum argumento especial.

class MinhaClasse:
    valor = 10  # Atributo de classe

    def __init__(self, nome) -> None:
        self.nome = nome  # Atributo da instância

    # requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"

# Não precisa de uma instância para ser chamado
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para valor={cls.valor}"

# Não tem acesso a instância ou a classe, é apenas uma função dentro da classe
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca},\nModelo: {carro1.modelo},\nAno: {carro1.ano}")

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Divisão por zero não é permitida"

print(Matematica.somar(10, 5))
print(Matematica.subtrair(10, 5))           
print(Matematica.multiplicar(10, 5))
print(Matematica.dividir(10, 5))    
print(Matematica.dividir(10, 0))  # Testando divisão por zero