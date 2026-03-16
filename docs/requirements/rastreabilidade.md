# Rastreabilidade de Requisitos --- Rifa Digital

Este documento apresenta a rastreabilidade entre requisitos, épicos,
user stories, tasks e bugs do projeto **Rifa Digital**.

A rastreabilidade permite acompanhar como cada requisito do sistema está
relacionado com os elementos do backlog e com a implementação do
sistema.

------------------------------------------------------------------------

# 1. Rastreabilidade de Requisitos Funcionais
```
  -----------------------------------------------------------------------
  Requisito                  Épico           User Story
  -------------------------- --------------- ----------------------------
  RF01                       E01 - Gestão da US01 - Criar campanha de
                             Rifa            rifa

  RF02                       E01 - Gestão da US02 - Visualizar
                             Rifa            informações da rifa

  RF03                       E02 - Compra de US03 - Visualizar números
                             Números         disponíveis

  RF04                       E02 - Compra de US04 - Escolher número da
                             Números         rifa

  RF05                       E02 - Compra de US05 - Registrar comprador
                             Números         

  RF06                       E03 - Pagamento US06 - Registrar pagamento

  RF07                       E02 - Compra de US07 - Marcar número como
                             Números         vendido

  RF08                       E03 - Pagamento US08 - Visualizar números
                                             vendidos

  RF09                       E03 - Pagamento US09 - Visualizar progresso
                                             da rifa

  RF10                       E04 - Sorteio   US10 - Realizar sorteio

  RF11                       E04 - Sorteio   US11 - Divulgar resultado

  RF12                       E01 - Gestão da US12 - Compartilhar rifa
                             Rifa            

  RF13                       E04 - Sorteio   US13 - Visualizar
                                             compradores

  RF14                       E04 - Sorteio   US14 - Cancelar reserva

  RF15                       E01 - Gestão da US15 - Visualizar histórico
                             Rifa            da rifa
  -----------------------------------------------------------------------
```
------------------------------------------------------------------------

# 2. Rastreabilidade de Requisitos Não Funcionais
```
  Requisito Não Funcional                         Relacionamento
  ----------------------------------------------- ----------------
  RNF01 - Impedir seleção simultânea de números   US04
  RNF02 - Registro de logs                        Backend
  RNF03 - Validação de dados                      US04, US05
  RNF04 - Integridade de dados                    Banco de dados
  RNF05 - Tempo de resposta adequado              Arquitetura
  RNF06 - Acesso por dispositivos móveis          Frontend
  RNF07 - Proteção de dados pessoais              Segurança
  RNF08 - Histórico de transações                 US15
```
------------------------------------------------------------------------

# 3. Rastreabilidade com Tasks
```
  User Story   Tasks
  ------------ -------------------------
  US01         T01, T02, T03, T04, T05
  US03         T06, T07
  US04         T08, T09
  US05         T10
  US06         T11
  US10         T12
```
------------------------------------------------------------------------

# 4. Rastreabilidade com Bugs
```
  Bug                        Requisito   User Story
  -------------------------- ----------- ------------
  BUG01 - Número duplicado   RNF01       US04
```
------------------------------------------------------------------------

# 5. Visão Geral da Rastreabilidade

Requisitos ↓ Épicos ↓ User Stories ↓ Tasks ↓ Bugs

Exemplo:

RNF01 - Impedir duplicação de números\
↓\
US04 - Escolher número da rifa\
↓\
BUG01 - Número da rifa pode ser selecionado duas vezes

------------------------------------------------------------------------

# 6. Benefícios da Rastreabilidade

-   Facilita a gestão do backlog.
-   Permite identificar rapidamente impactos de mudanças.
-   Auxilia na verificação de cobertura de requisitos.
-   Conecta documentação, desenvolvimento e testes.

------------------------------------------------------------------------

# 7. Observações

Este documento deve ser atualizado sempre que novos requisitos, user
stories, tasks ou bugs forem adicionados ao projeto.
