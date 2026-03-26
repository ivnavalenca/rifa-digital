# 🔗 Matriz de Rastreabilidade --- Rifa Digital

  ----------------------------------------------------------------------------------------
  RF     User Story    Caso de Uso    Endpoint / Código     Teste                Status
  ------ ------------- -------------- --------------------- -------------------- ---------
  RF01   US01          Criar Rifa     POST /rifas           test_create_rifa     ⬜

  RF02   US02          Visualizar     GET /rifas/{id}       test_get_rifa        ⬜
                       Rifa                                                      

  RF03   US03          Listar números GET                   test_list_numbers    ⬜
                                      /rifas/{id}/numeros                        

  RF04   US04          Escolher       POST /numeros/select  test_select_number   ⬜
                       número                                                    

  RF05   US05          Registrar      POST /comprador       test_buyer_data      ⬜
                       comprador                                                 

  RF06   US06          Registrar      POST /pagamento       test_payment         ⬜
                       pagamento                                                 

  RF07   US07          Marcar vendido PATCH /numeros        test_mark_sold       ⬜

  RF08   US08          Ver vendidos   GET /numeros/vendidos test_sold_numbers    ⬜

  RF09   US09          Progresso      GET /rifas/progresso  test_progress        ⬜

  RF10   US10          Sorteio        POST /rifas/sorteio   test_draw            ⬜

  RF11   US11          Resultado      GET /rifas/resultado  test_result          ⬜

  RF12   US12          Compartilhar   GET /rifas/link       test_share           ⬜

  RF13   US13          Compradores    GET /compradores      test_buyers          ⬜

  RF14   US14          Cancelar       DELETE /numeros       test_cancel          ⬜
                       reserva                                                   

  RF15   US15          Histórico      GET /rifas/historico  test_history         ⬜
  ----------------------------------------------------------------------------------------
