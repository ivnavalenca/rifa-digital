
# AI Engineering Assistant

O **AI Engineering Assistant** é uma ferramenta dentro do portal de engenharia
que permite consultar informações sobre a arquitetura, requisitos e testes do
sistema **Rifa Digital**.

Ele funciona como um assistente que ajuda a navegar pela documentação técnica
do projeto.

---

## Objetivo

O objetivo do assistente é facilitar:

- compreensão da arquitetura do sistema
- navegação entre requisitos e testes
- identificação de relações entre componentes
- exploração da documentação técnica

---

## Exemplos de Perguntas

O assistente pode responder perguntas como:

- Qual requisito está ligado ao RifaService?
- Quais testes validam o RF01?
- Quais componentes utilizam a tabela RIFA?
- Quais serviços fazem parte da arquitetura?

---

## Fonte de Conhecimento

O assistente utiliza como base:

- documentação de requisitos
- diagramas de arquitetura
- modelo de dados
- casos de teste
- relatórios de qualidade

Essas informações são organizadas em um **Knowledge Graph de engenharia**.

---

## Exemplo de Consulta

Pergunta:

> Quais testes validam o RF01?

Resposta esperada:

- CT001 – Criar rifa com dados válidos
- CT002 – Criar rifa sem informar nome
- CT003 – Criar rifa sem quantidade de números

---

## Integração com o Portal

O assistente está integrado com:

- Engineering Map
- Knowledge Graph
- Traceability Graph
- Architecture Explorer

Esses documentos permitem explorar as relações entre os artefatos do sistema.

---

## Evolução Futura

No futuro o assistente poderá:

- responder perguntas usando IA
- gerar novos casos de teste
- sugerir melhorias na arquitetura
- identificar inconsistências entre requisitos e testes

---

## Navegação Relacionada

- [Engineering Map](engineering-map.md)
- [Knowledge Graph](knowledge-graph.md)
- [Traceability Graph](traceability-graph.md)
- [Architecture Explorer](architecture-explorer.md)
