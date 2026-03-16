# Modelo de Dados --- Rifa Digital

Este documento descreve o modelo de dados do sistema **Rifa Digital**,
incluindo entidades, atributos, relacionamentos, cardinalidades e regras
de integridade do banco de dados.

------------------------------------------------------------------------

# 1. Visão Geral

O banco de dados armazena informações relacionadas a:

-   campanhas de rifa
-   números disponíveis
-   participantes
-   reservas de números
-   pagamentos
-   sorteio da rifa

O modelo segue uma estrutura **relacional**, garantindo integridade e
consistência das informações.

------------------------------------------------------------------------

# 2. Diagrama Entidade‑Relacionamento

``` mermaid
erDiagram

RIFA ||--o{ NUMERO : possui
NUMERO ||--o{ RESERVA : reservado_em
COMPRADOR ||--o{ RESERVA : realiza
RESERVA ||--|| PAGAMENTO : gera
RIFA ||--|| SORTEIO : possui

RIFA {
  int id PK
  string nome
  string descricao
  decimal valor_numero
  int quantidade_numeros
  date data_sorteio
  string status
}

NUMERO {
  int id PK
  int numero
  string status
  int rifa_id FK
}

COMPRADOR {
  int id PK
  string nome
  string telefone
  string email
}

RESERVA {
  int id PK
  datetime data_reserva
  string status
  int numero_id FK
  int comprador_id FK
}

PAGAMENTO {
  int id PK
  decimal valor
  date data_pagamento
  string status
  int reserva_id FK
}

SORTEIO {
  int id PK
  date data_sorteio
  int numero_vencedor
  int rifa_id FK
}
```

------------------------------------------------------------------------

# 3. Entidades

## Rifa

Representa uma campanha de rifa criada por um organizador.

  Campo                Tipo      Obrigatório
  -------------------- --------- -------------
  id                   inteiro   sim
  nome                 texto     sim
  descricao            texto     sim
  valor_numero         decimal   sim
  quantidade_numeros   inteiro   sim
  data_sorteio         data      sim
  status               texto     sim

------------------------------------------------------------------------

## Número

Representa um número disponível em uma rifa.

  Campo     Tipo      Obrigatório
  --------- --------- -------------
  id        inteiro   sim
  numero    inteiro   sim
  status    texto     sim
  rifa_id   inteiro   sim

------------------------------------------------------------------------

## Comprador

Representa um participante da rifa.

  Campo      Tipo      Obrigatório
  ---------- --------- -------------
  id         inteiro   sim
  nome       texto     sim
  telefone   texto     sim
  email      texto     não

------------------------------------------------------------------------

## Reserva

Representa a reserva de um número antes da confirmação de pagamento.

  Campo          Tipo       Obrigatório
  -------------- ---------- -------------
  id             inteiro    sim
  data_reserva   datetime   sim
  status         texto      sim
  numero_id      inteiro    sim
  comprador_id   inteiro    sim

------------------------------------------------------------------------

## Pagamento

Representa o pagamento realizado para confirmar a compra.

  Campo            Tipo      Obrigatório
  ---------------- --------- -------------
  id               inteiro   sim
  valor            decimal   sim
  data_pagamento   data      sim
  status           texto     sim
  reserva_id       inteiro   sim

------------------------------------------------------------------------

## Sorteio

Representa o sorteio realizado ao final da rifa.

  Campo             Tipo      Obrigatório
  ----------------- --------- -------------
  id                inteiro   sim
  data_sorteio      data      sim
  numero_vencedor   inteiro   sim
  rifa_id           inteiro   sim

------------------------------------------------------------------------

# 4. Cardinalidades

  Relacionamento        Cardinalidade
  --------------------- ---------------
  Rifa → Número         1:N
  Número → Reserva      1:N
  Comprador → Reserva   1:N
  Reserva → Pagamento   1:1
  Rifa → Sorteio        1:1

------------------------------------------------------------------------

# 5. Regras de Integridade

-   Um número pertence a **uma única rifa**.
-   Um número só pode estar **reservado por um comprador por vez**.
-   Um pagamento deve estar associado a **uma reserva válida**.
-   Um número só pode ser marcado como **vendido após confirmação do
    pagamento**.
-   Cada rifa possui **apenas um sorteio**.

------------------------------------------------------------------------

# 6. Normalização

O modelo segue princípios da **Terceira Forma Normal (3FN)**.

## 1FN -- Primeira Forma Normal

-   Todos os atributos são atômicos.
-   Não existem grupos repetidos.

## 2FN -- Segunda Forma Normal

-   Todas as entidades dependem da chave primária completa.

## 3FN -- Terceira Forma Normal

-   Não existem dependências transitivas entre atributos.

------------------------------------------------------------------------

# 7. Índices Recomendados

Para melhorar o desempenho das consultas:

``` sql
CREATE INDEX idx_numero_rifa
ON numero(rifa_id);

CREATE INDEX idx_reserva_numero
ON reserva(numero_id);

CREATE INDEX idx_reserva_comprador
ON reserva(comprador_id);
```

------------------------------------------------------------------------

# 8. Evolução do Modelo

O modelo permite evoluções futuras, como:

-   múltiplos prêmios
-   histórico completo de reservas
-   integração com gateways de pagamento
-   autenticação de usuários
-   notificações automáticas
