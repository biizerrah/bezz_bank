class Cliente:
    def __init__(self,nome,cpf,relacao):

        self.nome = nome
        self.cpf = cpf
        self.relacao = relacao

    def __str__(self):
        return f"{self.nome} - (CPF: {self.cpf}) - (Cliente : {self.relacao})"
    

