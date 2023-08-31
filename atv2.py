class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_valor(self):
        return self.preco

class Produto(Item):
    def __init__(self, nome, preco, quant):
        self.quant = quant
        super().__init__(nome, preco)

    def calcular_valor(self):
        return self.preco * self.quant

class Servico(Item):
    def __init__(self, nome, preco, horas):
        self.horas = horas
        super().__init__(nome, preco)

    def calcular_valor(self):
        return self.preco * self.horas

produto = Produto("tenis", 15, 30)
servico = Servico("entregador", 100, 5)

print(f"Valor do produto {produto.nome}: R${produto.calcular_valor()}")
print(f"Valor do serviço {servico.nome}: R${servico.calcular_valor()}")
