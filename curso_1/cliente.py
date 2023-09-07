
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    # tirar o get, para ser acionado como uma propriedade, sem uso dos () para chamar
    # colocar a mesma nomenclatura do atributo
    #getter
    def nome(self): 
        print("chamando @property nome()")
        return self.__nome.title()
    
    #setter
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome