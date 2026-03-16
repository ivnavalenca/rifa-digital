# Arquitetura do Sistema --- Rifa Digital

Esta seção apresenta a **arquitetura do sistema Rifa Digital**,
incluindo a visão geral do sistema, modelo arquitetural, modelo C4 e
documentação do banco de dados.

A arquitetura foi documentada para facilitar:

-   entendimento do funcionamento do sistema
-   evolução e manutenção do software
-   alinhamento entre desenvolvedores
-   organização da documentação técnica

------------------------------------------------------------------------

# Estrutura da Arquitetura

A documentação de arquitetura está organizada nos seguintes documentos:

  Documento                  Descrição
  -------------------------- --------------------------------------------
  system-overview.md         visão geral do sistema
  arquitetura.md             descrição da arquitetura do sistema
  c4-model.md                diagramas arquiteturais usando o modelo C4
  data/modelo-dados.md       modelo de dados do sistema
  data/dicionario-dados.md   dicionário de dados do banco
  data/schema.sql            script SQL do banco de dados
  data/der.png               diagrama entidade-relacionamento

------------------------------------------------------------------------

# Documentos de Arquitetura

## System Overview

Apresenta uma visão geral do sistema, incluindo:

-   objetivo do sistema
-   funcionalidades principais
-   tipos de usuários
-   fluxo do sistema
-   visão arquitetural simplificada

Arquivo:

    system-overview.md

------------------------------------------------------------------------

## Arquitetura do Sistema

Descreve a arquitetura adotada pelo sistema, incluindo:

-   organização da aplicação
-   responsabilidades dos componentes
-   decisões arquiteturais

Arquivo:

    arquitetura.md

------------------------------------------------------------------------

## Modelo C4

Apresenta a arquitetura utilizando o **modelo C4**, que descreve o
sistema em diferentes níveis:

1.  Context Diagram
2.  Container Diagram
3.  Component Diagram

Arquivo:

    c4-model.md

------------------------------------------------------------------------

# Arquitetura de Dados

A documentação de dados descreve o banco de dados utilizado pelo
sistema.

## Modelo de Dados

Contém o diagrama MER e a descrição das entidades do sistema.

Arquivo:

    data/modelo-dados.md

------------------------------------------------------------------------

## Dicionário de Dados

Descreve detalhadamente cada campo das tabelas do banco de dados.

Arquivo:

    data/dicionario-dados.md

------------------------------------------------------------------------

## Script SQL

Contém o script SQL para criação das tabelas do banco de dados.

Arquivo:

    data/schema.sql

------------------------------------------------------------------------

# Diagrama Entidade‑Relacionamento

O DER do sistema pode ser encontrado em:

    data/der.png

Este diagrama apresenta:

-   entidades do sistema
-   atributos principais
-   relacionamentos
-   cardinalidades

------------------------------------------------------------------------

# Benefícios da Documentação de Arquitetura

A documentação de arquitetura permite:

-   melhor entendimento do sistema
-   facilidade de manutenção
-   padronização do desenvolvimento
-   apoio à evolução do software

------------------------------------------------------------------------

# Documentação Relacionada

Outras seções da documentação do projeto:

-   Product --- visão do produto
-   UX --- experiência do usuário
-   Requirements --- requisitos do sistema
-   Testing --- estratégia e execução de testes
-   User --- manual do usuário
