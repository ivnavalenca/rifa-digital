# Requisitos do Sistema

Este documento apresenta os requisitos do sistema **Rifa Digital**, descrevendo as funcionalidades e características necessárias para o funcionamento da aplicação.

---

# 1. Requisitos Funcionais

Os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer aos usuários.

RF01 - O sistema deve permitir criar uma campanha de rifa.

RF02 - O sistema deve permitir visualizar informações da rifa.

RF03 - O sistema deve exibir os números disponíveis da rifa.

RF04 - O sistema deve permitir selecionar um número da rifa.

RF05 - O sistema deve registrar os dados do comprador do número.

RF06 - O sistema deve registrar o pagamento associado ao número da rifa.

RF07 - O sistema deve marcar o número como vendido após confirmação do pagamento.

RF08 - O sistema deve permitir visualizar os números vendidos.

RF09 - O sistema deve exibir o progresso da venda dos números da rifa.

RF10 - O sistema deve realizar o sorteio da rifa.

RF11 - O sistema deve divulgar o resultado do sorteio.

RF12 - O sistema deve permitir compartilhar a rifa com outros usuários.

RF13 - O sistema deve permitir visualizar os compradores da rifa.

RF14 - O sistema deve permitir cancelar a reserva de um número.

RF15 - O sistema deve permitir visualizar o histórico da rifa.

---

# 2. Requisitos Não Funcionais

Os requisitos não funcionais descrevem características de qualidade, desempenho e segurança do sistema.

RNF01 - O sistema deve impedir que um mesmo número da rifa seja selecionado por mais de um usuário simultaneamente.

RNF02 - O sistema deve registrar logs das operações realizadas no sistema.

RNF03 - O sistema deve validar todos os dados enviados pelo usuário.

RNF04 - O sistema deve garantir integridade dos dados armazenados.

RNF05 - O sistema deve responder às requisições do usuário em até 2 segundos.

RNF06 - O sistema deve ser acessível através de dispositivos móveis e navegadores modernos.

RNF07 - O sistema deve proteger os dados pessoais dos usuários.

RNF08 - O sistema deve manter histórico das transações realizadas.

RNF09 - O sistema deve garantir disponibilidade do sistema durante o período da campanha da rifa.

---

# 3. Regras de Negócio

As regras de negócio definem restrições importantes do funcionamento da rifa.

RN01 - Cada número da rifa pode ser vendido apenas uma vez.

RN02 - Um número só pode ser considerado vendido após confirmação do pagamento.

RN03 - O sorteio da rifa deve ocorrer na data definida pelo organizador.

RN04 - O resultado do sorteio deve ser registrado e exibido no sistema.

RN05 - Apenas o organizador da rifa pode gerenciar informações da campanha.

---

# 4. Relação com as User Stories

Os requisitos funcionais estão diretamente relacionados às User Stories do backlog.

| Requisito | User Story |
|----------|-----------|
RF01 | US01 |
RF02 | US02 |
RF03 | US03 |
RF04 | US04 |
RF05 | US05 |
RF06 | US06 |
RF07 | US07 |
RF08 | US08 |
RF09 | US09 |
RF10 | US10 |
RF11 | US11 |
RF12 | US12 |
RF13 | US13 |
RF14 | US14 |
RF15 | US15 |

---

# 5. Observações

Este documento serve como base para o desenvolvimento do sistema e está alinhado com o backlog definido no projeto.
