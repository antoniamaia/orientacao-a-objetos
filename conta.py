

class Conta:
    
    # Função construtora // se há __ -> funções com "significado especial"//(self) referencia objeto
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}.".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite