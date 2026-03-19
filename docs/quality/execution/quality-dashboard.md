# Quality Dashboard --- Rifa Digital

## 1. Introdução

Este documento apresenta um **Quality Dashboard** com métricas de
qualidade do sistema **Rifa Digital**.

O objetivo é fornecer uma visão consolidada da qualidade do produto
baseada em:

-   execução de testes
-   defeitos identificados
-   cobertura de requisitos

Essas métricas são comumente utilizadas em práticas de **QA, ISTQB e
DevOps**.

------------------------------------------------------------------------

# 2. Métricas de Teste

  Métrica                   Valor
  ------------------------- -------
  Total de Requisitos       15
  Total de User Stories     15
  Total de Casos de Teste   75
  Casos Executados          75
  Casos Aprovados           72
  Casos Reprovados          3

------------------------------------------------------------------------

# 3. Taxa de Aprovação dos Testes

A taxa de aprovação indica a porcentagem de testes que passaram com
sucesso.

Fórmula:

Taxa de Aprovação = (Testes Aprovados / Testes Executados) × 100

Exemplo:

Taxa de Aprovação = (72 / 75) × 100 = **96%**

------------------------------------------------------------------------

# 4. Cobertura de Testes

A cobertura de testes mede o quanto dos requisitos do sistema possuem
casos de teste associados.

  Item                         Cobertura
  ---------------------------- -----------
  Requisitos Funcionais        100%
  User Stories                 100%
  Funcionalidades principais   100%

Cada User Story possui aproximadamente **5 casos de teste associados**.

------------------------------------------------------------------------

# 5. Densidade de Defeitos

A densidade de defeitos mede a quantidade de defeitos identificados em
relação ao tamanho do sistema.

Fórmula:

Densidade de Defeitos = Número de Defeitos / Número de Funcionalidades

Exemplo:

2 defeitos / 15 funcionalidades = **0,13 defeitos por funcionalidade**

------------------------------------------------------------------------

# 6. Distribuição de Defeitos por Severidade

  Severidade   Quantidade
  ------------ ------------
  Crítica      0
  Alta         1
  Média        1
  Baixa        0

------------------------------------------------------------------------

# 7. Indicadores de Qualidade

  Indicador                 Avaliação
  ------------------------- -----------
  Estabilidade do Sistema   Alta
  Cobertura de Testes       Alta
  Qualidade do Código       Adequada
  Risco de Produção         Baixo

------------------------------------------------------------------------

# 8. Visualização Simplificada

    Cobertura de Testes      █████████████████ 100%
    Taxa de Aprovação        ████████████████  96%
    Defeitos Críticos        █ 0%

------------------------------------------------------------------------

# 9. Conclusão

O sistema **Rifa Digital** apresenta boa qualidade geral com:

-   alta cobertura de testes
-   baixa quantidade de defeitos
-   estabilidade das funcionalidades principais

As métricas indicam que o sistema está **adequado para uso e validação
final**.
