class bicicleta:
    def __init__(self, ano,cor,tamanho,marca,situacao):
        self.ano = ano
        self.cor = cor
        self.tamanho = tamanho
        self.marca = marca
        self.situacao = situacao

    def MudaCor(self,cor):
        self.cor = cor
        return self.cor
    def BuscaSituacao(self):
        return self.situacao
    def AlterSituacao(self,novaSituacao):
        self.situacao = novaSituacao
        return self
    def __str__(self) -> str:
        return f"{__class__.__name__}{self.ano, self.situacao, self.tamanho, self.cor, self.marca}"
Bike = bicicleta(2024,'Vermelha',26,'Monark','Nova')
print('Bike',Bike.MudaCor('Azul'))
print('Bike',Bike.BuscaSituacao())
Bike.AlterSituacao('Usada')
print('Bike',Bike.BuscaSituacao())
print('Bike',Bike)