# Data Architecture --- Rifa Digital

Este documento descreve a **arquitetura de dados** do sistema **Rifa
Digital**. O objetivo é apresentar como os dados são organizados,
modelados e armazenados dentro do sistema.

A arquitetura de dados conecta os seguintes elementos:

-   Modelo Conceitual (MER)
-   Modelo Lógico (Modelo Relacional)
-   Modelo Físico (SQL)
-   Banco de Dados

------------------------------------------------------------------------

# Visão Geral da Arquitetura de Dados

``` mermaid
flowchart LR

A[Requisitos]
B[Modelo Conceitual - MER]
C[Modelo Lógico - Modelo Relacional]
D[Modelo Físico - SQL]
E[(Banco de Dados)]

A --> B
B --> C
C --> D
D --> E
```

Cada nível representa um grau diferente de abstração da modelagem.

------------------------------------------------------------------------

# Componentes da Arquitetura de Dados

## Modelo Conceitual

Representa o domínio do sistema de forma conceitual.

Elementos principais:

-   entidades
-   atributos
-   relacionamentos
-   cardinalidades

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

## Modelo Lógico

Transforma o modelo conceitual em **estrutura relacional**.

Principais elementos:

-   tabelas
-   chaves primárias
-   chaves estrangeiras
-   relacionamentos

Documento relacionado:

`logical/modelo-relacional.md`

------------------------------------------------------------------------

## Modelo Físico

Define como os dados serão implementados no banco.

Inclui:

-   tipos de dados
-   constraints
-   índices
-   integridade referencial

Documento relacionado:

`physical/schema-sql.md`

------------------------------------------------------------------------

# Entidades Principais

A arquitetura de dados é baseada nas seguintes entidades:

  Entidade       Descrição
  -------------- ------------------------------------
  Rifa           Campanha de rifa criada no sistema
  Número         Número participante da rifa
  Participante   Usuário que compra números
  Reserva        Reserva temporária de número
  Pagamento      Registro de pagamento
  Sorteio        Resultado do sorteio da rifa

------------------------------------------------------------------------

# Integração com o Sistema

Os dados são utilizados por diferentes componentes do sistema:

``` mermaid
flowchart LR

Frontend[Frontend]
Backend[Backend/API]
Database[(Banco de Dados)]

Frontend --> Backend
Backend --> Database
```

O **backend** é responsável por:

-   validar dados
-   aplicar regras de negócio
-   persistir dados no banco

------------------------------------------------------------------------

# Dicionário de Dados

O dicionário de dados descreve cada campo presente nas tabelas.

Ele inclui:

-   nome do campo
-   tipo de dado
-   descrição
-   obrigatoriedade

Documento relacionado:

`dictionary/dicionario-dados.md`

------------------------------------------------------------------------

# Benefícios da Arquitetura de Dados

A definição clara da arquitetura de dados permite:

-   melhor organização da informação
-   maior consistência dos dados
-   facilidade de manutenção do banco
-   escalabilidade do sistema
