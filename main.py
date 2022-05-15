from mochilaFracionada import mochila_fracionada, print_mochila
from mochilaForcabruta import mochila_forca_bruta
from Item import Item
import time
import json

with open("skyrim_itens.json", encoding='utf-8') as skyrim_itens:
    dados = json.load(skyrim_itens)



itens = []
for dado in dados:
  if dado['Weight'] != 0:
    itens.append(Item(dado['Weight'],dado['Gold'],dado['Name']))

print(len(itens))


totalmochila=300
n = len(itens)

print("-----Algoritmo guloso para mochila fracionada-----------")
tempo_ini = time.time()
mochila = mochila_fracionada(itens,n, totalmochila)
tempo_fim = time.time()
print(f"tempode de execução: {tempo_fim-tempo_ini}")
valor_mochila = 0
carga_total = 0
for item in mochila:
    print("item: {:<30} peso: {:<5} de {:<5} valor: {:<5} de {:<5}".format(item.item, round(item.get_valor(),2), 
                                                            item.peso_aux,round(item.get_valor(),2), item.valor_aux))
    valor_mochila = valor_mochila + item.valor
    carga_total = carga_total + item.peso

print(carga_total)
print("valor da mochilha: {}".format(round(valor_mochila,2)) )  


print("-------Algoritmo força bruta mochila")
tempo_ini = time.time()
print(mochila_forca_bruta(itens,n,totalmochila))
tempo_fim = time.time()

