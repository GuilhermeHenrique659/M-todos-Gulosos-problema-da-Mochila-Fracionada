def mochila_forca_bruta(lista_itens:list, n, totalmochila):
    if n == 0 or totalmochila == 0:
      return 0
    
    if lista_itens[n-1].peso > totalmochila:
        return mochila_forca_bruta(lista_itens, n-1, totalmochila)
    else:
        return max(
            lista_itens[n-1].valor + mochila_forca_bruta(lista_itens, n-1, 
                                                          totalmochila-lista_itens[n-1].peso),
                                      mochila_forca_bruta(lista_itens, n-1, totalmochila)
        )