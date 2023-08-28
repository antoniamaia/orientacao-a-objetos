

class Conta:
    
    # Função construtora // se há __ -> funções com "significado especial"//(self) referencia objeto
    # __ encapsula o acesso dos atributos -> somente a partir dos métodos
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}.".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Funções específicas -> método //  utiliza parametro (self) referência do obj
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    # Parâmetro valor utilizado para podermos definir o valor a mais ou menos na conta
    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)    



    # Há a possibilidade de criar variaveis identicas, perdendo a referência do objeto, 
    # para isso o python possui a função `garbage collector´

    # None - pode ser utilizado caso tenham mais referências (xerox), que não quer mais utilizar