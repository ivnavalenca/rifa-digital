# BDD Scenarios --- Rifa Digital

## Introdução

Este documento apresenta cenários de teste utilizando **BDD (Behavior
Driven Development)**. Os cenários seguem o formato
**Given--When--Then**, conectando:

Requisitos → User Stories → Testes

Essa abordagem melhora a comunicação entre:

-   Product Owner
-   Desenvolvedores
-   QA
-   Stakeholders

------------------------------------------------------------------------

# US01 --- Criar campanha de rifa

Scenario: Criar rifa com dados válidos Given que o organizador acessa o
sistema When ele informa nome, descrição, quantidade de números, valor e
data do sorteio Then o sistema deve criar a campanha de rifa com sucesso

Scenario: Criar rifa sem nome Given que o organizador acessa o sistema
When ele tenta criar uma rifa sem informar o nome Then o sistema deve
exibir mensagem de erro

------------------------------------------------------------------------

# US02 --- Visualizar informações da rifa

Scenario: Visualizar rifa existente Given que existe uma rifa cadastrada
no sistema When o participante acessa a página da rifa Then o sistema
deve exibir as informações da rifa

------------------------------------------------------------------------

# US03 --- Visualizar números disponíveis

Scenario: Exibir números disponíveis Given que uma rifa possui números
cadastrados When o participante acessa a página da rifa Then o sistema
deve exibir os números disponíveis

------------------------------------------------------------------------

# US04 --- Escolher número da rifa

Scenario: Escolher número disponível Given que existe um número
disponível When o participante seleciona o número Then o sistema deve
reservar o número para o participante

Scenario: Evitar duplicação de número Given que um número já foi
selecionado When outro participante tenta escolher o mesmo número Then o
sistema deve impedir a duplicação

------------------------------------------------------------------------

# US06 --- Registrar pagamento

Scenario: Registrar pagamento válido Given que um número está reservado
When o organizador registra o pagamento Then o sistema deve marcar o
número como vendido

------------------------------------------------------------------------

# US10 --- Realizar sorteio

Scenario: Realizar sorteio da rifa Given que todos os números foram
vendidos When o organizador executa o sorteio Then o sistema deve
selecionar um número vencedor

------------------------------------------------------------------------

# US11 --- Divulgar resultado

Scenario: Visualizar resultado da rifa Given que o sorteio foi realizado
When o participante acessa a página da rifa Then o sistema deve exibir o
número vencedor

------------------------------------------------------------------------

# Benefícios do BDD

A utilização de BDD proporciona:

-   melhor entendimento dos requisitos
-   documentação executável de testes
-   alinhamento entre negócio e tecnologia
-   base para automação de testes
