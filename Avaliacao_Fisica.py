class Cliente :  # GERA OS DADOS DO MEU CLIENTE
    def __init__(self, nome , idade, telefone, email):
        self._nome = nome
        self._idade = idade
        self._tefone = telefone
        self._email = email


    def __str__(self): 
        return f'  --> nome: {self._nome} - idade: {self._idade} Anos - telefone: {self._tefone} - emai: {self._email}'

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
        self.abdominal =  Abdôminal
        self.femural_medio =   Femural_Medio

    def __str__(self):
        return f'  --> Peso: {self.peso}kg - Altura: {self.altura} -  Subescapular {self.subscapular}mm - Triceps {self.triceps}mm - Peitoral {self.peitoral}mm - Axilar_Media {self.axilar_media}mm - Supra_Iliaca {self.supra_iliaca}mm - Abdôminal {self.abdominal}mm - Femural_Medio {self.femural_medio}mm '


#ProgramaPricipal


Vitor = Cliente('Vitor Barros', 26, '(22)997637516' , 'vitor-nf10@hotmail.com') 
Dados_Vitor = Avaliacao( 84 , 1.82, 8, 10 , 4, 12, 20 , 22 , 18 )



#Teste

print (Vitor)
print (Dados_Vitor)



#PASSOS
# 1° criei meus objetos 
# 2°Tenho que gerar os calculos 
# 3°Tenho que gerar todas as informçoes como persutal de gordura e imc na tela ( provavel que tenha que criar metodos )
#
#
#
#
