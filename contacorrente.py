class ContaCorrente:

    def __init__(self, numero_conta= "1", nome= "Gabriella", saldo= 0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor_deposito):
        self.saldo = valor_deposito

    def saque(self, valor_saque ):
       
       if valor_saque > self.saldo:
           print("Saldo insuficiente")

       else:
           self.saldo -= valor_saque
           print(f"Saque realizado. Saldo atual: {self.saldo}")

       

#######################################################

conta01 = ContaCorrente() 
    

conta01.alterarNome("João") 
print(f"Seu nome foi alterado para: {conta01.nome}")

print(f"Seu saldo atual é: {conta01.saldo}")

conta01.deposito(500) 
print(f"Seu saldo foi atualizado: {conta01.saldo}")

conta01.saque(20)

