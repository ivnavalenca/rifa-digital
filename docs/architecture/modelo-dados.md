# Modelo de Dados --- Rifa Digital

Este documento apresenta o modelo de dados do sistema **Rifa Digital**,
descrevendo as entidades, atributos e relacionamentos responsáveis pelo
armazenamento das informações do sistema.

------------------------------------------------------------------------

# 1. Visão Geral

O banco de dados armazena informações relacionadas a:

-   campanhas de rifa
-   números disponíveis
-   participantes
-   pagamentos
-   resultado do sorteio

O modelo segue uma estrutura relacional para garantir **integridade e
consistência dos dados**.

------------------------------------------------------------------------

# 2. Diagrama Entidade-Relacionamento

``` mermaid
erDiagram

RIFA ||--o{ NUMERO : possui
NUMERO }o--|| COMPRADOR : reservado_por
NUMERO ||--o{ PAGAMENTO : possui

RIFA {
  int id
  string nome
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
  int rifa_id
  int comprador_id
}

COMPRADOR {
  int id
  string nome
  string telefone
  string email
}

PAGAMENTO {
  int id
  decimal valor
  date data_pagamento
  string status
  int numero_id
}
```

------------------------------------------------------------------------

# 3. Entidades do Sistema

## Rifa

Representa uma campanha de rifa criada por um organizador.

Principais atributos:

-   id
-   nome
-   descricao
-   valor_numero
-   quantidade_numeros
-   data_sorteio
-   status

------------------------------------------------------------------------

## Número

Representa um número da rifa que pode ser comprado por um participante.

Principais atributos:

-   id
-   numero
-   status (disponível, reservado, vendido)
-   rifa_id
-   comprador_id

------------------------------------------------------------------------

## Comprador

Representa o participante que compra ou reserva um número.

Principais atributos:

-   id
-   nome
-   telefone
-   email

------------------------------------------------------------------------

## Pagamento

Representa o pagamento realizado para confirmar a compra de um número.

Principais atributos:

-   id
-   valor
-   data_pagamento
-   status
-   numero_id

------------------------------------------------------------------------

# 4. Relacionamentos

Os relacionamentos entre as entidades são:

-   Uma **rifa possui vários números**.
-   Cada **número pertence a uma única rifa**.
-   Um **comprador pode reservar um número da rifa**.
-   Um **pagamento está associado a um número**.

------------------------------------------------------------------------

# 5. Regras de Integridade

Para garantir consistência no sistema:

-   Um número só pode pertencer a **uma única rifa**.
-   Um número só pode ser **vendido uma vez**.
-   Um pagamento deve estar associado a **um número válido**.
-   Um número só pode ser marcado como **vendido após confirmação do
    pagamento**.

------------------------------------------------------------------------

# 6. Considerações

O modelo de dados foi projetado para:

-   garantir integridade das informações
-   evitar duplicação de números
-   facilitar consultas e relatórios
-   permitir evolução futura do sistema
