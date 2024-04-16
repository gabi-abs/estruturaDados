class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_valor_lados(self, novo_valor_ladoA, novo_valor_ladoB):
        self.ladoA = novo_valor_ladoA
        self.ladoB = novo_valor_ladoB

    def retorna_valor_lados(self):
        return self.ladoA
        return self.ladoB

    def calcular_area(self):
       return self.ladoA * self.ladoB

    def calcular_perimetro(self):
        return 2 *(self.ladoA + self.ladoB)
    

    #############################


#Instanciando um objeto
retangulo01 = Retangulo(ladoA=2, ladoB=2)
print(retangulo01.ladoA)
print(retangulo01.ladoB)

# Mudando valor 
retangulo01.mudar_valor_lados(5,5)
print(retangulo01.ladoA)
print(retangulo01.ladoB)

# Retornando valores
print(retangulo01.retorna_valor_lados())

# Calculando a area
print(retangulo01.calcular_area())

# Calculando perimetro 
print(retangulo01.calcular_perimetro())





