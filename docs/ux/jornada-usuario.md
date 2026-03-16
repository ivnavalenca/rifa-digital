# Jornada do Usuário

A jornada do usuário descreve as etapas percorridas pelos diferentes perfis de usuários ao interagir com o sistema de Rifa Digital.

As jornadas foram definidas com base nas personas identificadas no documento de personas.

---

# 1. Jornada do Organizador da Rifa

Persona: Ana Organizadora

O organizador é responsável por criar e gerenciar uma campanha de rifa.

## Etapas da Jornada

1. Acessar o sistema de Rifa Digital.
2. Criar uma nova campanha de rifa.
3. Definir informações da rifa:
   - nome da rifa
   - descrição
   - quantidade de números
   - valor de cada número
   - data do sorteio
4. Publicar a rifa no sistema.
5. Compartilhar o link da rifa com possíveis participantes.
6. Acompanhar os números vendidos.
7. Registrar pagamentos recebidos.
8. Acompanhar o progresso da venda da rifa.
9. Realizar o sorteio na data definida.
10. Divulgar o resultado da rifa.

## User Stories relacionadas

US01 - Criar campanha de rifa  
US02 - Visualizar informações da rifa  
US06 - Registrar pagamento  
US09 - Visualizar progresso da rifa  
US10 - Realizar sorteio  
US11 - Divulgar resultado  
US12 - Compartilhar rifa  
US15 - Visualizar histórico da rifa

---

# 2. Jornada do Participante da Rifa

Persona: Carlos Participante

O participante deseja escolher um número da rifa e acompanhar o resultado do sorteio.

## Etapas da Jornada

1. Receber o link da rifa.
2. Acessar a página da rifa.
3. Visualizar informações da rifa.
4. Visualizar os números disponíveis.
5. Escolher um número da rifa.
6. Informar seus dados pessoais.
7. Confirmar a reserva do número.
8. Realizar o pagamento do número.
9. Aguardar o sorteio.
10. Visualizar o resultado do sorteio.

## User Stories relacionadas

US02 - Visualizar informações da rifa  
US03 - Visualizar números disponíveis  
US04 - Escolher número da rifa  
US05 - Registrar comprador  
US06 - Registrar pagamento  
US11 - Divulgar resultado

---

# 3. Jornada do Usuário Mal-Intencionado

Persona: Marcos Fraudador

Este usuário tenta explorar falhas no sistema para obter vantagens ou causar inconsistências.

## Possíveis ações maliciosas

1. Tentar selecionar o mesmo número da rifa várias vezes.
2. Enviar múltiplas requisições simultâneas para reservar números.
3. Manipular dados enviados pelo navegador.
4. Tentar registrar pagamentos falsos.
5. Tentar acessar dados de outros participantes.

## Riscos identificados

- Venda duplicada de números.
- Inconsistência no sorteio.
- Falhas de integridade dos dados.

## Medidas de proteção do sistema

- Validação de dados no backend.
- Controle de concorrência na reserva de números.
- Registro de logs de operações.
- Verificação de pagamentos.
- Controle de acesso e autenticação.

## Bugs e requisitos relacionados

BUG01 - Número da rifa pode ser selecionado duas vezes  
RNF01 - O sistema deve impedir que um número seja selecionado por dois usuários simultaneamente.

---

# 4. Visão Geral da Jornada

Fluxo principal do sistema:

Organizador cria rifa  
↓  
Participantes acessam a rifa  
↓  
Participantes escolhem números  
↓  
Pagamentos são registrados  
↓  
Sistema acompanha progresso da rifa  
↓  
Sorteio é realizado  
↓  
Resultado é divulgado

---

# 5. Observações

A jornada do usuário ajuda a compreender a experiência dos diferentes perfis que interagem com o sistema e orienta a definição de requisitos, funcionalidades e melhorias do produto.
