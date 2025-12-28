
from .cliente import Cliente

class ContaBancaria:

    def __init__(self, titular: Cliente, num_conta:str):

        self.titular = titular
        self.__saldo = 0.0
        self.num_conta = num_conta

    def __str__(self):
        return f"(Conta: {self.num_conta})"

    def sacar():
        pass

    def depositar():
        pass

