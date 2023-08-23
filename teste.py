## Orientação à Objetos ##
# Tenho várias informações, para montar uma conta:
# >>> numero = 123
# >>> titular = "Nico"
# >>> saldo = 55.0
# >>> limite = 1000.0
# 
# Já descobrimos a forma mais fácil de apresentar: (Dict)
# >>> conta = {"numero": 123, "titular": "Nico", "saldo": 55.0, "limite": 1000.00}
# Para acessar o valor, ["chave"]:
# >>> conta["numero"]
# 123
# >>> conta["limite"]
# 1000.0
# >>> conta2 = {"numero": 321, "titular": "Marco", "saldo": 100.0, "limite": 1000.00}
# e se eu criar uma função que guarda tudo isso de uma vez só? 
# segue...


def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

# >>> from teste import cria_conta
# >>> conta = cria_conta(123, "Nico", 55.0, 1000.0)
# >>> conta["numero"]
# 123
# >>> conta["limite"]
# 1000.0

def deposita(conta, valor):
    conta["saldo"] += valor 

def saca(conta, valor):
    conta["saldo"] -= valor     

def extrato(conta):
    print("Seu saldo é de {}".format(conta["saldo"]))

# >>> from teste import cria_conta, deposita, saca, extrato
# >>> conta = cria_conta(123, "Nico", 55.0, 1000.0)
# >>> deposita(conta, 15.0)
# >>> extrato(conta)
# Seu saldo é de 70.0
# >>> saca(conta, 20.0)
# >>> extrato(conta)
# Seu saldo é de 50.0    //ainda procedural -> ligações frágeis/ruido de comunicação
# ainda assim é possivel depositar sem a função! >>> conta["saldo"] = conta ["saldo"] + 100.0 
#                                                    funcionaria, mas não queremos isso!!
