class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo= False, dormindo = False, falando =False):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comendo = comendo
        self.dormindo = dormindo
        self.falando = falando

    def comer(self, alimento):
        print(f"{self.nome} foi comer {alimento}")
        self.comendo= True
    def paradecomer(self):
        print(f"{self.nome} parou de comer ")
        self.comendo= False
    def dormir(self):
        print(f"{self.nome} está dormindo")
        self.dormindo = True
    def parardedormir(self):
        print(f"{self.nome} acordou")
        self.dormindo = False
    def falar(self):
        print(f"{self.nome} está falando")
        self.falando= True
    def paradefalar(self):
        print(f"{self.nome} parou de falar")
        self.falando = False