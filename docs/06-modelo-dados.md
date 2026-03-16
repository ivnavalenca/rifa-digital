# Modelo de Dados

Este documento descreve o modelo de dados do sistema **Rifa Digital**, apresentando as entidades principais e seus relacionamentos.

O modelo de dados representa as informações necessárias para o funcionamento do sistema, incluindo rifas, números, compradores e pagamentos.

---

# 1. Visão Geral do Modelo

O sistema armazena informações sobre:

- rifas criadas
- números disponíveis
- compradores
- pagamentos
- resultados do sorteio

Principais entidades do sistema:

- Rifa
- Numero
- Comprador
- Pagamento
- Sorteio

---

# 2. Entidades do Sistema

## 2.1 Rifa

Representa uma campanha de rifa criada no sistema.

Atributos:

id  
nome  
descricao  
valor_numero  
quantidade_numeros  
data_sorteio  
status

Relacionamentos:

Uma rifa possui vários números.

---

## 2.2 Numero

Representa um número disponível na rifa.

Atributos:

id  
numero  
status  
rifa_id  
comprador_id

Status possíveis:

disponivel  
reservado  
vendido

Relacionamentos:

Um número pertence a uma rifa.

Um número pode estar associado a um comprador.

---

## 2.3 Comprador

Representa o participante que compra um número da rifa.

Atributos:

id  
nome  
telefone  
email

Relacionamentos:

Um comprador pode possuir um ou mais números da rifa.

---

## 2.4 Pagamento

Representa o pagamento realizado pelo comprador.

Atributos:

id  
valor  
data_pagamento  
status  
numero_id

Relacionamentos:

Um pagamento está associado a um número da rifa.

---

## 2.5 Sorteio

Representa o resultado do sorteio da rifa.

Atributos:

id  
rifa_id  
numero_sorteado  
data_sorteio

Relacionamentos:

Um sorteio está associado a uma rifa.

---

# 3. Relacionamentos entre Entidades

Rifa 1 --- N Numero

Numero 1 --- 1 Comprador

Numero 1 --- 1 Pagamento

Rifa 1 --- 1 Sorteio

---

# 4. Diagrama do Modelo de Dados

```mermaid
erDiagram

RIFA ||--o{ NUMERO : possui
NUMERO }o--|| COMPRADOR : pertence
NUMERO ||--|| PAGAMENTO : possui
RIFA ||--|| SORTEIO : gera

RIFA {
  int id
  string nome
  string descricao
  float valor_numero
  int quantidade_numeros
  date data_sorteio
}

NUMERO {
  int id
  int numero
  string status
  int rifa_id
  int comprador_id
}

COMPRADOR {
  int id
  string nome
  string telefone
  string email
}

PAGAMENTO {
  int id
  float valor
  date data_pagamento
  string status
  int numero_id
}

SORTEIO {
  int id
  int rifa_id
  int numero_sorteado
  date data_sorteio
}
