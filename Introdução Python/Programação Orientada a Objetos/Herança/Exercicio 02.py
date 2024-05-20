class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0
class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calcularArea(self, largura, altura):
        self.area = largura * altura
        print(f"A área é {self.area}")

    def calcularPerimetro(self, largura, altura):
        self.perimetro = 2 * (largura * altura)
        print(f"O perimetro é {self.perimetro}")

class Triangulo(Forma):
