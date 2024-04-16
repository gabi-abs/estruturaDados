class Macaco:
    def __init__(self, nome, estomago):
        self.nome = nome
        self.estomago = []

    def comer(self, alimento):
            self.estomago.append(alimento)
            
    def verEstomago(self):
        print(f"Estomago de {self.nome} = {self.estomago}")
    
    def digerir(self):
        self.estomago.clear()
      

########################################################
            
macaco01 = Macaco("Caco", "Acai")
macaco02 = Macaco("Caquinho", "ameixa")


macaco01.comer("Banana")
macaco02.comer("Acai")

macaco01.verEstomago()
macaco02.verEstomago()

macaco01.comer("Chocolate") 
macaco02.comer("Banana")

macaco01.verEstomago()
macaco02.verEstomago()

macaco01.comer(macaco02.nome) 
macaco02.comer(macaco01.nome)

macaco01.verEstomago()
macaco02.verEstomago()

macaco01.digerir()
macaco02.digerir()

macaco01.verEstomago()
macaco02.verEstomago()
