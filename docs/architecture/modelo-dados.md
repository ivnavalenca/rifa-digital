# Modelo de Dados --- Rifa Digital

Este documento apresenta o modelo de dados do sistema **Rifa Digital**,
descrevendo as principais entidades e relacionamentos utilizados para
armazenar informações da aplicação.

------------------------------------------------------------------------

# 1. Entidades do Sistema

## Rifa

Representa uma campanha de rifa criada por um organizador.

Campos principais:

-   id
-   nome
-   descricao
-   valor_numero
-   quantidade_numeros
-   data_sorteio
-   status

------------------------------------------------------------------------

## Número

Representa um número disponível na rifa.

Campos principais:

-   id
-   numero
-   status (disponível, reservado, vendido)
-   rifa_id
-   comprador_id

------------------------------------------------------------------------

## Comprador

Representa o participante que compra um número da rifa.

Campos principais:

-   id
-   nome
-   telefone
-   email

------------------------------------------------------------------------

## Pagamento

Representa o pagamento associado a um número da rifa.

Campos principais:

-   id
-   data_pagamento
-   valor
-   status
-   numero_id

------------------------------------------------------------------------

# 2. Relacionamentos

-   Uma **rifa** possui vários **números**
-   Um **número** pertence a uma **rifa**
-   Um **número** pode estar associado a um **comprador**
-   Um **pagamento** está associado a um **número**

------------------------------------------------------------------------

# 3. Diagrama Conceitual Simplificado

RIFA\
↓\
NUMERO\
↓\
COMPRADOR\
↓\
PAGAMENTO

------------------------------------------------------------------------

# 4. Regras de Integridade

-   Cada número pertence a apenas uma rifa.
-   Um número só pode ser vendido uma vez.
-   Um pagamento deve estar associado a um número válido.
-   Um número só pode ser marcado como vendido após confirmação do
    pagamento.

------------------------------------------------------------------------

# 5. Considerações

O modelo de dados foi projetado para garantir consistência das
informações e facilitar a implementação das funcionalidades do sistema.
