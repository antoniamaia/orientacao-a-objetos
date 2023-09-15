class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

# Outro uso comum de herança múltipla é quando você tem aspectos não-funcionais 
# usados por múltiplas classes. Para compartilhar estes comportamentos, você pode 
# usar Mixins, que são apenas classes que podem ser herdadas mas que não devem 
# ser instanciadas, já que servem para disponibilizar comportamentos para outras classes.    

class Junior(Alura):
    pass

# Herança multipla
class Pleno(Alura, Caelum, Hipster):
    pass

jose = Junior("José")
jose.busca_perguntas_sem_resposta()

luan = Pleno("Luan ")
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()

print(luan)