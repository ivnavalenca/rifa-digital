# Testing Documentation --- Rifa Digital

Este diretório contém toda a **documentação de qualidade e testes** do
projeto **Rifa Digital**.

A organização segue boas práticas de **QA, ISTQB e Engenharia de
Software**, cobrindo planejamento, projeto, execução e rastreabilidade
de testes.

------------------------------------------------------------------------

# Visão Geral do Processo de Testes

O processo de testes do projeto segue o fluxo:

Requisitos → User Stories → Estratégia de Testes → Plano de Testes → BDD
→ Casos de Teste → Execução → Métricas de Qualidade → Rastreabilidade

``` mermaid
flowchart TD
A[Requisitos] --> B[User Stories]
B --> C[BDD Scenarios]
C --> D[Test Cases]
D --> E[Test Execution]
E --> F[Quality Dashboard]
D --> G[Traceability Matrix]
F --> H[Test Process]
```

------------------------------------------------------------------------

# Estrutura da Documentação

## Strategy

Documentos relacionados ao **planejamento da estratégia de testes**.

-   `estrategia-testes.md` --- abordagem geral de testes
-   `plano-testes.md` --- plano detalhado de execução
-   `test-pyramid.md` --- estratégia de automação e níveis de testes

------------------------------------------------------------------------

## Design

Documentos relacionados ao **projeto de testes**.

-   `bdd-scenarios.md` --- cenários Given--When--Then derivados das User
    Stories
-   `casos-de-teste.md` --- especificação dos casos de teste
-   `test-data.md` --- dados utilizados durante os testes

------------------------------------------------------------------------

## Execution

Documentos relacionados à **execução dos testes e resultados**.

-   `test-execution-report.md` --- relatório de execução dos testes
-   `quality-dashboard.md` --- métricas de qualidade e cobertura de
    testes

------------------------------------------------------------------------

## Traceability

Documentos que garantem **rastreabilidade entre requisitos e testes**.

-   `matriz-rastreabilidade-testes.md` --- matriz RF → US → CT
-   `test-traceability-diagram.md` --- diagrama visual de
    rastreabilidade

------------------------------------------------------------------------

## Process

Documentos relacionados ao **processo de qualidade**.

-   `plano-qualidade.md` --- práticas de garantia da qualidade
-   `test-process-diagram.md` --- diagrama do processo de testes

------------------------------------------------------------------------

## Cases

Contém os **casos de teste detalhados**.

Cada caso de teste segue o padrão:

    CTXXX-USYY-descricao.md

Exemplo:

    CT005-US01-criar-rifa-sem-data-de-sorteio.md

------------------------------------------------------------------------

# Objetivo desta Organização

Essa estrutura permite:

-   rastreabilidade completa entre requisitos e testes
-   clareza no processo de QA
-   separação entre planejamento, design e execução
-   fácil navegação da documentação

Essa abordagem é inspirada em práticas utilizadas por **equipes
profissionais de QA e DevOps**.
