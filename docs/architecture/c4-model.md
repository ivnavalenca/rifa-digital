# C4 Model --- Arquitetura do Sistema

Este documento apresenta a arquitetura do sistema **Rifa Digital**
utilizando o **modelo C4**, que descreve o sistema em diferentes níveis
de abstração.

O modelo C4 é dividido em:

-   Context Diagram
-   Container Diagram
-   Component Diagram

------------------------------------------------------------------------

# 1. Context Diagram

O diagrama de contexto mostra como o sistema se relaciona com usuários
externos.

``` mermaid
flowchart LR

Participante[Participante] --> Sistema[Rifa Digital]
Organizador[Organizador] --> Sistema

Sistema --> Banco[(Banco de Dados)]
Sistema --> Sorteio[Processo de Sorteio]
```

## Descrição

O sistema é utilizado por dois tipos de usuários:

### Participante

Responsável por:

-   visualizar rifas
-   escolher números
-   realizar pagamento
-   acompanhar resultados

### Organizador

Responsável por:

-   criar rifas
-   gerenciar números
-   acompanhar vendas
-   realizar sorteio

------------------------------------------------------------------------

# 2. Container Diagram

O diagrama de containers apresenta os principais componentes técnicos do
sistema.

``` mermaid
flowchart LR

User[Usuário]

Frontend[Interface Web]
Backend[Aplicação Rifa Digital]
Database[(Banco de Dados)]

User --> Frontend
Frontend --> Backend
Backend --> Database
```

## Containers
```
  -----------------------------------------------------------------------
  Container                           Descrição
  ----------------------------------- -----------------------------------
  Frontend                            Interface web utilizada pelos
                                      usuários

  Backend                             Serviço responsável pela lógica de
                                      negócio

  Database                            Banco de dados responsável pela
                                      persistência das informações
  -----------------------------------------------------------------------
```
------------------------------------------------------------------------

# 3. Component Diagram

O diagrama de componentes detalha os módulos internos da aplicação.

``` mermaid
flowchart LR

API[API da Aplicação]

Rifa[Gestão de Rifas]
Numero[Gestão de Números]
Reserva[Gestão de Reservas]
Pagamento[Gestão de Pagamentos]
Sorteio[Processo de Sorteio]

Database[(Banco de Dados)]

API --> Rifa
API --> Numero
API --> Reserva
API --> Pagamento
API --> Sorteio

Rifa --> Database
Numero --> Database
Reserva --> Database
Pagamento --> Database
Sorteio --> Database
```

## Componentes
```
  Componente             Responsabilidade
  ---------------------- ----------------------------------
  Gestão de Rifas        criação e gerenciamento de rifas
  Gestão de Números      controle dos números disponíveis
  Gestão de Reservas     reserva temporária de números
  Gestão de Pagamentos   confirmação de pagamentos
  Sorteio                definição do número vencedor
```
------------------------------------------------------------------------

# 4. Benefícios da Arquitetura

A arquitetura adotada permite:

-   separação clara de responsabilidades
-   manutenção facilitada
-   escalabilidade do sistema
-   organização da lógica de negócio
