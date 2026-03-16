# Plano de Testes --- Rifa Digital

## 1. Introdução

Este documento apresenta o **Plano de Testes** do sistema **Rifa
Digital**.

O objetivo deste plano é definir:

-   escopo dos testes
-   abordagem de teste
-   recursos necessários
-   cronograma de execução
-   critérios de qualidade

Este plano segue boas práticas baseadas em:

-   ISTQB
-   IEEE 829
-   ISO/IEC/IEEE 29119

------------------------------------------------------------------------

# 2. Itens de Teste

Os seguintes componentes do sistema serão testados:

-   criação de campanhas de rifa
-   visualização de números disponíveis
-   escolha de números
-   registro de compradores
-   registro de pagamentos
-   marcação de números vendidos
-   realização do sorteio
-   divulgação de resultados

------------------------------------------------------------------------

# 3. Funcionalidades a Serem Testadas

  ID     Funcionalidade
  ------ --------------------------------
  RF01   Criar campanha de rifa
  RF02   Visualizar informações da rifa
  RF03   Visualizar números disponíveis
  RF04   Escolher número da rifa
  RF05   Registrar comprador
  RF06   Registrar pagamento
  RF07   Marcar número como vendido
  RF08   Visualizar números vendidos
  RF09   Visualizar progresso da rifa
  RF10   Realizar sorteio
  RF11   Divulgar resultado
  RF12   Compartilhar rifa
  RF13   Visualizar compradores
  RF14   Cancelar reserva
  RF15   Visualizar histórico da rifa

------------------------------------------------------------------------

# 4. Funcionalidades Fora do Escopo

Não fazem parte deste plano:

-   testes de carga em grande escala
-   testes automatizados complexos
-   integração com gateways de pagamento externos

------------------------------------------------------------------------

# 5. Abordagem de Teste

A abordagem adotada inclui:

-   testes manuais baseados em casos de teste
-   validação baseada em User Stories
-   rastreabilidade entre requisitos, testes e defeitos
-   execução progressiva conforme funcionalidades são implementadas

Os casos de teste estão documentados em:

docs/testing/cases

------------------------------------------------------------------------

# 6. Níveis de Teste

## Teste de Unidade

Validação de componentes individuais do sistema.

## Teste de Integração

Validação da comunicação entre:

-   frontend
-   backend
-   banco de dados

## Teste de Sistema

Validação do comportamento completo do sistema.

## Teste de Aceitação

Validação final sob a perspectiva do usuário.

------------------------------------------------------------------------

# 7. Tipos de Teste

## Teste Funcional

Verifica se as funcionalidades operam conforme esperado.

## Teste de Regras de Negócio

Verifica regras importantes como:

-   número não pode ser vendido duas vezes
-   pagamento deve ser confirmado antes da venda
-   sorteio só ocorre após vendas

## Teste de Usabilidade

Avalia facilidade de uso e clareza da interface.

## Teste de Segurança

Avalia proteção contra manipulação de dados e acessos indevidos.

## Teste de Desempenho (básico)

Avalia tempo de resposta das funcionalidades principais.

------------------------------------------------------------------------

# 8. Ambiente de Teste

Os testes serão realizados em ambiente contendo:

-   navegador web
-   backend da aplicação
-   banco de dados

Navegadores utilizados:

-   Google Chrome
-   Mozilla Firefox

------------------------------------------------------------------------

# 9. Dados de Teste

Os dados utilizados incluem:

-   rifas simuladas
-   números de rifa fictícios
-   compradores fictícios
-   pagamentos simulados

------------------------------------------------------------------------

# 10. Critérios de Entrada

Os testes podem iniciar quando:

-   requisitos estiverem definidos
-   funcionalidades implementadas
-   casos de teste documentados
-   ambiente de testes disponível

------------------------------------------------------------------------

# 11. Critérios de Saída

Os testes serão considerados concluídos quando:

-   todos os casos de teste forem executados
-   defeitos críticos forem corrigidos
-   funcionalidades principais estiverem funcionando corretamente

------------------------------------------------------------------------

# 12. Gestão de Defeitos

Defeitos encontrados devem ser registrados como **Issues do tipo Bug no
GitHub**.

Cada registro deve incluir:

-   descrição do problema
-   passos para reprodução
-   resultado esperado
-   resultado obtido
-   evidências (prints ou logs)

------------------------------------------------------------------------

# 13. Papéis e Responsabilidades

  Papel                       Responsabilidade
  --------------------------- -----------------------------------
  Product Owner               Validação do produto
  Equipe de Desenvolvimento   Implementação das funcionalidades
  QA / Testador               Execução dos testes
  Usuários                    Teste de aceitação

------------------------------------------------------------------------

# 14. Cronograma de Testes

  Fase                Atividade
  ------------------- -------------------------------------------
  Planejamento        Definição da estratégia e plano de testes
  Projeto de Testes   Criação dos casos de teste
  Execução            Execução dos testes
  Correção            Correção de defeitos
  Validação           Testes finais e aceitação

------------------------------------------------------------------------

# 15. Riscos de Teste

Principais riscos identificados:

-   duplicação de números da rifa
-   inconsistência no registro de pagamentos
-   falhas no sorteio
-   perda de integridade dos dados

------------------------------------------------------------------------

# 16. Rastreabilidade

A rastreabilidade entre requisitos, user stories e casos de teste pode
ser consultada em:

docs/testing/matriz-rastreabilidade-testes.md

------------------------------------------------------------------------

# 17. Aprovação

Este plano de testes deve ser revisado e aprovado pelas partes
responsáveis antes do início da execução dos testes.
