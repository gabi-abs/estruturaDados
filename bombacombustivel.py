class BombaCombustivel:
    
    def __init__(self, tipoCombustivel="gasolina", valorLitroRs=6, quantidadeCombustivelL=0, valorPagoPorLitro=0, quantidadeCombustivelTotal=50):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitroRs = valorLitroRs
        self.quantidadeCombustivelL = quantidadeCombustivelL
        self.valorPagoPorLitro = valorPagoPorLitro
        self.quantidadeCombustivelTotal = quantidadeCombustivelTotal

    def abastecerPorValor(self, valorEmReal):
        self.quantidadeCombustivelL = (valorEmReal / self.valorLitroRs) 
        print(f" A quantidade em litros colocado no veículo é: : {self.quantidadeCombustivelL}")

        self.quantidadeCombustivelTotal -= self.quantidadeCombustivelL
        print(f" Combustível restante na bomba:  {self.quantidadeCombustivelTotal}")


    def abastecerPorLitro(self, quantidadeLitro):
       self.valorPagoPorLitro = (self.valorLitroRs * quantidadeLitro)
       print(f"Valor a ser pago pelo Litro: {self.valorPagoPorLitro}")


    def alterarValor(self, novoValorLitro):
        self.valorLitroRs = novoValorLitro
        print(f"Novo valor do litro: {self.valorLitroRs}")


    def alterarCombustivel(self, alteraTipoCombustivel):
        self.tipoCombustivel = alteraTipoCombustivel
        print(f" Novo tipo de combustível: {self.tipoCombustivel}")


    def alterarQuantidadeCombustivel(self, alteraQuantidadeTotalBomba):
        self.quantidadeCombustivelTotal = alteraQuantidadeTotalBomba
        print(f"Quantidade de combustivel restante na bomba: {self.quantidadeCombustivelTotal}")

###########################################################################
        
carro01 = BombaCombustivel()

carro01.abastecerPorValor(20)

carro01.abastecerPorLitro(3.33)

carro01.alterarValor(7)

carro01.alterarCombustivel("Gás")

carro01.alterarQuantidadeCombustivel(20)