class Tamagotchi:
    def __init__(self, nome= "Bingo", fome= True, saude= True, idade= 1):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    
    def altera_nome(self, novo_nome):
        self.nome = novo_nome

    def altera_fome(self, esta_com_fome):
        self.fome = esta_com_fome

    def altera_saude(self, esta_saudavel):
        self.saude = esta_saudavel

    def altera_idade(self, nova_idade):
        self.idade = nova_idade



    def retorna_nome(self):
        return self.nome
    
    def retorna_fome(self):
        return self.fome
    
    def retorna_saude(self):
        return self.saude
    
    def retorna_idade(self):
        return self.idade
    


    def humor(self):
        if self.fome is False and self.saude is True:
            print("Seu Tamagotchi está feliz e saudável")

        elif self.fome is True:
            print("Seu tamagotchi está com fome!")

        elif self.saude is False:
            print("Seu tamagotchi está doente, dê remédio!")



##################################################
        
bichinho = Tamagotchi()


#Altera
bichinho.altera_nome("Binga")
print(bichinho.nome)

bichinho.altera_fome(False)
print(bichinho.fome)

bichinho.altera_saude(True)
print(bichinho.saude)

bichinho.altera_idade(2)
print(bichinho.idade)

#Retorna
print(bichinho.retorna_nome())
print(bichinho.retorna_fome())
print(bichinho.retorna_saude())
print(bichinho.retorna_idade())

#Humor da binga
print(bichinho.humor())