# Processo de Desenvolvimento --- Rifa Digital

Este documento descreve o **processo de desenvolvimento utilizado no
projeto Rifa Digital**, destacando as práticas ágeis adotadas e como
elas são aplicadas na organização do trabalho.

O projeto utiliza um processo de desenvolvimento **ágil**, combinando
práticas das metodologias **Scrum** e **Kanban**, abordagem
frequentemente conhecida como **Scrumban**.

------------------------------------------------------------------------

# 1. Abordagem Ágil

O desenvolvimento do sistema segue princípios de metodologias ágeis,
priorizando:

-   entregas incrementais
-   adaptação a mudanças
-   colaboração contínua
-   melhoria contínua do processo

O projeto utiliza ferramentas do ecossistema GitHub para gerenciar o
desenvolvimento.

------------------------------------------------------------------------

# 2. Metodologias Utilizadas

## Scrum

O Scrum é utilizado para organizar o planejamento e a estrutura do
trabalho.

Práticas utilizadas no projeto:

-   **Product Backlog**
-   **Epics**
-   **User Stories**
-   **Story Points**
-   **Sprints**
-   **Roadmap de desenvolvimento**

As funcionalidades do sistema são organizadas como **User Stories**,
agrupadas em **Epics**, e distribuídas ao longo das sprints.

------------------------------------------------------------------------

## Kanban

O Kanban é utilizado para visualizar o fluxo de trabalho e acompanhar o
progresso das tarefas.

O quadro Kanban do projeto contém colunas como:

-   Product Backlog
-   Sprint Backlog
-   To Do
-   Doing
-   Review
-   Done

Esse quadro é implementado através do **GitHub Projects**.

------------------------------------------------------------------------

# 3. Ferramentas Utilizadas

O gerenciamento do projeto utiliza ferramentas integradas ao GitHub:

-   **GitHub Issues** --- registro de épicos, histórias de usuário,
    tarefas e bugs
-   **GitHub Projects** --- organização visual do trabalho em formato
    Kanban
-   **GitHub Repository** --- armazenamento da documentação e código do
    projeto

Project Board:

https://github.com/users/ivnavalenca/projects/4

------------------------------------------------------------------------

# 4. Fluxo do Processo de Desenvolvimento

O processo de desenvolvimento segue o fluxo abaixo:

Visão do Produto\
↓\
Personas\
↓\
Jornada do Usuário\
↓\
Requisitos\
↓\
Product Backlog\
↓\
Planejamento das Sprints\
↓\
Desenvolvimento\
↓\
Revisão\
↓\
Entrega

Esse fluxo permite transformar necessidades do usuário em
funcionalidades implementadas no sistema.

------------------------------------------------------------------------

# 5. Artefatos do Processo

O projeto utiliza os seguintes artefatos de engenharia de software:
```
  Artefato                      Localização
  ----------------------------- -------------------------------------
  Visão do Produto              docs/01-visao-produto.md
  Requisitos                    docs/02-requisitos.md
  Personas                      docs/03-personas.md
  Jornada do Usuário            docs/04-jornada-usuario.md
  Arquitetura                   docs/05-arquitetura.md
  Modelo de Dados               docs/06-modelo-dados.md
  Roadmap                       docs/07-roadmap.md
  Rastreabilidade               docs/08-rastreabilidade.md
  Processo de Desenvolvimento   docs/09-processo-desenvolvimento.md
```
------------------------------------------------------------------------

# 6. Gestão do Backlog

O backlog do projeto é mantido através de **GitHub Issues** e organizado
no **GitHub Project Board**.

Os itens do backlog incluem:

-   **Epics** --- grandes funcionalidades do sistema
-   **User Stories** --- requisitos do ponto de vista do usuário
-   **Tasks** --- atividades técnicas necessárias para implementar as
    histórias
-   **Bugs** --- defeitos identificados durante o desenvolvimento

------------------------------------------------------------------------

# 7. Organização em Sprints

O desenvolvimento do sistema foi planejado em **sprints de duas
semanas**, cada uma com objetivos específicos.
```
  Sprint     Objetivo
  ---------- ---------------------------
  Sprint 1   Estrutura inicial da rifa
  Sprint 2   Compra de números
  Sprint 3   Pagamentos e controle
  Sprint 4   Sorteio e finalização
```
------------------------------------------------------------------------

# 8. Benefícios do Processo Utilizado

A utilização de práticas ágeis traz diversas vantagens ao projeto:

-   melhor organização do trabalho
-   maior transparência do progresso
-   facilidade para adaptar requisitos
-   melhoria contínua do desenvolvimento

------------------------------------------------------------------------

# 9. Considerações Finais

O processo adotado combina práticas de **Scrum e Kanban**, permitindo
planejamento estruturado e acompanhamento visual das tarefas.

Essa abordagem proporciona maior controle sobre o desenvolvimento e
facilita a gestão das funcionalidades e melhorias do sistema.
