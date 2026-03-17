# Diagrama de Componentes --- Rifa Digital

Este documento apresenta o **Diagrama de Componentes UML** do sistema
**Rifa Digital**.

O objetivo é mostrar os principais **componentes do sistema** e como
eles se relacionam dentro da arquitetura.

O sistema segue uma arquitetura em camadas:

Usuário → Frontend → Backend / API → Banco de Dados

------------------------------------------------------------------------

# 1. Diagrama de Componentes

``` mermaid
flowchart LR

User[Usuário]

Frontend[Frontend<br>Interface Web]

Backend[Backend / API]

RifaService[Gerenciamento de Rifa]

NumeroService[Gerenciamento de Números]

PagamentoService[Processamento de Pagamentos]

SorteioService[Serviço de Sorteio]

DB[(Banco de Dados)]

User --> Frontend
Frontend --> Backend

Backend --> RifaService
Backend --> NumeroService
Backend --> PagamentoService
Backend --> SorteioService

RifaService --> DB
NumeroService --> DB
PagamentoService --> DB
SorteioService --> DB
```

------------------------------------------------------------------------

# 2. Componentes do Sistema

## Frontend

Responsável pela interface com o usuário.

Funções principais:

-   exibir informações da rifa
-   mostrar números disponíveis
-   permitir seleção de números
-   exibir resultado do sorteio

Tecnologias possíveis:

-   HTML
-   CSS
-   JavaScript
-   React

------------------------------------------------------------------------

## Backend / API

Responsável pela lógica de negócio do sistema.

Principais responsabilidades:

-   validar dados
-   gerenciar rifas
-   controlar números disponíveis
-   registrar compradores
-   registrar pagamentos
-   executar sorteio

Tecnologias possíveis:

-   Node.js
-   Python
-   Java

------------------------------------------------------------------------

# 3. Serviços Internos

## Rifa Service

Responsável por:

-   criar campanhas de rifa
-   configurar quantidade de números
-   definir data do sorteio

------------------------------------------------------------------------

## Numero Service

Responsável por:

-   gerenciar números da rifa
-   verificar disponibilidade
-   atualizar status dos números

------------------------------------------------------------------------

## Pagamento Service

Responsável por:

-   registrar pagamentos
-   confirmar venda de números

------------------------------------------------------------------------

## Sorteio Service

Responsável por:

-   executar sorteio
-   registrar número vencedor
-   divulgar resultado

------------------------------------------------------------------------

# 4. Banco de Dados

Responsável por armazenar:

-   rifas
-   números da rifa
-   compradores
-   pagamentos
-   resultados de sorteio

------------------------------------------------------------------------

# 5. Observações

O diagrama de componentes ajuda a compreender:

-   a organização interna do sistema
-   a separação de responsabilidades
-   a estrutura da arquitetura

Ele complementa:

-   **Diagrama de Casos de Uso**
-   **Diagrama de Classes**
-   **Diagrama de Sequência**
-   **Arquitetura do Sistema**
