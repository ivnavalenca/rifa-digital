# Dicionário de Dados --- Rifa Digital

Este documento descreve detalhadamente os campos de cada tabela do banco
de dados do sistema **Rifa Digital**.

------------------------------------------------------------------------

# 1. Tabela: RIFA

Armazena informações sobre cada campanha de rifa.

  Campo                Tipo            Obrigatório   Descrição
  -------------------- --------------- ------------- ------------------------------------
  id                   INTEGER         sim           Identificador único da rifa
  nome                 VARCHAR(150)    sim           Nome da campanha de rifa
  descricao            TEXT            sim           Descrição da rifa
  valor_numero         DECIMAL(10,2)   sim           Valor de cada número
  quantidade_numeros   INTEGER         sim           Total de números disponíveis
  data_sorteio         DATE            sim           Data prevista para o sorteio
  status               VARCHAR(20)     sim           Status da rifa (aberta, encerrada)

------------------------------------------------------------------------

# 2. Tabela: NUMERO

Armazena os números disponíveis para cada rifa.

  -----------------------------------------------------------------------
  Campo             Tipo              Obrigatório       Descrição
  ----------------- ----------------- ----------------- -----------------
  id                INTEGER           sim               Identificador do
                                                        número

  numero            INTEGER           sim               Número da rifa

  status            VARCHAR(20)       sim               Status do número
                                                        (disponível,
                                                        reservado,
                                                        vendido)

  rifa_id           INTEGER           sim               Identificador da
                                                        rifa associada
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 3. Tabela: COMPRADOR

Armazena os dados do participante que compra números da rifa.

  Campo      Tipo           Obrigatório   Descrição
  ---------- -------------- ------------- ----------------------------
  id         INTEGER        sim           Identificador do comprador
  nome       VARCHAR(150)   sim           Nome do participante
  telefone   VARCHAR(20)    sim           Telefone do participante
  email      VARCHAR(150)   não           Email do participante

------------------------------------------------------------------------

# 4. Tabela: RESERVA

Representa a reserva de um número antes da confirmação do pagamento.

  Campo          Tipo          Obrigatório   Descrição
  -------------- ------------- ------------- --------------------------------------
  id             INTEGER       sim           Identificador da reserva
  data_reserva   TIMESTAMP     sim           Data e hora da reserva
  status         VARCHAR(20)   sim           Status da reserva (ativa, cancelada)
  numero_id      INTEGER       sim           Número reservado
  comprador_id   INTEGER       sim           Comprador que realizou a reserva

------------------------------------------------------------------------

# 5. Tabela: PAGAMENTO

Registra os pagamentos realizados para confirmar a compra de um número.

  -----------------------------------------------------------------------
  Campo             Tipo              Obrigatório       Descrição
  ----------------- ----------------- ----------------- -----------------
  id                INTEGER           sim               Identificador do
                                                        pagamento

  valor             DECIMAL(10,2)     sim               Valor pago

  data_pagamento    DATE              sim               Data do pagamento

  status            VARCHAR(20)       sim               Status do
                                                        pagamento
                                                        (pendente,
                                                        confirmado)

  reserva_id        INTEGER           sim               Reserva associada
                                                        ao pagamento
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 6. Tabela: SORTEIO

Armazena informações sobre o sorteio da rifa.

  Campo             Tipo      Obrigatório   Descrição
  ----------------- --------- ------------- -------------------------------------
  id                INTEGER   sim           Identificador do sorteio
  data_sorteio      DATE      sim           Data em que o sorteio foi realizado
  numero_vencedor   INTEGER   sim           Número vencedor da rifa
  rifa_id           INTEGER   sim           Rifa associada ao sorteio

------------------------------------------------------------------------

# 7. Relacionamentos Principais

  Tabela Origem   Campo          Tabela Destino   Campo
  --------------- -------------- ---------------- -------
  numero          rifa_id        rifa             id
  reserva         numero_id      numero           id
  reserva         comprador_id   comprador        id
  pagamento       reserva_id     reserva          id
  sorteio         rifa_id        rifa             id

------------------------------------------------------------------------

# 8. Observações

Este dicionário de dados facilita:

-   entendimento do modelo de banco
-   implementação do banco de dados
-   manutenção do sistema
-   integração com outros sistemas
