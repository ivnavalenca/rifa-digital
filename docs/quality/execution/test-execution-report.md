# Test Execution Report --- Rifa Digital

## 1. Introdução

Este documento apresenta o **Relatório de Execução de Testes** do
sistema **Rifa Digital**.

Seu objetivo é registrar:

-   resultados da execução dos casos de teste
-   defeitos identificados
-   status geral da qualidade do sistema

------------------------------------------------------------------------

# 2. Ambiente de Teste

  Item             Descrição
  ---------------- -----------------------------------
  Sistema          Rifa Digital
  Ambiente         Desenvolvimento
  Navegadores      Google Chrome, Mozilla Firefox
  Banco de dados   Ambiente local de desenvolvimento

------------------------------------------------------------------------

# 3. Resumo da Execução

  Métrica                   Valor
  ------------------------- -------
  Total de Casos de Teste   75
  Executados                75
  Aprovados                 72
  Reprovados                3

------------------------------------------------------------------------

# 4. Resultados por Caso de Teste

  Caso de Teste   User Story   Status   Observação
  --------------- ------------ -------- ------------------------------------
  CT001           US01         Pass     Criação da rifa funcionando
  CT002           US01         Pass     Validação de nome correta
  CT003           US01         Fail     Campo quantidade aceita vazio
  CT006           US02         Pass     Visualização da rifa correta
  CT010           US02         Pass     Exibição da rifa encerrada correta

------------------------------------------------------------------------

# 5. Defeitos Identificados

  -----------------------------------------------------------------------
  ID                Descrição         Severidade        Status
  ----------------- ----------------- ----------------- -----------------
  BUG01             Número pode ser   Alta              Aberto
                    selecionado duas                    
                    vezes                               

  BUG02             Falha na          Média             Corrigido
                    validação de                        
                    quantidade de                       
                    números                             
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 6. Avaliação Geral

O sistema apresenta comportamento adequado para as funcionalidades
principais.

Alguns defeitos foram identificados e registrados para correção.

------------------------------------------------------------------------

# 7. Conclusão

Com base nos testes executados, o sistema **Rifa Digital** está
funcional para os fluxos principais, porém algumas correções ainda são
necessárias antes da liberação final.
