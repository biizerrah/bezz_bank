import sys
from bezz_core.cliente import Cliente
from bezz_core.conta_corrente import ContaCorrente
from bezz_core.excecoes import SaldoInsuficienteError

def limpar_tela():
    
    print("\n" + "="*50 + "\n")

def ler_valor_monetario(mensagem):
   
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("❌ Erro: Por favor, insira apenas números (ex: 100.50).")

def iniciar_sistema():
    print("🐂 --- BEM-VINDO AO BEZZ BANK --- 🐂")
    print("Vamos configurar sua conta inicial.\n")

    
    nome = input("Digite o nome do titular: ")
    cpf = input("Digite o CPF: ")
    profissao = input("Digite a profissão: ")

    cliente = Cliente(nome, cpf, profissao)
    
    conta = ContaCorrente(cliente, "1001-BR")

    print(f"\n✅ Conta criada com sucesso para {cliente.nome}!")
    
    while True:
        limpar_tela()
        print(f"Titular: {conta.titular.nome} | Conta: {conta.num_conta}")
        print("--- MENU DE OPERAÇÕES ---")
        print("1. 📥 Depositar")
        print("2. 💸 Sacar")
        print("3. 📜 Ver Extrato")
        print("4. 💰 Consultar Saldo")
        print("0. ❌ Sair")
        
        opcao = input("\nEscolha uma opção: ")

        
        if opcao == "1":
        
            valor = ler_valor_monetario("Valor a depositar: R$ ")
            try:
                conta.depositar(valor)
            except ValueError as e:
                print(f"⚠️ {e}")
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            
            valor = ler_valor_monetario("Valor a sacar: R$ ")
            try:
                conta.sacar(valor)
                
            except SaldoInsuficienteError as erro:
                
                print(f"❌ OPERAÇÃO NEGADA: {erro}")
                print("💡 Dica: Lembre-se que existe uma taxa de R$ 2,00 por saque.")
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")
            
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            
            conta.exibir_extrato()
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            
            print(f"\n💰 Saldo Disponível: R$ {conta.saldo:.2f}")
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            print("\nObrigado por usar o Bezz Bank! Até a próxima. 🐂")
            break

        else:
            print("❌ Opção inválida! Tente novamente.")
            input("Pressione ENTER...")

if __name__ == "__main__":
    try:
        iniciar_sistema()
    except KeyboardInterrupt:
        print("\n\nOperação interrompida pelo usuário. Saindo...")
        sys.exit(0)