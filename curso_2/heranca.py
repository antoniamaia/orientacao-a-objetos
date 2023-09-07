# Criando uma classe "mãe", para questões que são comuns para ambas funções -> hierarquia
# __ privado --> não vai para a classe filha - convenção: utilizar apenas 1 _ para mostrar 
#                                              proteção, assim a classe filha consegue acessar o atributo 
# Classe Genérica
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Protegendo atributos:
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    @property
    def likes(self):
        return self._likes


    def dar_like(self):
        self._likes += 1

# No parâmetro da classe entra a classe mãe. (pode haver mais de uma classe herdada)
# recebe todos os métodos, atributos, propriedades.. reutiliza informações!
# Classes específicas, métodos exclusivos 
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # Classe mãe = SUPER -> para utilizar o que já vem com ela
        # extensão, sobreescreve o método init da classe Programa 
        super().__init__(nome, ano)
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):   
        pass
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas




# objetos


vingadores = Filme("vingadores - Guera Infinita", 2018, 160)
vingadores.dar_like()
print(f"{vingadores.nome} -{vingadores.ano} - {vingadores.duracao}- : {vingadores.likes}")

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like() 
atlanta.dar_like() 
print(f" {atlanta.nome} - {atlanta.ano} -  {atlanta.temporadas} : {atlanta.likes}")
