
# Dicionário de Dados — Rifa Digital

Este documento apresenta o **Dicionário de Dados** do sistema **Rifa Digital**.

O dicionário de dados descreve detalhadamente os **campos das tabelas do banco de dados**, incluindo:

- nome do campo
- tipo de dado
- obrigatoriedade
- descrição
- relacionamento

Ele complementa o **Modelo Relacional** e o **Schema SQL**, fornecendo uma visão clara da estrutura dos dados.

---

# 1. Tabela RIFA

Armazena informações sobre cada campanha de rifa.

| Campo | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id_rifa | INT | Sim | Identificador único da rifa |
| titulo | VARCHAR(150) | Sim | Nome da rifa |
| descricao | TEXT | Não | Descrição da campanha |
| data_sorteio | DATE | Sim | Data do sorteio da rifa |
| valor_numero | DECIMAL(10,2) | Sim | Valor de cada número da rifa |
| quantidade_numeros | INT | Sim | Quantidade total de números disponíveis |
| status | VARCHAR(30) | Não | Status da rifa (ativa, encerrada, cancelada) |
| created_at | TIMESTAMP | Não | Data de criação da rifa |

---

# 2. Tabela NUMERO

Representa os números disponíveis para compra em cada rifa.

| Campo | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id_numero | INT | Sim | Identificador do número |
| numero | INT | Sim | Número da rifa |
| status | VARCHAR(20) | Não | Situação do número (disponível, reservado, pago) |
| id_rifa | INT | Sim | Identificador da rifa associada |

Relacionamento:

```
NUMERO.id_rifa → RIFA.id_rifa
```

---

# 3. Tabela PARTICIPANTE

Armazena os participantes da rifa.

| Campo | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id_participante | INT | Sim | Identificador do participante |
| nome | VARCHAR(150) | Sim | Nome completo do participante |
| telefone | VARCHAR(20) | Não | Telefone para contato |
| email | VARCHAR(150) | Não | Email do participante |
| created_at | TIMESTAMP | Não | Data de cadastro do participante |

---

# 4. Tabela RESERVA

Registra a reserva de um número por um participante.

| Campo | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id_reserva | INT | Sim | Identificador da reserva |
| data_reserva | DATETIME | Não | Data e hora da reserva |
| status | VARCHAR(20) | Não | Status da reserva (reservado, confirmado, cancelado) |
| id_numero | INT | Sim | Número reservado |
| id_participante | INT | Sim | Participante que realizou a reserva |

Relacionamentos:

```
RESERVA.id_numero → NUMERO.id_numero
RESERVA.id_participante → PARTICIPANTE.id_participante
```

---

# 5. Tabela PAGAMENTO

Armazena informações sobre o pagamento realizado para confirmar a reserva.

| Campo | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id_pagamento | INT | Sim | Identificador do pagamento |
| valor | DECIMAL(10,2) | Sim | Valor pago |
| data_pagamento | DATETIME | Não | Data e hora do pagamento |
| metodo_pagamento | VARCHAR(50) | Não | Forma de pagamento (PIX, cartão, dinheiro) |
| status | VARCHAR(20) | Não | Status do pagamento (pendente, aprovado, recusado) |
| id_reserva | INT | Sim | Reserva associada ao pagamento |

Relacionamento:

```
PAGAMENTO.id_reserva → RESERVA.id_reserva
```

---

# 6. Resumo das Tabelas

| Tabela | Descrição |
|------|------|
| RIFA | Campanhas de rifa |
| NUMERO | Números disponíveis para cada rifa |
| PARTICIPANTE | Pessoas que participam da rifa |
| RESERVA | Reserva de números pelos participantes |
| PAGAMENTO | Pagamentos realizados pelos participantes |

---

# 7. Fluxo de Dados do Sistema

O fluxo principal de dados no sistema ocorre da seguinte forma:

```
RIFA
 ↓
NUMERO
 ↓
RESERVA
 ↓
PAGAMENTO
```

Participantes interagem com o sistema realizando reservas de números e confirmando o pagamento.

---

# 8. Relação com a Modelagem de Dados

Este documento complementa os seguintes artefatos da arquitetura de dados:

```
MER (Modelo Conceitual)
        ↓
Modelo Relacional (Modelo Lógico)
        ↓
Schema SQL (Modelo Físico)
        ↓
Dicionário de Dados
```

O dicionário de dados fornece a descrição detalhada de cada campo do banco de dados.
