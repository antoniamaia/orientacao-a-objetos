

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

    # Método privado, para ser acessado apenas quando a função é chamada, não fora
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # Métodos que somente retornam algo, GET = sempre tem retorno

    #def get_saldo(self):          \ 
    #    return self.__saldo        \ 
    #                                 podem ser apresentados desta forma ou |
    #def get_titular(self):         /                                       |
    #    return self.__titular     /                                        |

    
    #chamando "por debaixo dos panos" - podemos acessar o método da mesma forma que um atributo
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    

    # Métodos que podem receber mudanças = SET (não retorna algo/sempre muda)
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Código do banco, deveria ser acessado sem objeto 
    # -> métodos estáticos = métodos da classe, não do objeto
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return{"BB":"001", "Caixa":"104", "Bradesco":"237"}


    # Há a possibilidade de criar variaveis identicas, perdendo a referência do objeto, 
    # para isso o python possui a função `garbage collector´

    # None - pode ser utilizado caso tenham mais referências (xerox), que não quer mais utilizar