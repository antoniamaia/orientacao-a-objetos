class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

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

    # Poderia ser como abaixo, utilizando polimorfismo? Sim
    #
    # def imprime(self):
    #     print(f" {self._nome} - {self.ano} - {self._likes}")
    #
    # Mas também podemos utilizar os Dunder methods (métodos especiais) - Representar objetos textuais

    def __str__(self) -> str:
        return f" {self._nome} - {self.ano} - {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):   
        pass

    # Polimorfismo 
    def __str__(self):
        return f" {self._nome} - {self.ano} - {self.duracao}min - {self._likes}"    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f" {self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}"


vingadores = Filme("vingadores - Guera Infinita", 2018, 160)
vingadores.dar_like()
print(f"{vingadores.nome} -{vingadores.ano} - {vingadores.duracao}- : {vingadores.likes}")

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like() 
atlanta.dar_like() 
print(f" {atlanta.nome} - {atlanta.ano} -  {atlanta.temporadas} : {atlanta.likes}")

#Herança -> classes filhas são do mesmo tipo que a classe mãe - objetos são da classe Programa
# polimorfismo = como tem a mesma estrutura posso utilizar os dois tipos no for

filmes_e_series = [vingadores, atlanta]

# Poderia esrever assim? sim! mas podemos utilizar Polimorfismo!!
# for programa in filmes_e_series:
#     #verificação de atributo     |_____________________if ternário_____________________|  
#     detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
#     print(f" {programa.nome} - {programa.ano} -  D {detalhes} : {programa.likes}")

for programa in filmes_e_series:
    print(programa)