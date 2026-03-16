# Arquitetura do Sistema --- Rifa Digital

Este documento descreve a arquitetura do sistema **Rifa Digital**,
apresentando a organização técnica utilizada para implementar as
funcionalidades do sistema.

------------------------------------------------------------------------

# 1. Visão Geral da Arquitetura

O sistema segue uma arquitetura em camadas, separando responsabilidades
entre interface do usuário, lógica de negócio e persistência de dados.

Fluxo geral:

Usuário\
↓\
Frontend (Interface Web)\
↓\
Backend / API\
↓\
Banco de Dados

Essa separação facilita manutenção, evolução e escalabilidade do
sistema.

------------------------------------------------------------------------

# 2. Camadas do Sistema

## 2.1 Camada de Apresentação (Frontend)

Responsável pela interação com o usuário.

Principais funções:

-   exibir informações da rifa
-   mostrar números disponíveis
-   permitir seleção de números
-   exibir resultados do sorteio

Tecnologias possíveis:

-   HTML
-   CSS
-   JavaScript
-   React (opcional)

------------------------------------------------------------------------

## 2.2 Camada de Aplicação (Backend)

Responsável pela lógica de negócio do sistema.

Principais responsabilidades:

-   gerenciamento de rifas
-   controle de números disponíveis
-   registro de compradores
-   validação de pagamentos
-   realização do sorteio

Tecnologias possíveis:

-   Node.js
-   Python
-   Java
-   API REST

------------------------------------------------------------------------

## 2.3 Camada de Persistência (Banco de Dados)

Responsável pelo armazenamento das informações do sistema.

Principais dados armazenados:

-   rifas
-   números da rifa
-   compradores
-   pagamentos
-   resultados do sorteio

Tecnologias possíveis:

-   PostgreSQL
-   MySQL
-   MongoDB

------------------------------------------------------------------------

# 3. Componentes do Sistema

## Gerenciamento de Rifa

Responsável por:

-   criar campanha de rifa
-   definir número de bilhetes
-   configurar data do sorteio

User Stories relacionadas:

US01 - Criar campanha de rifa\
US02 - Visualizar informações da rifa

------------------------------------------------------------------------

## Compra de Números

Responsável por:

-   exibir números disponíveis
-   permitir seleção de números
-   registrar compradores

User Stories relacionadas:

US03 - Visualizar números disponíveis\
US04 - Escolher número da rifa\
US05 - Registrar comprador

------------------------------------------------------------------------

## Pagamento

Responsável por:

-   registrar pagamento
-   confirmar venda do número

User Stories relacionadas:

US06 - Registrar pagamento\
US07 - Marcar número como vendido

------------------------------------------------------------------------

## Sorteio

Responsável por:

-   realizar sorteio
-   divulgar resultado

User Stories relacionadas:

US10 - Realizar sorteio\
US11 - Divulgar resultado

------------------------------------------------------------------------

# 4. Fluxo de Dados

Exemplo de fluxo de operação:

Participante acessa a rifa\
↓\
Frontend solicita números disponíveis\
↓\
Backend consulta banco de dados\
↓\
Sistema retorna números disponíveis\
↓\
Usuário escolhe número\
↓\
Sistema registra comprador\
↓\
Pagamento é registrado\
↓\
Número é marcado como vendido

------------------------------------------------------------------------

# 5. Considerações de Segurança

O sistema deve implementar medidas para evitar fraudes e
inconsistências.

Principais cuidados:

-   impedir seleção simultânea do mesmo número
-   validar dados recebidos
-   registrar logs das operações
-   proteger dados dos usuários

------------------------------------------------------------------------

# 6. Evolução do Sistema

A arquitetura permite evolução do sistema para incluir funcionalidades
como:

-   integração com meios de pagamento
-   autenticação de usuários
-   notificações automáticas
-   painel administrativo
