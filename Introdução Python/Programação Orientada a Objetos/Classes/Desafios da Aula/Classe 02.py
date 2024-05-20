class ContaBancaria():
    def __init__(self, numero_conta, nome_cliente, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_cliente = nome_cliente
        self.tipo_conta = tipo_conta
        self.saldo = 0
        self.statusConta = False
        self.limite = self.saldo

    def depositar(self, valor):
        if not self.statusConta:
            print("A conta está inativa. Ative a conta para realizar depósitos.")
        else:
            if valor <= 0:
                print("O valor do depósito deve ser positivo, tente novamente.")
            else:
                self.saldo += valor
                print(f"Depósito de R${valor} realizado com sucesso.")

    def sacar(self, valor):
        if not self.statusConta:
            print("Conta Inativa, impossivel realizar saque.")
        else:
            if valor > self.saldo:
                print("Saldo insuficiente")
            elif valor == 0:
                print("Não pode sacar R$ 0,00")
            else:
                print(f"Saque de R${valor} realizado com sucesso")
                self.saldo -= valor

    def verificarSaldo(self):
        if not self.statusConta:
            print("Conta Inativa, ative a conta para verificar saldo.")
        else:
            print(f"Saldo total é R${self.saldo}")

    def ativarConta(self):
        if  self.statusConta:
            print("Conta já está ativa")
        else:
            print("Conta ativada com sucesso, Bem-Vindo!")
            self.statusConta = True

    def desativarConta(self):
        if not self.statusConta:
            print("A conta ja está inativa")
        elif self.saldo > 0:
            print(f"Não pode desativar uma conta com saldo positivo, saque R${self.saldo} e tente novamente")
        else:
            print("Conta Desativada com sucesso")
            self.statusConta = False
