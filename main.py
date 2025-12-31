from bezz_core.conta_bancaria import ContaBancaria
from bezz_core.conta_corrente import ContaCorrente
from bezz_core.cliente import Cliente


def rodar_teste():
    print("=== 🐂 INICIANDO SISTEMA BEZZ BANK ===")

    tatiana = Cliente("Tatiana Bezerra", "000.000.000-00", "Conta Básica")
    print(f"   Cliente cadastrado: {tatiana}")

    conta_tati = ContaBancaria(tatiana, "0000-9")
    print(f"   Conta {conta_tati.num_conta} pertence a: {conta_tati.titular.nome}")

    print(f"\n3. Saldo Inicial: R${conta_tati.saldo:.2f}")

    conta_tati.depositar(1000)
    print(f"   Saldo pós-depósito: R${conta_tati.saldo:.2f}")

    conta_tati.sacar(200)
    print(f"   Saldo Final: R${conta_tati.saldo:.2f}")

    print("======================")
    print("CONTA CORRENTE")
    print("======================")

    conta_cc = ContaCorrente(tatiana, "0002-B")
    
    print("Depositando R$100,00 na Conta Corrente...")
    conta_cc.depositar(100)

    conta_cc.sacar(10) 
    
    print(f"Saldo Final CC: R${conta_cc.saldo:.2f}")

    conta_cc.taxa_manutencao()
    print(f"Saldo após manutenção: R${conta_cc.saldo:.2f}")

if __name__ == "__main__":
    rodar_teste()