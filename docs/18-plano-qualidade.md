# Plano de Qualidade --- Rifa Digital

## Objetivo

Definir critérios e práticas para garantir a qualidade do sistema Rifa
Digital.

------------------------------------------------------------------------

## Critérios de Qualidade

### Confiabilidade

O sistema deve manter a integridade das informações registradas.

### Segurança

-   impedir duplicação de números
-   proteger dados dos participantes

### Usabilidade

A interface deve ser simples e fácil de usar.

### Performance

Tempo de resposta inferior a 2 segundos para operações principais.

------------------------------------------------------------------------

## Controle de Defeitos

Defeitos identificados durante o desenvolvimento devem ser registrados
como **issues do tipo Bug** no GitHub.

Exemplo:

BUG01 --- Número da rifa pode ser selecionado duas vezes

------------------------------------------------------------------------

## Processo de Correção

1.  Identificação do defeito
2.  Registro no backlog
3.  Correção durante a sprint
4.  Teste de regressão
5.  Validação final
