# MER --- Modelo Entidade-Relacionamento Completo

Este documento apresenta o **Modelo Entidade‑Relacionamento (MER)**
completo do sistema **Rifa Digital**.

O objetivo é representar as **entidades principais do domínio**, seus
**atributos** e os **relacionamentos** entre elas.

------------------------------------------------------------------------

# Diagrama MER

``` mermaid
erDiagram

RIFA {
    int id
    string titulo
    string descricao
    decimal valor_numero
    int quantidade_numeros
    date data_sorteio
    string status
}

NUMERO {
    int id
    int numero
    string status
}

PARTICIPANTE {
    int id
    string nome
    string telefone
    string email
}

RESERVA {
    int id
    datetime data_reserva
    string status
}

PAGAMENTO {
    int id
    datetime data_pagamento
    decimal valor
    string status
}

SORTEIO {
    int id
    datetime data_sorteio
    int numero_vencedor
}

RIFA ||--o{ NUMERO : possui
NUMERO ||--o{ RESERVA : reservado
PARTICIPANTE ||--o{ RESERVA : realiza
RESERVA ||--|| PAGAMENTO : gera
RIFA ||--|| SORTEIO : realiza
```

------------------------------------------------------------------------

# Entidades

## Rifa

Representa uma campanha de rifa criada por um organizador.

Principais atributos:

-   id
-   titulo
-   descricao
-   valor_numero
-   quantidade_numeros
-   data_sorteio
-   status

------------------------------------------------------------------------

## Número

Representa um número individual pertencente a uma rifa.

Atributos:

-   id
-   numero
-   status

Status possíveis:

-   disponível
-   reservado
-   vendido

------------------------------------------------------------------------

## Participante

Representa o usuário que participa da rifa.

Atributos:

-   id
-   nome
-   telefone
-   email

------------------------------------------------------------------------

## Reserva

Representa a reserva temporária de um número por um participante.

Atributos:

-   id
-   data_reserva
-   status

------------------------------------------------------------------------

## Pagamento

Representa o pagamento associado a uma reserva.

Atributos:

-   id
-   data_pagamento
-   valor
-   status

------------------------------------------------------------------------

## Sorteio

Representa o sorteio realizado ao final da campanha.

Atributos:

-   id
-   data_sorteio
-   numero_vencedor

------------------------------------------------------------------------

# Relacionamentos

  Entidade       Relacionamento   Entidade
  -------------- ---------------- -----------
  Rifa           possui           Número
  Número         pode gerar       Reserva
  Participante   realiza          Reserva
  Reserva        gera             Pagamento
  Rifa           possui           Sorteio

------------------------------------------------------------------------

# Observações

Este modelo conceitual serve como base para:

-   modelo relacional
-   implementação SQL
-   definição das regras de integridade do banco

Ele também está diretamente relacionado aos documentos:

-   `modelo-relacional.md`
-   `schema-sql.md`
-   `dicionario-dados.md`
