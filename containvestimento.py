class ContaInvestimento:

    def __init__(self, saldoInicial, taxaJuros ):
        self.saldoInicial = saldoInicial
        self.taxaJuros = taxaJuros

    def adicioneJuros(self):
     self.saldoInicial += (self.saldoInicial * self.taxaJuros)/100 

    #########################################E

contaPoupanca01 = ContaInvestimento(saldoInicial=1_000, taxaJuros=10)

print(contaPoupanca01.adicioneJuros())
print(contaPoupanca01.adicioneJuros())
print(contaPoupanca01.adicioneJuros())
print(contaPoupanca01.adicioneJuros())
print(contaPoupanca01.adicioneJuros())
print(contaPoupanca01.saldoInicial)
