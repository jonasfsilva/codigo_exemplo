class Conta:

    identificador = 0
    saldo = 0
    
    def __init__(self, identificador, saldo):
        self.identificador = identificador
        self.saldo = saldo

    def __repr__(self):
        return "{0},{1}".format(
            self.identificador, self.saldo)    

    def adicionar_saldo(self):
        pass

    def remover_saldo(self):
        pass

    def executa_transacao(self):
        pass

    def aplica_multa(self):
        pass
