from .conta_bancaria import ContaBancaria
from .excecoes import SaldoInsuficienteError

class ContaCorrente(ContaBancaria):

    def sacar(self,valor):

        taxa_saque = 2.0
        valor_total = valor + taxa_saque

        if valor > 0 and self._saldo >= valor_total:
            self._saldo -= valor_total

            self.historico.adicionar_transacao(f"Saque: -R${valor:.2f} (Taxa: R${taxa_saque:.2f})")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True
        else:
            raise SaldoInsuficienteError(self._saldo, valor_total)
        

