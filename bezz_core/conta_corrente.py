from .conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):

    def sacar(self,valor):

        taxa_saque = 2.0
        valor_total = valor + taxa_saque

        if valor > 0 and self._saldo >= valor_total:
            self._saldo -= valor_total
            print(f"Saque de R${valor:.2f} (+ R${taxa_saque:.2f} de taxa) realizado!")
            print(f"Saldo restante: R${self._saldo:.2f}")
            return True
        else:
            print(f"Saldo insuficiente para saque + taxa (Total: R${valor_total:.2f})")
            return False
        
    def taxa_manutencao(self):
        taxa = 15.0
        self._saldo -= taxa
        print(f"Taxa de manutenção de R${taxa:.2f} debitada.")
