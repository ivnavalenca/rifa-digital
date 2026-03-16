# Casos de Teste — Rifa Digital

Este documento apresenta a organização dos **casos de teste** do sistema **Rifa Digital**.

Os casos de teste foram derivados das **User Stories** definidas no backlog do projeto e têm como objetivo validar se os requisitos funcionais e não funcionais estão corretamente implementados.

Cada **User Story** possui múltiplos **Casos de Teste (CT)** que verificam:

- fluxo principal da funcionalidade
- validação de entradas
- regras de negócio
- cenários alternativos ou de erro

---

# Identificação dos Casos de Teste

Os casos de teste utilizam identificação sequencial global:

CT001, CT002, CT003, ...

Essa abordagem facilita:

- rastreabilidade
- organização dos testes
- manutenção futura

A relação entre artefatos segue o modelo:

Requisito → User Story → Caso de Teste

Exemplo:

RF01 → US01 → CT001–CT005

---

# Localização dos Casos de Teste

Os casos de teste detalhados estão organizados na pasta:

docs/testes/

Cada caso de teste é armazenado em um arquivo `.md` individual.

---

# Distribuição dos Casos de Teste

| User Story | Casos de Teste |
|---|---|
| US01 | CT001–CT005 |
| US02 | CT006–CT010 |
| US03 | CT011–CT015 |
| US04 | CT016–CT020 |
| US05 | CT021–CT025 |
| US06 | CT026–CT030 |
| US07 | CT031–CT035 |
| US08 | CT036–CT040 |
| US09 | CT041–CT045 |
| US10 | CT046–CT050 |
| US11 | CT051–CT055 |
| US12 | CT056–CT060 |
| US13 | CT061–CT065 |
| US14 | CT066–CT070 |
| US15 | CT071–CT075 |

---

# Estrutura de Arquivos

docs  
└ testes  
   ├ CT001-US01-criar-rifa-valido.md  
   ├ CT002-US01-criar-rifa-sem-nome.md  
   ├ CT003-US01-criar-rifa-sem-quantidade.md  
   ├ CT004-US01-criar-rifa-valor-invalido.md  
   ├ CT005-US01-criar-rifa-sem-data.md  
   └ ...

---

# Cobertura de Testes

Os casos de teste cobrem:

- funcionalidades principais do sistema
- validações de entrada
- regras de negócio
- cenários alternativos
- requisitos não funcionais críticos

A rastreabilidade completa entre requisitos, histórias de usuário e testes pode ser consultada em:

docs/19-matriz-rastreabilidade-testes.md
