

class Conta:
    
    # Função construtora // se há __ -> funções com "significado especial"//(self) referencia objeto
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}.".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # Funções específicas -> método //  utiliza parametro (self) referência do obj
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    # Parâmetro valor utilizado para podermos definir o valor a mais ou menos na conta
    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor



    # Há a possibilidade de criar variaveis identicas, perdendo a referência do objeto, 
    # para isso o python possui a função `garbage collector´

    # None - pode ser utilizado caso tenham mais referências (xerox), que não quer mais utilizar