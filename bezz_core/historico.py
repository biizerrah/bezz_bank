from datetime import datetime

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.transacoes.append(f"[{data_hora}] {descricao}")

    def imprimir(self):
        print("\n----- EXTRATO BANCÁRIO -----")
        if not self.transacoes:
            print("Nenhuma movimentação recente.")
        else:
            for t in self.transacoes:
                print(t)
        print("-------------------------------")