
def mochila_fracionada(lista_ordenada:list, n, totalmochila):
    lista_ordenada.sort(reverse=True)
    carga = 0
    i = 1
    item_pegados = []
    while(carga < totalmochila and i < n):
      if lista_ordenada[i].peso <= (totalmochila - carga):
        item_pegados.append(lista_ordenada[i])
        carga = carga + lista_ordenada[i].peso
      else:
        carga_restante = totalmochila-carga
        lista_ordenada[i].valor = lista_ordenada[i].valor * (carga_restante / lista_ordenada[i].peso)
        lista_ordenada[i].peso = carga_restante / lista_ordenada[i].peso
        item_pegados.append(lista_ordenada[i])
        carga = carga + carga_restante/lista_ordenada[i].peso
      i = i + 1
    print(carga)
    return item_pegados