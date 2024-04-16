class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_valor):
        self.tamanho_lado = novo_valor

    def retorna_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado ** 2

    #########################
        
#Instanciando um objeto
quadrado01 = Quadrado(tamanho_lado= 5)
print(quadrado01.tamanho_lado)

# Mudando o valor do lado
quadrado01.mudar_valor_lado(10)
print(quadrado01.tamanho_lado)

# Retornando o valor
print(quadrado01.retorna_valor_lado())

# Área do quadrado
print(quadrado01.calcular_area())