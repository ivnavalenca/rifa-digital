# Casos de Teste --- Rifa Digital

Este documento descreve os **Casos de Teste (CT)** utilizados para
validar as **User Stories (US)** e seus **Critérios de Aceitação (AC)**.

Fluxo de rastreabilidade:

Requisito → User Story → Critérios de Aceitação → Casos de Teste

------------------------------------------------------------------------

# US01 --- Criar campanha de rifa

**User Story**\
Como organizador\
Quero criar uma campanha de rifa\
Para disponibilizar números para os participantes.

------------------------------------------------------------------------

## Critérios de Aceitação

  ID     Critério
  ------ --------------------------------------------
  AC01   Organizador deve informar dados da rifa
  AC02   Sistema deve validar campos obrigatórios
  AC03   Sistema deve gerar números automaticamente
  AC04   Sistema deve registrar a rifa no sistema
  AC05   Sistema deve exibir a rifa criada

------------------------------------------------------------------------

# Casos de Teste

## CT01 --- Criar rifa com dados válidos

**User Story:** US01\
**ACs Cobertos:** AC01, AC04, AC05\
**Prioridade:** Alta

### Pré‑condições

Usuário possui permissão de organizador.

### Passos

1.  Acessar página de criação de rifa
2.  Informar nome da rifa
3.  Informar quantidade de números
4.  Informar valor por número
5.  Informar data do sorteio
6.  Confirmar criação

### Resultado Esperado

-   Rifa criada com sucesso
-   Rifa registrada no sistema
-   Informações exibidas na tela

### Status

Não executado

------------------------------------------------------------------------

## CT02 --- Validar campos obrigatórios

**User Story:** US01\
**ACs Cobertos:** AC02\
**Prioridade:** Alta

### Pré‑condições

Usuário acessou tela de criação de rifa.

### Passos

1.  Acessar página de criação de rifa
2.  Deixar campo obrigatório vazio
3.  Tentar criar rifa

### Resultado Esperado

Sistema impede criação e apresenta mensagem de erro.

### Status

Não executado

------------------------------------------------------------------------

## CT03 --- Geração automática de números

**User Story:** US01\
**ACs Cobertos:** AC03\
**Prioridade:** Alta

### Pré‑condições

Usuário criou rifa com quantidade de números definida.

### Passos

1.  Criar rifa com 100 números
2.  Confirmar criação

### Resultado Esperado

Sistema gera automaticamente números de 1 a 100.

### Status

Não executado

------------------------------------------------------------------------

## CT04 --- Exibição da rifa criada

**User Story:** US01\
**ACs Cobertos:** AC05\
**Prioridade:** Média

### Pré‑condições

Rifa criada com sucesso.

### Passos

1.  Acessar página da rifa criada

### Resultado Esperado

Sistema exibe: - nome da rifa - lista de números - valor do número -
data do sorteio

### Status

Não executado

------------------------------------------------------------------------

# Resumo

  User Story   Critérios de Aceitação         Casos de Teste
  ------------ ------------------------------ ------------------------
  US01         AC01, AC02, AC03, AC04, AC05   CT01, CT02, CT03, CT04
