# Um decorador é uma função que recebe outra função como argumento 
# E retorna uma nova função que adiciona algum comportamento adicional à função original.

def meu_decorador(func):
    def wrapper():
        print("Antes da execução da função.")
        func()
        print("Depois da execução da função.")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Executando a função.")

minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self) -> Any:
        print("Antes da execução do método (decorador de classe).")
        self.func()
        print("Depois da execução do método (decorador de classe).")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Executando a segunda função.")

segunda_funcao()