from bezz_core.conta_bancaria import ContaBancaria
from bezz_core.cliente import Cliente


cliente1 = Cliente("Tatiana Bezerra","000.444.555-77","V.I.P.")
conta1 = ContaBancaria(cliente1,"2222-5")

print(cliente1, conta1)