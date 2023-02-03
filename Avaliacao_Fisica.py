class Cliente :  # GERA OS DADOS DO MEU CLIENTE
    def __init__(self, nome , idade, telefone, email):
        self._nome = nome
        self._idade = idade
        self._tefone = telefone
        self._email = email


    def __str__(self): 
        return f'  --> nome: {self._nome} - idade: {self._idade} Anos - telefone: {self._tefone} - email: {self._email}'

class Avaliacao: # GERA OS DADOS DA AVALIAÇÂO DO MEU CLIENTE
    def __init__(self, peso, altura, Subescapular, Triceps, Peitoral, 
    Axilar_Media, Supra_Iliaca, Abdôminal, Femural_Medio):
        self.peso = peso
        self.altura = altura
        self.subscapular = Subescapular
        self.triceps = Triceps
        self.peitoral = Peitoral
        self.axilar_media = Axilar_Media
        self.supra_iliaca = Supra_Iliaca
        self.abdominal = Abdôminal
        self.femural_medio =  Femural_Medio
        self.soma_dobra = Subescapular + Triceps + Peitoral + Axilar_Media + Supra_Iliaca + Abdôminal + Femural_Medio

    def Imc (self): # CAlcular o IMC
        self.imc = self.peso / self.altura ** 2
        return f'IMC : {self.imc:.2f}'

    def __str__(self):
        return f'  --> Peso: {self.peso}kg - Altura: {self.altura} - \n' \
               f' Subescapular {self.subscapular}mm - Triceps {self.triceps}mm -' \
               f' Peitoral {self.peitoral}mm - Axilar_Media {self.axilar_media}mm - \n' \
               f' Supra_Iliaca {self.supra_iliaca}mm - Abdôminal {self.abdominal}mm - Femural_Medio {self.femural_medio}mm '

    def calcula_gordura(self):
        dc = 1.112 - 0.00043499 * (self.soma_dobra) + 0.00000055 * (self.soma_dobra)*2 - 0.00028826 * (22)
        Percentual_de_gordura = (495 / dc) - 450
        return f'Percentual De Gordura {Percentual_de_gordura:.2f} %'

#ProgramaPricipal


Vitor = Cliente('Vitor Barros', 33, '(22)997637516' , 'vitor-nf10@hotmail.com')
Dados_Vitor = Avaliacao( 70 , 1.82, 9, 12 , 5, 6, 9 , 14 , 16 )




#Teste

print (Vitor)
print (Dados_Vitor)
print(Dados_Vitor.Imc())
print(Dados_Vitor.calcula_gordura())



#PASSOS
# 1° criei meus objetos 
# 2°Tenho que gerar os calculos 
# 3°Tenho que gerar todas as informaçoes como % de gordura e imc na tela ( provavel que tenha que criar metodos )
# 4° usar o tkinter  para a interface grafica
#
#
#
