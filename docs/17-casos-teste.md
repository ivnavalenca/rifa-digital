# Casos de Teste --- Rifa Digital

Este documento apresenta cenários de teste para validar as
funcionalidades do sistema.
```
  -------------------------------------------------------------------------
  ID     User Story         Cenário       Resultado Esperado
  ------ ------------------ ------------- ---------------------------------
  CT01   US01               Criar nova    Rifa criada com sucesso
                            rifa          

  CT02   US04               Selecionar    Número reservado
                            número        
                            disponível    

  CT03   US04               Selecionar    Sistema impede duplicação
                            número já     
                            reservado     

  CT04   US06               Registrar     Número marcado como vendido
                            pagamento     

  CT05   US08               Realizar      Número vencedor selecionado
                            sorteio       
  -------------------------------------------------------------------------
```
------------------------------------------------------------------------

## Exemplo de Caso de Teste

**ID:** CT02\
**User Story:** US04 --- Escolher número da rifa

**Passos:**

1.  Acessar página da rifa
2.  Visualizar números disponíveis
3.  Selecionar um número
4.  Informar dados do participante

**Resultado esperado:**\
O número é reservado para o participante.
