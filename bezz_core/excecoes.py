
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        mensagem = f"Saldo de R${saldo_atual:.2f} insuficiente para saque de R${valor_saque:.2f}"
        super().__init__(mensagem)