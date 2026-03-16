# Personas

As personas representam os principais perfis de usuários que interagem com o sistema de Rifa Digital. Elas ajudam a compreender necessidades, objetivos e possíveis riscos no uso da aplicação.

---

# 👩 Persona 1 — Organizador da Rifa

**Nome:** Ana Organizadora  
**Idade:** 35 anos  
**Profissão:** Professora  
**Perfil:** Usuária responsável por criar e administrar campanhas de rifa.

## Contexto

Ana organiza rifas para arrecadar recursos para eventos escolares, projetos comunitários ou viagens educacionais.

## Objetivos

- Criar uma campanha de rifa facilmente
- Definir quantidade de números disponíveis
- Registrar compradores
- Controlar pagamentos
- Realizar o sorteio da rifa

## Dores (Problemas)

- Controle manual de números vendidos
- Falta de organização das vendas
- Risco de vender o mesmo número duas vezes
- Dificuldade em acompanhar pagamentos

## Como o sistema ajuda

O sistema permite criar rifas, controlar automaticamente os números vendidos e registrar os compradores e pagamentos.

---

# 👨 Persona 2 — Participante da Rifa

**Nome:** Carlos Participante  
**Idade:** 28 anos  
**Profissão:** Analista de TI  
**Perfil:** Usuário interessado em participar de rifas e escolher um número.

## Contexto

Carlos participa de rifas organizadas por amigos ou instituições e deseja um processo rápido e transparente para escolher seu número.

## Objetivos

- Visualizar números disponíveis
- Escolher um número da rifa
- Confirmar sua participação
- Acompanhar o resultado do sorteio

## Dores (Problemas)

- Não saber quais números estão disponíveis
- Falta de confirmação da compra
- Falta de transparência no sorteio

## Como o sistema ajuda

O sistema mostra os números disponíveis em tempo real, registra a participação do usuário e divulga o resultado do sorteio.

---

# ⚠️ Persona 3 — Usuário Mal-Intencionado (Abuser Persona)

**Nome:** Marcos Fraudador  
**Idade:** 30 anos  
**Perfil:** Usuário que tenta explorar falhas do sistema para obter vantagens ou causar problemas.

## Contexto

Marcos pode tentar manipular o sistema para reservar múltiplos números, registrar pagamentos falsos ou explorar falhas de validação.

## Objetivos

- Selecionar o mesmo número mais de uma vez
- Manipular informações da rifa
- Explorar falhas do sistema
- Fraudar o processo de compra ou sorteio

## Possíveis Ações Maliciosas

- Enviar múltiplas requisições para reservar o mesmo número
- Manipular dados no navegador
- Tentar registrar pagamentos falsos
- Acessar dados de outros usuários

## Riscos para o Sistema

- Venda duplicada de números
- Inconsistência no sorteio
- Perda de confiança dos participantes
- Possível vazamento de dados

## Como o sistema deve se proteger

- Validação no backend para impedir números duplicados
- Controle de concorrência na reserva de números
- Registro de logs das operações
- Validação de pagamentos
- Controle de acesso e autenticação

---

# Relação com Requisitos e Bugs

A persona mal-intencionada ajuda a identificar possíveis falhas no sistema e inspira a criação de requisitos de segurança e correções de bugs.

Exemplo:

Persona mal-intencionada  
↓  
BUG01 — Número da rifa pode ser selecionado duas vezes  
↓  
Requisito: impedir duplicação de números.
