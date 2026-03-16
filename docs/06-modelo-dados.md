# Modelo de Dados

Este documento descreve o modelo de dados do sistema **Rifa Digital**,
apresentando as entidades principais e seus relacionamentos.

O modelo de dados representa as informações necessárias para o
funcionamento do sistema, incluindo rifas, números, compradores e
pagamentos.

------------------------------------------------------------------------

# 1. Visão Geral do Modelo

O sistema armazena informações sobre:

-   rifas criadas
-   números disponíveis
-   compradores
-   pagamentos
-   resultados do sorteio

Principais entidades do sistema:

-   Rifa
-   Numero
-   Comprador
-   Pagamento
-   Sorteio

------------------------------------------------------------------------

# 2. Entidades do Sistema

## 2.1 Rifa

Representa uma campanha de rifa criada no sistema.

**Atributos:**

-   id\
-   nome\
-   descricao\
-   valor_numero\
-   quantidade_numeros\
-   data_sorteio\
-   status

**Relacionamentos:**

Uma rifa possui vários números.

------------------------------------------------------------------------

## 2.2 Numero

Representa um número disponível na rifa.

**Atributos:**

-   id\
-   numero\
-   status\
-   rifa_id\
-   comprador_id

**Status possíveis:**

-   disponivel\
-   reservado\
-   vendido

**Relacionamentos:**

Um número pertence a uma rifa.

Um número pode estar associado a um comprador.

------------------------------------------------------------------------

## 2.3 Comprador

Representa o participante que compra um número da rifa.

**Atributos:**

-   id\
-   nome\
-   telefone\
-   email

**Relacionamentos:**

Um comprador pode possuir um ou mais números da rifa.

------------------------------------------------------------------------

## 2.4 Pagamento

Representa o pagamento realizado pelo comprador.

**Atributos:**

-   id\
-   valor\
-   data_pagamento\
-   status\
-   numero_id

**Relacionamentos:**

Um pagamento está associado a um número da rifa.

------------------------------------------------------------------------

## 2.5 Sorteio

Representa o resultado do sorteio da rifa.

**Atributos:**

-   id\
-   rifa_id\
-   numero_sorteado\
-   data_sorteio

**Relacionamentos:**

Um sorteio está associado a uma rifa.

------------------------------------------------------------------------

# 3. Relacionamentos entre Entidades

Rifa 1 --- N Numero\
Numero 1 --- 1 Comprador\
Numero 1 --- 1 Pagamento\
Rifa 1 --- 1 Sorteio

------------------------------------------------------------------------

# 4. Diagrama do Modelo de Dados



------------------------------------------------------------------------

# 5. Regras Importantes do Modelo

-   Cada número pertence a apenas uma rifa.
-   Cada número pode ser vendido apenas uma vez.
-   Um pagamento confirma a venda de um número.
-   O sorteio define o número vencedor da rifa.

------------------------------------------------------------------------

# 6. Observações

O modelo de dados foi projetado para garantir integridade das
informações e evitar inconsistências durante o processo de compra de
números da rifa.
