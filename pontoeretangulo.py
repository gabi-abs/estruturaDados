class Ponto:
    
    def __init__(self, x= 2, y= 2 ):
        self.x = x
        self.y = y
        

    def imprimirValoresPonto(self):
        print(f" Coordenadas: {self.x}, {self.y}")


class Retangulo:

    def __init__(self, largura, altura, verticeInferiorEsquerdo):
        self.largura = largura
        self.altura = altura 
        self.verticeInferiorEsquerdo = verticeInferiorEsquerdo


    def centroRetangulo(self):
         self.largura = self.largura/2 
         self.altura = self. altura / 2
         print(f" Centro do retangulo é: {self.largura, self.altura}")



#########################

retangulo01 = Retangulo(largura=4,altura=6, verticeInferiorEsquerdo="A")
retangulo02 = Retangulo(largura=8, altura=6, verticeInferiorEsquerdo="A")
retangulo08 = Retangulo(largura=4, altura=6, verticeInferiorEsquerdo="A")

retangulo01.centroRetangulo()

coordenada = Ponto()
coordenada.imprimirValoresPonto()