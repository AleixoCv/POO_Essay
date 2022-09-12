# Aqui, criamos nossa classe mãe ou SuperClasse
class Veiculos():
    terreno = ''
        
    def acelerar(self):
        print("Acelerando!")
    
    def freiar(self):
        print("Freiando!")
    
    
class Motor():
    engrenagens = 5

#Vamos criar nossa primeira classe com herança
class Carro(Veiculos, Motor):
    terreno = 'terrestre'
    cor = 'vermelho'
    modelo = 'jeep'
    
    def acelerar(self):
        print("Acelerando o carro!")
        
class Lancha(Veiculos):
    terreno = 'aquatico'
    cor = 'branca'
    modelo = 'jetspeed'
        
# Ambas as classes herdaram a característica de terreno
# E os métodos acelerar e freiar.

# Definimos os objetos
lancha = Lancha()
#carro = Carro()

# Chamamos os métodos e as variáveis
#print(carro.terreno)
#lancha.acelerar()

# Chamamos os métodos e as variáveis
#print(carro.engrenagens)
#carro.freiar()

# Definimos os objetos
carro = Carro()
carro2 = Veiculos()

# Agora verificamos as saídas dos métodos
carro.acelerar()
carro2.acelerar()