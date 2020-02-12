class Transacao:
    
    identificador_conta = 0
    e_debito = True
    __valor = 0
    
    def __init__(self, identificador_conta, valor):
        self.identificador_conta = identificador_conta
        self.__valor = valor
    
    def __repr__(self):
        return "{0},{1}".format(
            self.identificador_conta, self.valor)
    
    @property
    def valor(self):
        return self.__valor

    def _verifica_operacao(self):
        if self.__valor > 0:
            return True
        return False
