# 🏦🐮 Bezz Bank

> **Solidez e tecnologia em cada linha de código.**

Bem-vindo ao repositório do **Bezz Bank**, uma simulação de um sistema bancário desenvolvida em **Python**. 

Este projeto foi criado com foco educacional para demonstrar o domínio dos pilares da **Programação Orientada a Objetos (POO)** e boas práticas de arquitetura de software (Modularização).

---

## 🚀 Sobre o Projeto

O **Bezz Bank** simula operações financeiras essenciais através de um sistema backend organizado em pacotes, utilizando polimorfismo, garantindo que regras como saldo da conta, extrato, depositos e saques sejam aplicadas corretamente.

### 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.13
* **Paradigma:** Orientação a Objetos (POO)
* **Arquitetura:** Modular (Separação entre `main` e pacote `bezz_core`)

### 📋 Destaques Técnicos

O código foi estruturado para atender a requisitos rigorosos de desenvolvimento:

* ✅ **Herança:** Uso de superclasse `ContaBancaria` e a subclasse `ContaCorrente`.
* ✅ **Polimorfismo:** Sobrescrita de métodos (Override) no método `sacar()`.
* ✅ **Encapsulamento:** Proteção de atributos sensíveis (como saldo) com modificadores de acesso privados e uso de *Getters/Setters*.
* ✅ **Tratamento de Erros:** Implementação de Exceções Personalizadas para regras de negócio.
* ✅ **Associação e Composição:** Relacionamento entre objetos (Clientes e Contas).

---

## 📂 Estrutura do Projeto

```text
bezz_bank/
│
├── main.py                 # Interface do Sistema (Menu Interativo e Tratamento de Erros)
│
└── bezz_core/              # Pacote com a Lógica de Negócio (Core)
    ├── __init__.py         # Inicializador do pacote
    ├── cliente.py          # Classe Cliente (Associação)
    ├── conta_bancaria.py   # Superclasse Base (Lógica compartilhada)
    ├── conta_corrente.py   # Subclasse (Polimorfismo e Taxas)
    ├── historico.py        # Registro de Transações (Composição)
    └── excecoes.py         # Tratamento de Erros Personalizados