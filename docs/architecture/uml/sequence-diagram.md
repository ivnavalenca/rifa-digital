# Diagrama de Sequência --- Compra de Número

Este documento apresenta o **Diagrama de Sequência UML** para o fluxo de
compra/reserva de um número da rifa no sistema **Rifa Digital**.

O objetivo é mostrar a interação entre os principais componentes do
sistema durante essa operação.

------------------------------------------------------------------------

# 1. Participantes do Diagrama

O fluxo envolve os seguintes elementos:

-   **Participante** --- usuário que escolhe o número da rifa
-   **Frontend** --- interface web do sistema
-   **Backend / API** --- lógica de negócio
-   **Banco de Dados** --- persistência das informações

------------------------------------------------------------------------

# 2. Diagrama de Sequência

``` mermaid
sequenceDiagram

participant P as Participante
participant F as Frontend
participant B as Backend / API
participant DB as Banco de Dados

P->>F: Acessar página da rifa
F->>B: Solicitar números disponíveis
B->>DB: Consultar números
DB-->>B: Retornar números disponíveis
B-->>F: Lista de números
F-->>P: Exibir números disponíveis

P->>F: Selecionar número
F->>B: Enviar dados do participante

B->>DB: Registrar comprador
B->>DB: Atualizar status do número

DB-->>B: Confirmação

B-->>F: Número reservado
F-->>P: Exibir confirmação
```

------------------------------------------------------------------------

# 3. Descrição do Fluxo

1.  O **participante** acessa a página da rifa.
2.  O **frontend** solicita ao backend a lista de números disponíveis.
3.  O **backend** consulta o banco de dados.
4.  O **banco de dados** retorna os números disponíveis.
5.  O sistema exibe os números ao participante.
6.  O participante escolhe um número.
7.  O frontend envia os dados do participante ao backend.
8.  O backend registra o comprador no banco.
9.  O backend atualiza o status do número para **reservado**.
10. O sistema confirma a reserva ao usuário.

------------------------------------------------------------------------

# 4. Observações

Este diagrama ajuda a compreender:

-   como os componentes do sistema interagem
-   o fluxo de dados entre frontend, backend e banco
-   a sequência de operações necessárias para reservar um número

Ele complementa:

-   os **casos de uso**
-   o **diagrama de classes**
-   a **arquitetura do sistema**
