# System Overview --- Rifa Digital

## 1. Visão Geral

O **Rifa Digital** é um sistema web desenvolvido para permitir a criação
e gerenciamento de campanhas de rifas digitais.

O sistema permite que organizadores publiquem rifas e que participantes
escolham números para concorrer a prêmios.

O objetivo do sistema é **facilitar a gestão de rifas**, garantindo
organização, transparência e controle das vendas de números.

------------------------------------------------------------------------

# 2. Principais Funcionalidades

O sistema oferece as seguintes funcionalidades principais:

-   criação de campanhas de rifa
-   visualização de rifas disponíveis
-   escolha de números pelos participantes
-   registro de compradores
-   reserva de números
-   confirmação de pagamento
-   acompanhamento das vendas
-   realização do sorteio
-   divulgação do número vencedor

------------------------------------------------------------------------

# 3. Usuários do Sistema

O sistema possui dois tipos principais de usuários.

## Organizador

Responsável por:

-   criar rifas
-   definir quantidade de números
-   definir valor de cada número
-   acompanhar vendas
-   realizar o sorteio

## Participante

Responsável por:

-   visualizar rifas disponíveis
-   escolher números
-   realizar pagamento
-   acompanhar resultados

------------------------------------------------------------------------

# 4. Fluxo do Sistema

O funcionamento geral do sistema segue o fluxo abaixo.

``` mermaid
flowchart LR

A[Organizador cria rifa] --> B[Rifa publicada]
B --> C[Participantes escolhem números]
C --> D[Número reservado]
D --> E[Pagamento confirmado]
E --> F[Número vendido]
F --> G[Sorteio realizado]
G --> H[Divulgação do vencedor]
```

------------------------------------------------------------------------

# 5. Componentes Principais

O sistema é composto por três componentes principais.
```
  -----------------------------------------------------------------------
  Componente                          Descrição
  ----------------------------------- -----------------------------------
  Frontend                            Interface web utilizada pelos
                                      usuários

  Backend                             Aplicação responsável pela lógica
                                      de negócio

  Banco de Dados                      Armazena rifas, números, reservas,
                                      pagamentos e resultados
  -----------------------------------------------------------------------
```
------------------------------------------------------------------------

# 6. Visão Arquitetural Simplificada

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

------------------------------------------------------------------------

# 7. Entidades Principais

As principais entidades do sistema são:

-   **Rifa**
-   **Número**
-   **Comprador**
-   **Reserva**
-   **Pagamento**
-   **Sorteio**

Essas entidades compõem o modelo de dados responsável por armazenar as
informações do sistema.

------------------------------------------------------------------------

# 8. Documentação Relacionada

A documentação completa do sistema pode ser encontrada nas seguintes
seções:

-   Product --- visão do produto
-   UX --- experiência do usuário
-   Requirements --- requisitos do sistema
-   Architecture --- arquitetura do sistema
-   Testing --- estratégia e execução de testes
-   User --- manual do usuário
