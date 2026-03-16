# 🎟️ Rifa Digital

![GitHub last
commit](https://img.shields.io/github/last-commit/ivnavalenca/rifa-digital)
![GitHub repo
size](https://img.shields.io/github/repo-size/ivnavalenca/rifa-digital)
![GitHub Pages](https://img.shields.io/badge/docs-github%20pages-blue)
![License](https://img.shields.io/github/license/ivnavalenca/rifa-digital)

Sistema web para **criação e gerenciamento de rifas digitais**,
permitindo que organizadores publiquem campanhas e participantes
escolham números para concorrer a prêmios.

O projeto foi desenvolvido com foco em **engenharia de software,
arquitetura, experiência do usuário e garantia de qualidade**.

------------------------------------------------------------------------

# 🌐 Documentação

A documentação completa do projeto está disponível em:

https://ivnavalenca.github.io/rifa-digital/

Ou diretamente no repositório:

    docs/

------------------------------------------------------------------------

# 📑 Índice

-   Documentação
-   Funcionalidades
-   Fluxo do Sistema
-   Arquitetura (C4 Model)
-   Estrutura da Documentação
-   Qualidade e Testes
-   Tecnologias
-   Executar documentação localmente
-   Autoria

------------------------------------------------------------------------

# ✨ Funcionalidades

-   Criar campanha de rifa
-   Visualizar informações da rifa
-   Visualizar números disponíveis
-   Escolher número da rifa
-   Registrar comprador
-   Registrar pagamento
-   Visualizar números vendidos
-   Acompanhar progresso da rifa
-   Realizar sorteio
-   Divulgar resultado

------------------------------------------------------------------------

# 🧭 Fluxo do Sistema

``` mermaid
flowchart LR

A[Organizador cria rifa] --> B[Rifa publicada]
B --> C[Participantes escolhem números]
C --> D[Pagamento registrado]
D --> E[Número confirmado]
E --> F[Sorteio realizado]
F --> G[Divulgação do vencedor]
```

------------------------------------------------------------------------

# 🏗️ Arquitetura (C4 Model)

## Contexto do Sistema

``` mermaid
flowchart LR

U[Participante] --> S[Rifa Digital]
O[Organizador] --> S

S --> DB[(Banco de Dados)]
S --> P[Processo de Sorteio]
```

## Containers

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

## Componentes

``` mermaid
flowchart LR

API[API da Aplicação]

Rifa[Gestão de Rifas]
Numero[Gestão de Números]
Pagamento[Registro de Pagamento]
Sorteio[Sorteio]

DB[(Banco de Dados)]

API --> Rifa
API --> Numero
API --> Pagamento
API --> Sorteio

Rifa --> DB
Numero --> DB
Pagamento --> DB
Sorteio --> DB
```

------------------------------------------------------------------------

# 📂 Estrutura da Documentação

A documentação do projeto está organizada por áreas de engenharia de
software.

  Área           Descrição
  -------------- ---------------------------------
  Product        visão e planejamento do produto
  UX             personas e jornada do usuário
  Requirements   engenharia de requisitos
  Architecture   arquitetura do sistema
  Process        processo de desenvolvimento
  Testing        estratégia e execução de testes
  User           manual do usuário

Estrutura:

    docs
    ├ product
    ├ ux
    ├ requirements
    ├ architecture
    ├ process
    ├ testing
    └ user

------------------------------------------------------------------------

# 🧪 Qualidade e Testes

O projeto possui uma estrutura completa de **Quality Assurance (QA)**.

Inclui:

-   estratégia de testes
-   plano de testes
-   cenários BDD
-   casos de teste
-   execução de testes
-   métricas de qualidade
-   rastreabilidade

Estrutura:

    docs/testing
    ├ strategy
    ├ design
    ├ execution
    ├ traceability
    ├ process
    └ cases

------------------------------------------------------------------------

# 🧰 Tecnologias Utilizadas

-   GitHub
-   Markdown
-   MkDocs
-   Material for MkDocs
-   GitHub Pages
-   Mermaid (diagramas)

------------------------------------------------------------------------

# 🚀 Executar a documentação localmente

Instalar MkDocs:

    pip install mkdocs-material

Executar servidor local:

    mkdocs serve

Abrir no navegador:

    http://127.0.0.1:8000

------------------------------------------------------------------------

# 📊 Objetivo do Projeto

Este projeto demonstra práticas de:

-   Engenharia de Requisitos
-   Arquitetura de Software
-   UX Design
-   Garantia de Qualidade (QA)
-   Documentação técnica profissional

------------------------------------------------------------------------

# 🚧 Status do Projeto

Projeto acadêmico em desenvolvimento com foco em **engenharia de
software e qualidade**.

Componentes já modelados:

✔ requisitos\
✔ arquitetura\
✔ UX\
✔ estratégia de testes\
✔ documentação técnica

------------------------------------------------------------------------

# 👩‍💻 Autoria

**Ivna Valença**

Projeto acadêmico desenvolvido para estudos de **Engenharia de Software
e Qualidade de Software**.
