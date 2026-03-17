# Schema SQL --- Rifa Digital

Este documento apresenta o **schema SQL** do banco de dados do sistema
**Rifa Digital**.

O schema representa a implementação física do **modelo relacional** no
banco de dados. Ele define:

-   tabelas
-   chaves primárias
-   chaves estrangeiras
-   tipos de dados
-   regras de integridade

------------------------------------------------------------------------

# Estrutura do Banco de Dados

O banco de dados é composto pelas seguintes tabelas:

-   rifa
-   numero
-   participante
-   reserva
-   pagamento
-   sorteio

------------------------------------------------------------------------

# Tabela RIFA

``` sql
CREATE TABLE rifa (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    valor_numero DECIMAL(10,2) NOT NULL,
    quantidade_numeros INTEGER NOT NULL,
    data_sorteio DATE,
    status VARCHAR(20)
);
```

------------------------------------------------------------------------

# Tabela NUMERO

``` sql
CREATE TABLE numero (
    id SERIAL PRIMARY KEY,
    numero INTEGER NOT NULL,
    status VARCHAR(20) DEFAULT 'disponivel',
    rifa_id INTEGER NOT NULL,
    
    CONSTRAINT fk_rifa
        FOREIGN KEY (rifa_id)
        REFERENCES rifa(id)
);
```

------------------------------------------------------------------------

# Tabela PARTICIPANTE

``` sql
CREATE TABLE participante (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(120)
);
```

------------------------------------------------------------------------

# Tabela RESERVA

``` sql
CREATE TABLE reserva (
    id SERIAL PRIMARY KEY,
    data_reserva TIMESTAMP NOT NULL,
    status VARCHAR(20),
    numero_id INTEGER NOT NULL,
    participante_id INTEGER NOT NULL,

    CONSTRAINT fk_numero
        FOREIGN KEY (numero_id)
        REFERENCES numero(id),

    CONSTRAINT fk_participante
        FOREIGN KEY (participante_id)
        REFERENCES participante(id)
);
```

------------------------------------------------------------------------

# Tabela PAGAMENTO

``` sql
CREATE TABLE pagamento (
    id SERIAL PRIMARY KEY,
    data_pagamento TIMESTAMP,
    valor DECIMAL(10,2),
    status VARCHAR(20),
    reserva_id INTEGER NOT NULL,

    CONSTRAINT fk_reserva
        FOREIGN KEY (reserva_id)
        REFERENCES reserva(id)
);
```

------------------------------------------------------------------------

# Tabela SORTEIO

``` sql
CREATE TABLE sorteio (
    id SERIAL PRIMARY KEY,
    data_sorteio TIMESTAMP,
    numero_vencedor INTEGER,
    rifa_id INTEGER NOT NULL,

    CONSTRAINT fk_rifa_sorteio
        FOREIGN KEY (rifa_id)
        REFERENCES rifa(id)
);
```

------------------------------------------------------------------------

# Índices Recomendados

Para melhorar a performance das consultas, alguns índices podem ser
criados:

``` sql
CREATE INDEX idx_numero_rifa
ON numero(rifa_id);

CREATE INDEX idx_reserva_numero
ON reserva(numero_id);

CREATE INDEX idx_reserva_participante
ON reserva(participante_id);
```

------------------------------------------------------------------------

# Regras de Integridade

O banco de dados garante:

-   integridade referencial entre tabelas
-   consistência dos dados
-   controle das relações entre entidades

Principais regras:

-   um número pertence a apenas uma rifa
-   uma reserva está associada a um número e a um participante
-   um pagamento está associado a uma reserva
-   cada rifa possui um sorteio final

------------------------------------------------------------------------

# Relação com Outros Documentos

Este documento está relacionado com:

-   `conceptual/mer.md` --- modelo conceitual
-   `logical/modelo-relacional.md` --- modelo relacional
-   `dictionary/dicionario-dados.md` --- descrição detalhada dos campos

O schema SQL representa a **implementação final da arquitetura de
dados**.
