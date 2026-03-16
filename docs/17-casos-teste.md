# Casos de Teste --- Rifa Digital

Este documento descreve os casos de teste utilizados para validar os
requisitos e as funcionalidades do sistema **Rifa Digital**.

Cada caso de teste está relacionado a uma **User Story** e a um
**Requisito Funcional**, garantindo rastreabilidade entre requisitos e
validação.

------------------------------------------------------------------------

## CT01 --- Criar campanha de rifa

**User Story:** US01 --- Criar campanha de rifa\
**Requisito:** RF01\
**Prioridade:** Alta

### Descrição

Verificar se o organizador consegue criar uma nova campanha de rifa.

### Pré-condições

-   Usuário possui permissão de organizador

### Passos

1.  Acessar página de criação de rifa
2.  Informar nome da rifa
3.  Informar quantidade de números
4.  Informar valor por número
5.  Informar data do sorteio
6.  Confirmar criação

### Resultado Esperado

A rifa é criada com sucesso e os números são gerados automaticamente.

### Status

Não executado

------------------------------------------------------------------------

## CT02 --- Visualizar números da rifa

**User Story:** US02 --- Visualizar informações da rifa\
**Requisito:** RF02\
**Prioridade:** Alta

### Descrição

Validar se os participantes conseguem visualizar os números disponíveis
da rifa.

### Pré-condições

-   Rifa já criada

### Passos

1.  Acessar página da rifa
2.  Visualizar lista de números

### Resultado Esperado

Os números da rifa aparecem com seus respectivos status: - disponível -
reservado - vendido

### Status

Não executado

------------------------------------------------------------------------

## CT03 --- Selecionar número disponível

**User Story:** US04 --- Escolher número da rifa\
**Requisito:** RF04\
**Prioridade:** Alta

### Descrição

Validar se um participante consegue selecionar um número disponível.

### Pré-condições

-   Rifa criada
-   Número disponível

### Passos

1.  Acessar página da rifa
2.  Selecionar número disponível
3.  Informar dados do participante
4.  Confirmar escolha

### Resultado Esperado

Número fica reservado para o participante.

### Status

Não executado

------------------------------------------------------------------------

## CT04 --- Impedir seleção duplicada

**User Story:** US04 --- Escolher número da rifa\
**Requisito:** RF04\
**Prioridade:** Alta

### Descrição

Verificar se um número já reservado não pode ser selecionado novamente.

### Pré-condições

-   Número já reservado por outro usuário

### Passos

1.  Acessar página da rifa
2.  Tentar selecionar número já reservado

### Resultado Esperado

Sistema impede seleção duplicada e apresenta mensagem de erro.

### Status

Não executado

------------------------------------------------------------------------

## CT05 --- Registrar pagamento

**User Story:** US06 --- Registrar pagamento\
**Requisito:** RF06\
**Prioridade:** Alta

### Descrição

Verificar se o organizador pode registrar o pagamento de um número
reservado.

### Pré-condições

-   Número reservado por participante

### Passos

1.  Acessar painel do organizador
2.  Selecionar número reservado
3.  Confirmar pagamento

### Resultado Esperado

Número é marcado como **vendido**.

### Status

Não executado

------------------------------------------------------------------------

## CT06 --- Cancelar reserva

**User Story:** US07 --- Cancelar reserva\
**Requisito:** RF07\
**Prioridade:** Média

### Descrição

Verificar se uma reserva pode ser cancelada.

### Pré-condições

-   Número reservado

### Passos

1.  Acessar reserva
2.  Selecionar cancelar reserva

### Resultado Esperado

Número volta a ficar disponível.

### Status

Não executado

------------------------------------------------------------------------

## CT07 --- Realizar sorteio

**User Story:** US10 --- Realizar sorteio\
**Requisito:** RF10\
**Prioridade:** Alta

### Descrição

Validar se o sistema consegue realizar o sorteio da rifa.

### Pré-condições

-   Rifa finalizada
-   Números vendidos

### Passos

1.  Acessar página da rifa
2.  Selecionar opção realizar sorteio

### Resultado Esperado

Sistema seleciona automaticamente um número vencedor.

### Status

Não executado

------------------------------------------------------------------------

## CT08 --- Exibir resultado do sorteio

**User Story:** US11 --- Exibir resultado do sorteio\
**Requisito:** RF11\
**Prioridade:** Alta

### Descrição

Verificar se o sistema exibe corretamente o resultado do sorteio.

### Pré-condições

-   Sorteio já realizado

### Passos

1.  Acessar página da rifa

### Resultado Esperado

Sistema exibe: - número vencedor - dados do participante vencedor

### Status

Não executado

------------------------------------------------------------------------

## CT09 --- Compartilhar rifa

**User Story:** US12 --- Compartilhar rifa\
**Requisito:** RF12\
**Prioridade:** Média

### Descrição

Verificar se o usuário pode compartilhar o link da rifa.

### Pré-condições

-   Rifa ativa

### Passos

1.  Acessar página da rifa
2.  Clicar em compartilhar

### Resultado Esperado

Sistema gera link compartilhável da rifa.

### Status

Não executado

------------------------------------------------------------------------

## CT10 --- Visualizar histórico da rifa

**User Story:** US15 --- Visualizar histórico da rifa\
**Requisito:** RF15\
**Prioridade:** Baixa

### Descrição

Verificar se o organizador pode visualizar o histórico da rifa.

### Pré-condições

-   Rifa já finalizada

### Passos

1.  Acessar painel do organizador
2.  Selecionar histórico da rifa

### Resultado Esperado

Sistema exibe histórico com: - números vendidos - participante
vencedor - data do sorteio

### Status

Não executado
