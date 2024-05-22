class Ingresso():
    def __init__(self, valor):
        self.valorIngresso= valor

    def imprimirValor(self):
        print(f"O valor do ingresso é R${self.valorIngresso}")

class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
    def imprimirValor(self):
        ingressoVip = self.valorIngresso * 1.5
        print(f"O valor do igresso VIP é R${ingressoVip}")
