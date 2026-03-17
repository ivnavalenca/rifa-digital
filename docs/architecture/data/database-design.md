# Database Design --- Rifa Digital

Este documento descreve o **design do banco de dados** do sistema **Rifa
Digital**, mostrando como a modelagem evolui do **MER (Modelo
Entidade‑Relacionamento)** até a implementação do banco utilizando
**SQL**.

O objetivo é apresentar de forma clara as etapas de modelagem de dados
utilizadas no projeto.

------------------------------------------------------------------------

# Visão Geral do Design do Banco

``` mermaid
flowchart LR

A[Requisitos do Sistema]
B[Modelo Conceitual - MER]
C[Modelo Lógico - Modelo Relacional]
D[Modelo Físico - SQL]
E[(Banco de Dados)]

A --> B
B --> C
C --> D
D --> E
```

Cada etapa representa um nível diferente de abstração na modelagem de
dados.

------------------------------------------------------------------------

# 1. Modelo Conceitual (MER)

O **Modelo Entidade‑Relacionamento** descreve o domínio do problema.

Entidades principais do sistema:

-   Rifa
-   Número
-   Participante
-   Reserva
-   Pagamento
-   Sorteio

Este modelo identifica:

-   entidades
-   atributos
-   relacionamentos
-   cardinalidades

Documento relacionado:

`conceptual/mer.md`

------------------------------------------------------------------------

# 2. Modelo Lógico (Modelo Relacional)

O modelo relacional transforma as entidades do MER em **tabelas**.

Regras principais de transformação:

  MER              Modelo Relacional
  ---------------- -------------------
  Entidade         Tabela
  Atributo         Coluna
  Identificador    Chave Primária
  Relacionamento   Chave Estrangeira

Exemplo simplificado:

    RIFA(
     id PK,
     titulo,
     descricao,
     valor_numero,
     data_sorteio
    )

    NUMERO(
     id PK,
     numero,
     status,
     rifa_id FK
    )

Documento relacionado:

`logical/modelo-relacional.md`

------------------------------------------------------------------------

# 3. Modelo Físico (SQL)

O modelo físico representa a implementação real no banco de dados.

Exemplo de criação das tabelas:

``` sql
CREATE TABLE rifa (
 id SERIAL PRIMARY KEY,
 titulo VARCHAR(150) NOT NULL,
 descricao TEXT,
 valor_numero DECIMAL(10,2),
 data_sorteio DATE
);

CREATE TABLE participante (
 id SERIAL PRIMARY KEY,
 nome VARCHAR(120),
 telefone VARCHAR(20),
 email VARCHAR(120)
);

CREATE TABLE numero (
 id SERIAL PRIMARY KEY,
 numero INTEGER,
 status VARCHAR(20),
 rifa_id INTEGER REFERENCES rifa(id),
 participante_id INTEGER REFERENCES participante(id)
);
```

Documento relacionado:

`physical/schema-sql.md`

------------------------------------------------------------------------

# 4. Integridade dos Dados

O banco foi projetado para garantir:

-   integridade referencial
-   consistência dos dados
-   controle de relacionamentos

Exemplos de regras:

-   um número pertence a apenas uma rifa
-   um número não pode ser vendido duas vezes
-   um pagamento deve estar associado a uma reserva válida

------------------------------------------------------------------------

# 5. Dicionário de Dados

O **dicionário de dados** documenta cada campo do banco.

Ele descreve:

-   nome da coluna
-   tipo de dado
-   descrição
-   obrigatoriedade
-   relacionamentos

Documento relacionado:

`dictionary/dicionario-dados.md`

------------------------------------------------------------------------

# Benefícios da Modelagem

Seguir esse processo de design traz vantagens importantes:

-   maior clareza na estrutura dos dados
-   facilidade de manutenção do banco
-   redução de erros de modelagem
-   melhor rastreabilidade entre requisitos e dados
