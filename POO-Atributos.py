class veiculo():
    rodas = 0
    cilindradas = 0
    velocidade_max = 0
    
    # Definindo a variável privada
    __paísDeOrigem = 'Brasil'
    
    def paisDeOrigem(self):
        return self.__paísDeOrigem
    
    def acelerar(self):
        print('Acelerando!')
        
    def freiar(self):
        print('Freiar!')
        
    
# Inicializando os objetos de classe
carro = veiculo()
moto = veiculo()
bicicleta = veiculo()

# Adicionando os atributos de classe de cada objeto
carro.rodas = 4
carro.cilindradas = 400
carro.velocidade_max = 200

moto.rodas = 2
moto.cilindradas = 150
moto.velocidade_max = 180

bicicleta.rodas = 2
bicicleta.cilindradas = 0
bicicleta.velocidade_max = 40

# Note que cada objeto tem uma característica de classe diferente


# Vamos agora verificar as informações armazenadas
#print(carro.cilindradas)
#print(moto.cilindradas)

# Vamos verificar se os métodos funcionam corretamente
#carro.acelerar()
#carro.freiar()

# Para termos o output correto, temos de chamar a função no print
print(carro.paisDeOrigem())

# Se tentarmos chamar a variável diretamente 
# como fizemos anteriormente teremos um erro
print(carro.__paísDeOrigem)
