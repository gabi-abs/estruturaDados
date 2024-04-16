class Pessoa:
    def __init__(self, nome, idade=0, pesoG = 2_000, alturaCm = 30.0):
        self.nome = nome
        self.idade = idade
        self.pesoG = pesoG
        self.alturaCm = alturaCm

    def envelhecer(self):
        self.idade += 1

        if self.idade < 21:
          self.crescer(0.5)

    def engordar(self, gramas):
        self.pesoG += gramas

    def emagrecer(self, gramas):
        self.pesoG -= gramas

    def crescer(self, centimetros):
        self.alturaCm += centimetros


            

###################


pessoa01 = Pessoa(nome= "Gabriella") # Instânciando um objeto


pessoa01.envelhecer() #Chamadando o método envelhecer
print(pessoa01.idade)



pessoa01.engordar(10) #Chamando o método engordar
print(pessoa01.pesoG)


print(pessoa01.alturaCm) #Print da altura

