# Arquitetura do Sistema

Este documento descreve a arquitetura do sistema **Rifa Digital**, apresentando a estrutura técnica utilizada para implementar as funcionalidades do sistema.

---

# 1. Visão Geral da Arquitetura

O sistema Rifa Digital segue uma arquitetura baseada em camadas, separando responsabilidades entre interface do usuário, lógica de negócio e persistência de dados.

Arquitetura geral:

Usuário  
↓  
Frontend (Interface Web)  
↓  
API Backend  
↓  
Banco de Dados

Essa separação facilita manutenção, escalabilidade e evolução do sistema.

---

# 2. Camadas do Sistema

## 2.1 Camada de Apresentação (Frontend)

Responsável pela interface com o usuário.

Principais funções:

- exibir informações da rifa
- mostrar números disponíveis
- permitir seleção de números
- exibir resultados do sorteio

Exemplos de tecnologias:

- HTML
- CSS
- JavaScript
- React (opcional)

---

## 2.2 Camada de Aplicação (Backend)

Responsável pela lógica de negócio do sistema.

Principais responsabilidades:

- gerenciamento de rifas
- controle de números disponíveis
- registro de compradores
- validação de pagamentos
- realização do sorteio

Exemplos de tecnologias:

- Node.js
- Python
- Java
- API REST

---

## 2.3 Camada de Persistência (Banco de Dados)

Responsável pelo armazenamento das informações do sistema.

Principais dados armazenados:

- rifas
- números da rifa
- compradores
- pagamentos
- resultados do sorteio

Exemplos de tecnologias:

- PostgreSQL
- MySQL
- MongoDB

---

# 3. Componentes do Sistema

Principais componentes do sistema:

## Gerenciamento de Rifa

Responsável por:

- criar campanha de rifa
- definir número de bilhetes
- configurar data do sorteio

Relacionado às User Stories:

US01 - Criar campanha de rifa  
US02 - Visualizar informações da rifa

---

## Compra de Números

Responsável por:

- exibir números disponíveis
- permitir seleção de números
- registrar compradores

Relacionado às User Stories:

US03 - Visualizar números disponíveis  
US04 - Escolher número da rifa  
US05 - Registrar comprador

---

## Pagamento

Responsável por:

- registrar pagamento
- confirmar venda do número

Relacionado às User Stories:

US06 - Registrar pagamento  
US07 - Marcar número vendido

---

## Sorteio

Responsável por:

- realizar sorteio
- divulgar resultado

Relacionado às User Stories:

US10 - Realizar sorteio  
US11 - Divulgar resultado

---

# 4. Fluxo de Dados

Exemplo de fluxo de operação:

Participante acessa a rifa  
↓  
Frontend solicita números disponíveis  
↓  
Backend consulta banco de dados  
↓  
Sistema retorna números disponíveis  
↓  
Usuário escolhe número  
↓  
Sistema registra comprador  
↓  
Pagamento é registrado  
↓  
Número é marcado como vendido

---

# 5. Considerações de Segurança

O sistema deve implementar medidas para evitar fraudes e inconsistências.

Principais cuidados:

- impedir seleção simultânea do mesmo número
- validar dados recebidos
- registrar logs das operações
- proteger dados dos usuários

Relacionamento com requisitos:

RNF01 - impedir duplicação de números  
RNF03 - validação de dados  
RNF08 - proteção de dados pessoais

---

# 6. Escalabilidade e Evolução

A arquitetura proposta permite evolução do sistema para incluir novas funcionalidades, como:

- integração com meios de pagamento
- autenticação de usuários
- notificações automáticas
- painel administrativo

---

# 7. Observações

A arquitetura apresentada busca garantir organização, segurança e facilidade de manutenção do sistema Rifa Digital.
