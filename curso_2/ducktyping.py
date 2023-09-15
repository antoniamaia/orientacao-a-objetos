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

    def __str__(self) -> str:
        return f" {self._nome} - {self.ano} - {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):   
        pass

    def __str__(self):
        return f" {self._nome} - {self.ano} - {self.duracao}min - {self._likes} likes"    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f" {self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

# Método para transformar a classe em iterável sem utilizar herança
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
       
    def __len__(self):
        return len(self._programas)
    
    

vingadores = Filme("vingadores - Guera Infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("demolidor", 2016, 5)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like() 
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

print(vingadores in playlist_fim_de_semana)

# Ganhamos: 
for programa in playlist_fim_de_semana:
    print(programa)

print(vingadores in playlist_fim_de_semana)
print(playlist_fim_de_semana[0])
print(len(playlist_fim_de_semana))


    