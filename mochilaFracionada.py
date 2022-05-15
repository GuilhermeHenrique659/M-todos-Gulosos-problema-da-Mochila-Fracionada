
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



def print_mochila(mochila):
    valor_mochila = 0
    carga_total = 0
    for item in mochila:
        print("item: {:<30} peso: {:<5} de {:<5} valor: {:<5} de {:<5}".format(item.item, round(item.get_valor(),2), 
                                                            item.peso_aux,round(item.get_valor(),2), item.valor_aux))
        valor_mochila = valor_mochila + item.valor
        carga_total = carga_total + item.peso

    print(carga_total)
    print("valor da mochilha: {}".format(round(valor_mochila,2)) )  