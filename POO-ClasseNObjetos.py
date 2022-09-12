# Criando a classe
class Televisão:
    def __init__(self, tela, polegadas) -> None:
        self.tela = tela
        self.polegadas = polegadas
    

# Instanciando os objetos (Gerando os objetos)
SonyBravia = Televisão('LCD', 32)
Samsung = Televisão('OLED', 24)

# Aqui podemos printar na tela qualquer característica atribuida ao nosso objeto
print('A televisão tem: ',SonyBravia.polegadas, 'polegadas')



