# Test Data --- Rifa Digital

## 1. Introdução

Este documento descreve os **dados de teste utilizados para validar o
sistema Rifa Digital**.

Os dados de teste permitem simular cenários reais de utilização do
sistema.

------------------------------------------------------------------------

# 2. Dados de Teste de Rifa

  Campo                   Valor de Teste
  ----------------------- --------------------------
  Nome da rifa            Rifa Páscoa 2026
  Descrição               Rifa para viagem escolar
  Quantidade de números   100
  Valor do número         10
  Data do sorteio         30/04/2026

------------------------------------------------------------------------

# 3. Dados de Comprador

  Campo      Valor
  ---------- -------------------
  Nome       João da Silva
  Telefone   \(81\) 99999-9999
  Email      joao@email.com

------------------------------------------------------------------------

# 4. Dados de Pagamento

  Campo    Valor
  -------- ------------
  Valor    10
  Data     10/03/2026
  Status   Confirmado

------------------------------------------------------------------------

# 5. Cenários de Teste

## Cenário 1 --- Criar rifa válida

Dados utilizados:

-   nome da rifa válido
-   quantidade de números positiva
-   valor do número positivo

Resultado esperado:

-   sistema cria a rifa corretamente

------------------------------------------------------------------------

## Cenário 2 --- Número duplicado

Dados utilizados:

-   dois usuários tentando selecionar o mesmo número

Resultado esperado:

-   sistema bloqueia a duplicação

------------------------------------------------------------------------

# 6. Considerações

Os dados de teste devem ser atualizados sempre que novos cenários ou
funcionalidades forem adicionados ao sistema.
