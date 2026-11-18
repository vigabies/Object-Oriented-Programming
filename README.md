# POO em Python

Exemplos simples de Programação Orientada a Objetos (POO) em Python, com código comentado para ajudar a entender cada conceito.

## Conceitos abordados

- **Classe e Objeto:** a classe é o molde, e os objetos são instâncias criadas a partir dela.
- **Atributos e Métodos:** dados guardados no objeto e funções que pertencem à classe.
- **Construtor (`__init__`):** método especial que roda quando um objeto é criado.
- **Herança:** uma classe reaproveita atributos e métodos de outra classe.
- **Polimorfismo:** o mesmo nome de método se comporta de forma diferente dependendo do objeto.

## Exemplos

### 1. Classes e objetos

```python
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
person2 = Person(name="Rodrigo", age=32)

print(person1.greeting())
print(person2.greeting())
```

**Saída:**
```
Hello, my name is Alice and I am 30 years old.
Hello, my name is Rodrigo and I am 32 years old.
```

### 2. Herança e polimorfismo

```python
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def