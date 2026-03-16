
# Schema SQL — Rifa Digital

Este documento apresenta o **schema SQL (DDL)** do banco de dados do sistema **Rifa Digital**.

O script SQL é derivado do **Modelo Relacional** e representa o **nível físico da modelagem de dados**, contendo a definição das tabelas, chaves primárias, chaves estrangeiras e restrições de integridade.

---

# 1. Criação do Banco de Dados

```sql
CREATE DATABASE rifa_digital;
```

Selecionar o banco:

```sql
USE rifa_digital;
```

---

# 2. Tabela RIFA

Armazena informações sobre cada campanha de rifa.

```sql
CREATE TABLE rifa (
    id_rifa INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    data_sorteio DATE NOT NULL,
    valor_numero DECIMAL(10,2) NOT NULL,
    quantidade_numeros INT NOT NULL,
    status VARCHAR(30) DEFAULT 'ativa',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 3. Tabela NUMERO

Armazena os números disponíveis de cada rifa.

```sql
CREATE TABLE numero (
    id_numero INT PRIMARY KEY AUTO_INCREMENT,
    numero INT NOT NULL,
    status VARCHAR(20) DEFAULT 'disponivel',
    id_rifa INT NOT NULL,

    CONSTRAINT fk_numero_rifa
        FOREIGN KEY (id_rifa)
        REFERENCES rifa(id_rifa)
        ON DELETE CASCADE
);
```

Relacionamento:

```
RIFA (1) ---- (N) NUMERO
```

---

# 4. Tabela PARTICIPANTE

Armazena os participantes da rifa.

```sql
CREATE TABLE participante (
    id_participante INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 5. Tabela RESERVA

Representa a reserva de um número por um participante.

```sql
CREATE TABLE reserva (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    data_reserva DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'reservado',
    id_numero INT NOT NULL,
    id_participante INT NOT NULL,

    CONSTRAINT fk_reserva_numero
        FOREIGN KEY (id_numero)
        REFERENCES numero(id_numero),

    CONSTRAINT fk_reserva_participante
        FOREIGN KEY (id_participante)
        REFERENCES participante(id_participante)
);
```

Relacionamentos:

```
NUMERO (1) ---- (0..1) RESERVA
PARTICIPANTE (1) ---- (N) RESERVA
```

---

# 6. Tabela PAGAMENTO

Representa o pagamento associado a uma reserva.

```sql
CREATE TABLE pagamento (
    id_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    valor DECIMAL(10,2) NOT NULL,
    data_pagamento DATETIME,
    metodo_pagamento VARCHAR(50),
    status VARCHAR(20) DEFAULT 'pendente',
    id_reserva INT UNIQUE,

    CONSTRAINT fk_pagamento_reserva
        FOREIGN KEY (id_reserva)
        REFERENCES reserva(id_reserva)
);
```

Relacionamento:

```
RESERVA (1) ---- (1) PAGAMENTO
```

---

# 7. Índices

Índices são utilizados para melhorar o desempenho das consultas.

```sql
CREATE INDEX idx_numero_rifa
ON numero(id_rifa);

CREATE INDEX idx_reserva_participante
ON reserva(id_participante);

CREATE INDEX idx_reserva_numero
ON reserva(id_numero);
```

---

# 8. Regras de Integridade

O banco de dados implementa:

### Integridade de Entidade

Garantida pelas **chaves primárias (PRIMARY KEY)**.

Exemplo:

```
id_rifa
id_numero
id_participante
id_reserva
id_pagamento
```

---

### Integridade Referencial

Garantida pelas **chaves estrangeiras (FOREIGN KEY)**.

Principais vínculos:

```
numero.id_rifa → rifa.id_rifa
reserva.id_numero → numero.id_numero
reserva.id_participante → participante.id_participante
pagamento.id_reserva → reserva.id_reserva
```

---

# 9. Script Completo Consolidado

```sql
CREATE DATABASE rifa_digital;
USE rifa_digital;

CREATE TABLE rifa (
    id_rifa INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    data_sorteio DATE NOT NULL,
    valor_numero DECIMAL(10,2) NOT NULL,
    quantidade_numeros INT NOT NULL,
    status VARCHAR(30) DEFAULT 'ativa',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE numero (
    id_numero INT PRIMARY KEY AUTO_INCREMENT,
    numero INT NOT NULL,
    status VARCHAR(20) DEFAULT 'disponivel',
    id_rifa INT NOT NULL,
    FOREIGN KEY (id_rifa) REFERENCES rifa(id_rifa)
);

CREATE TABLE participante (
    id_participante INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reserva (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    data_reserva DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'reservado',
    id_numero INT NOT NULL,
    id_participante INT NOT NULL,
    FOREIGN KEY (id_numero) REFERENCES numero(id_numero),
    FOREIGN KEY (id_participante) REFERENCES participante(id_participante)
);

CREATE TABLE pagamento (
    id_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    valor DECIMAL(10,2) NOT NULL,
    data_pagamento DATETIME,
    metodo_pagamento VARCHAR(50),
    status VARCHAR(20) DEFAULT 'pendente',
    id_reserva INT UNIQUE,
    FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva)
);
```

---

# 10. Fluxo da Modelagem de Dados

O schema SQL é o último nível da modelagem de dados.

```
MER (Modelo Conceitual)
        ↓
Modelo Relacional (Modelo Lógico)
        ↓
Schema SQL (Modelo Físico)
        ↓
Banco de Dados
```

Este fluxo representa o processo clássico de **engenharia de dados em bancos relacionais**.
