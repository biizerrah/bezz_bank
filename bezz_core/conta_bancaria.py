
from .cliente import Cliente
from .historico import Historico

class ContaBancaria:

    def __init__(self, titular: Cliente, num_conta:str):

        self.titular = titular
        self._saldo = 0.0
        self.num_conta = num_conta
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"(Conta: {self.num_conta})"

    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            self.historico.adicionar_transacao(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado!")
        

    def sacar(self, valor):
        if valor <= self._saldo and valor > 0:
            self._saldo -= valor
            print(f"Saque no valor {valor} realizado!")
        else:
            print("Saldo Insuficiente!")

    def exibir_extrato(self):
        print(f"Cliente: {self.titular.nome}")
        self.historico.imprimir()
        print(f"Saldo Atual: R${self.saldo:.2f}\n")