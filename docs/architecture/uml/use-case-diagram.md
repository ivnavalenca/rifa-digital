# Diagrama de Caso de Uso --- Rifa Digital

Este documento apresenta o **Diagrama de Caso de Uso** do sistema **Rifa
Digital**, representando as interações entre os usuários e as
funcionalidades do sistema.

Os casos de uso foram definidos com base nos requisitos funcionais e nas
jornadas dos usuários.

------------------------------------------------------------------------

# 1. Atores do Sistema

O sistema possui dois atores principais:

**Organizador** - cria campanhas de rifa - gerencia números - registra
pagamentos - realiza sorteio

**Participante** - visualiza a rifa - escolhe números - participa do
sorteio

------------------------------------------------------------------------

# 2. Diagrama de Caso de Uso

``` mermaid
flowchart LR

Organizador((Organizador))
Participante((Participante))

CriarRifa[ Criar campanha de rifa ]
VisualizarRifa[ Visualizar informações da rifa ]
VisualizarNumeros[ Visualizar números disponíveis ]
EscolherNumero[ Escolher número da rifa ]
RegistrarComprador[ Registrar comprador ]
RegistrarPagamento[ Registrar pagamento ]
MarcarVendido[ Marcar número como vendido ]
VisualizarProgresso[ Visualizar progresso da rifa ]
RealizarSorteio[ Realizar sorteio ]
DivulgarResultado[ Divulgar resultado ]

Organizador --> CriarRifa
Organizador --> RegistrarPagamento
Organizador --> MarcarVendido
Organizador --> VisualizarProgresso
Organizador --> RealizarSorteio
Organizador --> DivulgarResultado

Participante --> VisualizarRifa
Participante --> VisualizarNumeros
Participante --> EscolherNumero
Participante --> RegistrarComprador
Participante --> VisualizarProgresso
Participante --> DivulgarResultado
```

------------------------------------------------------------------------

# 3. Descrição dos Casos de Uso

## Criar campanha de rifa

Permite ao organizador criar uma nova campanha informando:

-   nome da rifa
-   descrição
-   quantidade de números
-   valor de cada número
-   data do sorteio

## Visualizar informações da rifa

Permite visualizar:

-   nome da campanha
-   descrição
-   valor do número
-   data do sorteio

## Visualizar números disponíveis

O sistema apresenta todos os números da rifa com status:

-   disponível
-   reservado
-   vendido

## Escolher número da rifa

Permite que o participante selecione um número disponível.

## Registrar comprador

Após escolher um número, o sistema registra os dados do participante:

-   nome
-   telefone
-   email

## Registrar pagamento

O organizador registra a confirmação do pagamento do número reservado.

## Marcar número como vendido

Após confirmação do pagamento, o número passa para o status **vendido**.

## Visualizar progresso da rifa

Permite acompanhar:

-   números disponíveis
-   números reservados
-   números vendidos

## Realizar sorteio

O organizador executa o sorteio para definir o número vencedor.

## Divulgar resultado

O sistema exibe:

-   número vencedor
-   participante vencedor

------------------------------------------------------------------------

# 4. Observações

Este diagrama ajuda a compreender:

-   as funcionalidades principais do sistema
-   os atores envolvidos
-   as interações entre usuários e sistema

Ele também serve como base para:

-   modelagem UML
-   definição de requisitos
-   planejamento de testes
-   desenvolvimento das funcionalidades.
