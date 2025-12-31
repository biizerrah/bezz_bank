class Cliente:
    def __init__(self,nome,cpf,profissao):

        self.nome = nome
        self.cpf = cpf
        self.relacao = profissao

    def __str__(self):
        return f"{self.nome} - (CPF: {self.cpf}) - (Cliente : {self.profissao})"
    

