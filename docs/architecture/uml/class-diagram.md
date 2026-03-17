# Diagrama de Classes --- Rifa Digital

Este documento apresenta o **Diagrama de Classes UML** do sistema **Rifa
Digital**.

O diagrama descreve a estrutura das entidades principais do sistema e os
relacionamentos entre elas.

As classes foram derivadas do **modelo de dados do sistema** e das
funcionalidades descritas nos casos de uso.

------------------------------------------------------------------------

# 1. Diagrama de Classes

``` mermaid
classDiagram

class Rifa {
  +id: int
  +nome: string
  +descricao: string
  +valorNumero: decimal
  +quantidadeNumeros: int
  +dataSorteio: date
  +status: string
}

class Numero {
  +id: int
  +numero: int
  +status: string
}

class Comprador {
  +id: int
  +nome: string
  +telefone: string
  +email: string
}

class Pagamento {
  +id: int
  +dataPagamento: datetime
  +valor: decimal
  +status: string
}

Rifa "1" --> "many" Numero : possui
Numero "0..1" --> "1" Comprador : reservado_por
Numero "1" --> "0..1" Pagamento : pagamento
```

------------------------------------------------------------------------

# 2. Descrição das Classes

## Rifa

Representa uma **campanha de rifa** criada por um organizador.

Atributos principais:

-   id
-   nome
-   descricao
-   valorNumero
-   quantidadeNumeros
-   dataSorteio
-   status

Responsabilidades:

-   armazenar informações da campanha
-   controlar quantidade de números
-   registrar data do sorteio

------------------------------------------------------------------------

## Numero

Representa um **número disponível na rifa**.

Atributos:

-   id
-   numero
-   status (disponível, reservado, vendido)

Responsabilidades:

-   identificar número da rifa
-   controlar estado de venda

------------------------------------------------------------------------

## Comprador

Representa o **participante da rifa**.

Atributos:

-   id
-   nome
-   telefone
-   email

Responsabilidades:

-   identificar o participante
-   associar participante a um número reservado

------------------------------------------------------------------------

## Pagamento

Representa o **pagamento realizado por um participante**.

Atributos:

-   id
-   dataPagamento
-   valor
-   status

Responsabilidades:

-   registrar pagamento
-   confirmar venda do número

------------------------------------------------------------------------

# 3. Relacionamentos

## Rifa → Numero

Uma **rifa possui vários números**.

Cardinalidade:

    Rifa 1 ----- * Numero

------------------------------------------------------------------------

## Numero → Comprador

Um **número pode ser reservado por um comprador**.

Cardinalidade:

    Numero 0..1 ----- 1 Comprador

------------------------------------------------------------------------

## Numero → Pagamento

Um **número pode ter um pagamento associado**.

Cardinalidade:

    Numero 1 ----- 0..1 Pagamento

------------------------------------------------------------------------

# 4. Observações

O diagrama de classes representa a estrutura central do sistema e serve
como base para:

-   modelagem do banco de dados
-   implementação das entidades no backend
-   definição das relações entre dados
-   entendimento da arquitetura do sistema

Ele também se relaciona diretamente com:

-   modelo entidade-relacionamento
-   modelo relacional
-   implementação SQL do banco de dados.
