# Test Pyramid --- Rifa Digital

## 1. Introdução

Este documento descreve a **Test Pyramid** adotada no projeto **Rifa
Digital**.

A Test Pyramid é um modelo amplamente utilizado em engenharia de
software moderna para organizar os testes de acordo com:

-   velocidade de execução
-   custo de manutenção
-   nível de confiabilidade

Essa abordagem é recomendada por boas práticas de **ISTQB, Agile Testing
e DevOps**.

------------------------------------------------------------------------

# 2. Conceito da Pirâmide de Testes

A pirâmide organiza os testes em três níveis principais:

Unit Tests → Integration Tests → End‑to‑End Tests

Quanto mais baixo na pirâmide:

-   maior quantidade de testes
-   execução mais rápida
-   menor custo

Quanto mais alto:

-   menor quantidade de testes
-   maior custo
-   maior complexidade

------------------------------------------------------------------------

# 3. Representação da Pirâmide

                E2E Tests
            (Fluxos do Usuário)

           Integration Tests
         (API + Banco de Dados)

               Unit Tests
            (Lógica de Negócio)

------------------------------------------------------------------------

# 4. Estratégia de Testes para o Projeto

## 4.1 Testes de Unidade

Objetivo: Validar funções e componentes individuais do sistema.

Exemplos aplicados ao projeto:

-   validação de dados da rifa
-   cálculo de progresso da rifa
-   validação de regras de negócio
-   lógica de sorteio

Benefícios:

-   execução rápida
-   identificação precoce de defeitos
-   baixo custo de manutenção

------------------------------------------------------------------------

## 4.2 Testes de Integração

Objetivo: Validar a interação entre diferentes componentes do sistema.

Componentes envolvidos:

-   frontend
-   backend
-   banco de dados

Exemplos aplicados ao projeto:

-   comunicação entre interface e API
-   registro de compradores
-   registro de pagamentos
-   atualização do status dos números

------------------------------------------------------------------------

## 4.3 Testes End‑to‑End (E2E)

Objetivo: Validar fluxos completos do usuário no sistema.

Exemplos de fluxos testados:

-   criar campanha de rifa
-   escolher número da rifa
-   registrar pagamento
-   realizar sorteio
-   visualizar resultado

Esses testes simulam o comportamento real do usuário.

------------------------------------------------------------------------

# 5. Estratégia de Automação

Embora o projeto utilize principalmente **testes manuais**, a estratégia
prevê a possibilidade de automação futura.

  Tipo de Teste          Ferramentas Possíveis
  ---------------------- -----------------------
  Testes de Unidade      Jest / PyTest
  Testes de Integração   Supertest
  Testes E2E             Cypress / Playwright

Essas ferramentas podem ser integradas a pipelines de **CI/CD**.

------------------------------------------------------------------------

# 6. Benefícios da Automação de Testes

A adoção de automação traz diversos benefícios:

-   execução rápida de regressões
-   maior cobertura de testes
-   detecção precoce de defeitos
-   melhoria contínua da qualidade do software

------------------------------------------------------------------------

# 7. Relação com os Casos de Teste do Projeto

Os casos de teste definidos no projeto representam principalmente
**testes de sistema e testes de aceitação**.

Eles podem servir como base para futura automação.

Localização dos casos de teste:

docs/testing/cases

------------------------------------------------------------------------

# 8. Considerações Finais

A aplicação da **Test Pyramid** contribui para uma estratégia de testes
equilibrada, eficiente e alinhada com boas práticas da indústria.

Mesmo em projetos com foco em testes manuais, a definição da pirâmide
permite planejar a evolução da qualidade do software e a introdução
gradual de automação.
