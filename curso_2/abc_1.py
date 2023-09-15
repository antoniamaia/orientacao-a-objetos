from abc import ABC 
from collections.abc import MutableSequence
# Abstract Base Classes - classes Abstratas para reforçar para que se comporte como esperado
from numbers import Complex

class Playlist(MutableSequence):
    pass

filmes = Playlist()

class Numero(Complex):
    pass

filmes = Playlist()