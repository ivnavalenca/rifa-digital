# Documentação do Projeto --- Rifa Digital

Este diretório reúne toda a **documentação do sistema Rifa Digital**.

A organização segue práticas comuns de **Engenharia de Software, Product
Management, UX e Quality Assurance**, separando os artefatos por área de
responsabilidade.

------------------------------------------------------------------------

# Estrutura da Documentação

``` text
docs
├ product
├ ux
├ requirements
├ architecture
├ process
├ testing
└ user
```

Cada pasta contém documentos específicos de uma etapa do ciclo de
desenvolvimento.

------------------------------------------------------------------------

# Product

Documentos relacionados à **visão do produto e planejamento**.

-   `visao-produto.md` --- visão geral do sistema
-   `roadmap.md` --- planejamento evolutivo do produto
-   `stakeholders.md` --- partes interessadas do projeto

------------------------------------------------------------------------

# UX

Documentação relacionada à **experiência do usuário**.

-   `personas.md` --- perfis de usuários do sistema
-   `jornada-usuario.md` --- jornada de uso do sistema
-   `sequencia.md` --- fluxos de interação

------------------------------------------------------------------------

# Requirements

Documentos de **engenharia de requisitos**.

-   `requisitos.md` --- requisitos funcionais e não funcionais
-   `casos-de-uso.md` --- casos de uso do sistema
-   `priorizacao-requisitos.md` --- priorização de funcionalidades
-   `rastreabilidade.md` --- rastreabilidade entre requisitos

------------------------------------------------------------------------

# Architecture

Documentação da **arquitetura do sistema**.

-   `arquitetura.md` --- visão arquitetural da solução
-   `modelo-dados.md` --- modelo de dados do sistema

------------------------------------------------------------------------

# Process

Documentação relacionada ao **processo de desenvolvimento e qualidade**.

-   `processo-desenvolvimento.md` --- processo de desenvolvimento
    adotado

------------------------------------------------------------------------

# Testing

Documentação de **qualidade e testes de software**.

Inclui:

-   estratégia de testes
-   plano de testes
-   cenários BDD
-   casos de teste
-   execução de testes
-   métricas de qualidade
-   rastreabilidade

Para acessar todos os documentos de QA:

    docs/testing/

------------------------------------------------------------------------

# User

Documentação destinada ao **usuário final**.

-   `manual-usuario.md` --- manual de uso do sistema

------------------------------------------------------------------------

# Visão do Ciclo de Engenharia

A documentação segue o fluxo típico de desenvolvimento de software:

``` mermaid
flowchart LR

A[Product Vision] --> B[UX Design]
B --> C[Requirements]
C --> D[Architecture]
D --> E[Development Process]
E --> F[Testing]
F --> G[User Documentation]
```

------------------------------------------------------------------------

# Objetivo da Organização

Essa estrutura facilita:

-   navegação da documentação
-   separação por área de responsabilidade
-   rastreabilidade entre artefatos
-   manutenção da documentação ao longo do projeto

Esse modelo é inspirado em práticas utilizadas em **projetos
profissionais de engenharia de software e DevOps**.
