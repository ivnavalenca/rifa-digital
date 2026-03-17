# Modelo Relacional --- Rifa Digital

Este documento apresenta o **Modelo Relacional** do sistema **Rifa
Digital**.

O modelo relacional é derivado do **Modelo Entidade‑Relacionamento
(MER)** e descreve como as entidades do domínio são transformadas em
**tabelas relacionais**.

Cada tabela possui:

-   chave primária (PK)
-   chaves estrangeiras (FK)
-   atributos que representam os dados do sistema

------------------------------------------------------------------------

# Visão Geral do Modelo Relacional

``` mermaid
erDiagram

RIFA {
  int id PK
  string titulo
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

PARTICIPANTE {
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
  int participante_id FK
}

PAGAMENTO {
  int id PK
  datetime data_pagamento
  decimal valor
  string status
  int reserva_id FK
}

SORTEIO {
  int id PK
  datetime data_sorteio
  int numero_vencedor
  int rifa_id FK
}

RIFA ||--o{ NUMERO : possui
NUMERO ||--o{ RESERVA : reservado
PARTICIPANTE ||--o{ RESERVA : realiza
RESERVA ||--|| PAGAMENTO : gera
RIFA ||--|| SORTEIO : possui
```

------------------------------------------------------------------------

# Tabelas do Modelo Relacional

## Tabela RIFA

  Campo                Tipo      Descrição
  -------------------- --------- -----------------------------
  id                   PK        Identificador da rifa
  titulo               VARCHAR   Nome da campanha
  descricao            TEXT      Descrição da rifa
  valor_numero         DECIMAL   Valor de cada número
  quantidade_numeros   INT       Quantidade total de números
  data_sorteio         DATE      Data do sorteio
  status               VARCHAR   Status da rifa

------------------------------------------------------------------------

## Tabela NUMERO

  Campo     Tipo      Descrição
  --------- --------- ----------------------------------
  id        PK        Identificador do número
  numero    INT       Número da rifa
  status    VARCHAR   disponível / reservado / vendido
  rifa_id   FK        Referência para tabela RIFA

------------------------------------------------------------------------

## Tabela PARTICIPANTE

  Campo      Tipo      Descrição
  ---------- --------- -------------------------------
  id         PK        Identificador do participante
  nome       VARCHAR   Nome do participante
  telefone   VARCHAR   Telefone
  email      VARCHAR   Email

------------------------------------------------------------------------

## Tabela RESERVA

  Campo             Tipo       Descrição
  ----------------- ---------- --------------------------
  id                PK         Identificador da reserva
  data_reserva      DATETIME   Data da reserva
  status            VARCHAR    Status da reserva
  numero_id         FK         Número reservado
  participante_id   FK         Participante

------------------------------------------------------------------------

## Tabela PAGAMENTO

  Campo            Tipo       Descrição
  ---------------- ---------- ----------------------------
  id               PK         Identificador do pagamento
  data_pagamento   DATETIME   Data do pagamento
  valor            DECIMAL    Valor pago
  status           VARCHAR    Status do pagamento
  reserva_id       FK         Reserva associada

------------------------------------------------------------------------

## Tabela SORTEIO

  Campo             Tipo       Descrição
  ----------------- ---------- --------------------------
  id                PK         Identificador do sorteio
  data_sorteio      DATETIME   Data do sorteio
  numero_vencedor   INT        Número sorteado
  rifa_id           FK         Rifa associada

------------------------------------------------------------------------

# Regras de Integridade

O modelo relacional garante:

-   integridade referencial entre tabelas
-   consistência dos dados
-   rastreabilidade entre rifa, números e participantes

Principais regras:

-   um número pertence a apenas **uma rifa**
-   um participante pode reservar **vários números**
-   cada reserva pode gerar **um pagamento**
-   cada rifa possui **um sorteio final**

------------------------------------------------------------------------

# Relacionamento com Outros Documentos

Este documento se conecta diretamente com:

-   `conceptual/mer.md` --- modelo conceitual
-   `physical/schema-sql.md` --- implementação SQL
-   `dictionary/dicionario-dados.md` --- descrição dos campos

O modelo relacional serve como base para a **implementação do banco de
dados**.
