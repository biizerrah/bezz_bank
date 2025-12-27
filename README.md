# 🏦🐮 Bezz Bank

> **Solidez e tecnologia em cada linha de código.**

Bem-vindo ao repositório do **Bezz Bank**, uma simulação de um sistema bancário desenvolvida em **Python**. 

Este projeto foi criado com foco educacional para demonstrar o domínio dos pilares da **Programação Orientada a Objetos (POO)** e boas práticas de arquitetura de software (Modularização).

---

## 🚀 Sobre o Projeto

O **Bezz Bank** simula operações financeiras essenciais através de um sistema backend organizado em pacotes. A lógica de negócio diferencia comportamentos entre tipos de contas (Corrente vs. Poupança) utilizando polimorfismo, garantindo que regras como limites de crédito e rendimentos sejam aplicadas corretamente.

### 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.x
* **Paradigma:** Orientação a Objetos (POO)
* **Arquitetura:** Modular (Separação entre `main` e pacote `bezz_core`)

### 📋 Destaques Técnicos

O código foi estruturado para atender a requisitos rigorosos de desenvolvimento:

* ✅ **Herança:** Uso de superclasse `ContaBancaria` e subclasses `ContaCorrente` e `ContaPoupanca`.
* ✅ **Polimorfismo:** Sobrescrita de métodos (Override) no método `sacar()`.
* ✅ **Encapsulamento:** Proteção de atributos sensíveis (como saldo) com modificadores de acesso privados e uso de *Getters/Setters*.
* ✅ **Tratamento de Erros:** Implementação de Exceções Personalizadas para regras de negócio.
* ✅ **Associação e Composição:** Relacionamento entre objetos (Clientes e Contas).

---

## 📂 Estrutura do Projeto

```text
projeto_bezz_bank/
│
├── main.py                 # Interface do usuário (Menu CLI)
│
└── bezz_core/              # Pacote com a Lógica de Negócio
    ├── __init__.py         # Gerenciador de exportações
    ├── conta_bancaria.py   # Superclasse Base
    ├── conta_corrente.py   # Lógica de Limite e Taxas
    ├── conta_poupanca.py   # Lógica de Rendimentos
    └── cliente.py          # Dados do titular
