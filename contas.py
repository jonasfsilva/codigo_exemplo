class Conta:

    __identificador = 0
    __saldo = 0
    
    def __init__(self, identificador, saldo):
        self.__identificador = identificador
        self.__saldo = saldo

    def __repr__(self):
        return "{0},{1}".format(
            self.__identificador, self.saldo)    

    @property
    def saldo(self):
        return self.__saldo

    def adicionar_saldo(self):
        pass

    def remover_saldo(self):
        pass

    def executa_transacao(self, transacao):
        pass

    def aplica_multa(self):
        pass
