class Transacao:
    
    identificador_conta = 0
    valor = 0
    
    def __init__(self, identificador_conta, valor):
        self.identificador_conta = identificador_conta
        self.valor = valor
    
    def __repr__(self):
        return "{0},{1}".format(
            self.identificador_conta, self.valor)
    