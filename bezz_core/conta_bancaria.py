
from .cliente import Cliente

class ContaBancaria:

    def __init__(self, titular: Cliente, num_conta:str):

        self.titular = titular
        self._saldo = 0.0
        self.num_conta = num_conta

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"(Conta: {self.num_conta})"

    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print(f"Déposito no valor {valor} ralizado!")
        

    def sacar(self, valor):
        if valor <= self._saldo and valor > 0:
            self._saldo -= valor
            print(f"Saque no valor {valor} realizado!")
        else:
            print("Saldo Insuficiente!")

