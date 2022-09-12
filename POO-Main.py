import os
os.system('cls') or None

# Para podermos utilizar interface em Python, temos que utilizar o seguinte import - Abstract Base Class
from abc import ABC, abstractmethod

# Para definir uma classe, utilizamos
class animal(ABC):

    def __init__(self, raca):
        self.raca = raca

    @abstractmethod
    def som(self):
        pass

# Aqui podemos ver uma classe que herda da classes animal o atributo de raça e adiciona um atributo de nome
class cachorro(animal):

    def __init__(self, raca, nome):
        self.nome = nome

    def som(self):
        print("Latido - Au Au")

# Definindo um objeto
objeto = cachorro('cachorro', 'Arya')

# Chamando um método dentro de uma classe. Também é importante perceber que o método só é chamado pois a classe cachorro
# atende aos requisitos de sua SuperClasse, ou classe mãe, de ter um método "som", senão haveria um erro
objeto.som() # O output dessa chamada será "Latido - Au Au".