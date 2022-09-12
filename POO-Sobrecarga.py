class Pessoa():
    
    
    # Definindo um método
    def idade(idade = None):
        if idade is not None:
            print("Você tem ", idade, " anos!")
        else:
            print("Não sei quantos anos você tem!")
        
    # Sobrecarregando um método - será impresso "Não sei quantos anos você tem!"
    idade()
    
    # Sobrecarregando o método novamento - será impresso "Você tem 28 anos!"
    idade(28)
