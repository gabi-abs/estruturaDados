class Funcionario:
    def __init__(self, nome="Gabriella", salario=1_200):
        self.nome = nome
        self.salario = salario

    
    def get_nome(self):
       print(f"{self.nome}")


    def get_salario(self):
        print(f"{self.salario}")

    def aumentarSalario(self, quantos_porcento):
     self.salario += (quantos_porcento * self.salario)/100



########################################
        
funcionario01 = Funcionario()

funcionario01.get_nome()
funcionario01.get_salario()
funcionario01.aumentarSalario(10)

print(funcionario01.salario)