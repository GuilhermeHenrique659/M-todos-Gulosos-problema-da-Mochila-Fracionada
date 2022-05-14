class Item:
    def __init__(self, peso, valor, item):
      self.item = item
      self.peso = peso
      self.valor = valor
      self.valorpeso = valor/peso
      self.valor_aux = valor
      self.peso_aux = peso
 
    def __lt__ (self, other):
        return self.valorpeso < other.valorpeso
    
    def get_valor(self):
        return (self.valor*100)/self.valor_aux