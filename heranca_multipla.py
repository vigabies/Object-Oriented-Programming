class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def fazer_som(self):
        pass

# Subclasses; classes derivadas ou classes filhas
class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando"

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"

class Morcego(Mamifero, Ave):  # Herança múltipla
    def emitir_som(self):
        return "Morcegos emitem sons de alta frequência"

morcego = Morcego(nome="Bruce")

# Acessandro métodos das classes pai Animal
print(f"{morcego.nome} faz: {morcego.emitir_som()}")

# Acessando métodos das classes Mamifero e Ave
print(morcego.amamentar())
print(morcego.voar())   