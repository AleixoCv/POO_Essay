import os
os.system('cls') or None

# Para podermos utilizar interface em Python, temos que utilizar o seguinte import - Abstract Base Class
from abc import ABC, abstractmethod

# Para definir uma classe, utilizamos
class animal(ABC):

    @abstractmethod
    def som(self):
        pass

class cachorro(animal):