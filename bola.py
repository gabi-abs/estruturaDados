class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material


    def trocaCor(self, nova_cor):
      self.cor = nova_cor
    
    def mostraCor(self):
        print(self.cor)
       

       
# # # # # # # # # # # # # # # # # # # # # # # #        
       
bola01 = Bola(cor= "azul", circunferencia="5", material="plastico")

bola01.trocaCor("amarelo")

bola01.mostraCor()

