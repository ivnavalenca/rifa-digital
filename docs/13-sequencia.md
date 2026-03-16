# Diagrama de Sequência --- Compra de Número

Este diagrama representa o fluxo de interação para a compra de um número
da rifa.

Participante → Frontend → Backend → Banco de Dados

Fluxo:

1.  Participante acessa página da rifa.
2.  Frontend solicita números disponíveis ao backend.
3.  Backend consulta banco de dados.
4.  Sistema retorna números disponíveis.
5.  Participante escolhe um número.
6.  Frontend envia dados ao backend.
7.  Backend registra comprador.
8.  Backend atualiza status do número.
9.  Banco de dados salva alterações.
