# Evolução do Modelo de Dados --- Rifa Digital

Este documento descreve a evolução da modelagem de dados do sistema
**Rifa Digital**, desde a análise de requisitos até a implementação
física do banco de dados.

A modelagem segue o processo clássico da **Engenharia de Banco de
Dados**:

1.  Modelo Conceitual --- MER\
2.  Modelo Lógico --- Modelo Relacional\
3.  Modelo Físico --- SQL\
4.  Banco de Dados Implementado

------------------------------------------------------------------------

# Processo de Modelagem de Dados

``` mermaid
flowchart TD

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

Cada etapa possui um nível diferente de abstração.

------------------------------------------------------------------------

# Modelo Conceitual (MER)

O **Modelo Entidade-Relacionamento (MER)** descreve os dados do sistema
de forma conceitual.

Ele representa:

-   entidades
-   atributos
-   relacionamentos
-   cardinalidades

Nesta etapa **não existem tabelas ou SQL**.

Principais entidades do sistema:

-   Rifa
-   Número
-   Participante
-   Reserva
-   Pagamento
-   Sorteio

Documento relacionado:

`conceptual/mer.md`

------------------------------------------------------------------------

# Modelo Lógico (Modelo Relacional)

O modelo relacional traduz o MER para uma estrutura baseada em
**tabelas**.

Transformações principais:

  MER              Modelo Relacional
  ---------------- -------------------
  Entidade         Tabela
  Atributo         Coluna
  Identificador    Chave Primária
  Relacionamento   Chave Estrangeira

Exemplo:

    RIFA(
     id,
     titulo,
     valor_numero,
     data_sorteio,
     status
    )

Documento relacionado:

`logical/modelo-relacional.md`

------------------------------------------------------------------------

# Modelo Físico (SQL)

O modelo físico define a implementação no banco de dados.

São definidos:

-   tipos de dados
-   constraints
-   chaves estrangeiras
-   índices

Exemplo:

``` sql
CREATE TABLE rifa (
 id SERIAL PRIMARY KEY,
 titulo VARCHAR(150) NOT NULL,
 valor_numero DECIMAL(10,2),
 data_sorteio DATE,
 status VARCHAR(20)
);
```

Documento relacionado:

`physical/schema-sql.md`

------------------------------------------------------------------------

# Dicionário de Dados

O **Dicionário de Dados** documenta cada campo do banco.

Ele descreve:

-   nome da coluna
-   tipo
-   descrição
-   obrigatoriedade
-   relacionamentos

Documento relacionado:

`dictionary/dicionario-dados.md`

------------------------------------------------------------------------

# Visão Geral da Arquitetura de Dados

``` mermaid
flowchart LR

REQ[Requisitos]
MER[MER]
REL[Modelo Relacional]
SQL[SQL]
DB[(Banco de Dados)]

REQ --> MER
MER --> REL
REL --> SQL
SQL --> DB
```

------------------------------------------------------------------------

# Benefícios dessa abordagem

Separar os modelos permite:

-   melhor entendimento do domínio
-   redução de erros de modelagem
-   rastreabilidade entre requisitos e banco
-   maior qualidade na estrutura de dados
