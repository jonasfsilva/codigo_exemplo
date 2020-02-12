import csv
from collections import OrderedDict 


class ManageOperations:

    contas_csv = ''
    transacoes_csv = ''
    contas = []
    transacoes = []

    def __init__(self, contas_csv, transacoes_csv):
        self.contas_csv = contas_csv
        self.transacoes_csv = transacoes_csv

    def read_csv(self, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                lines = OrderedDict() 
                lines[row[0]] = row[1]
        return lines

    def load_data(self):
        transacoes_lines = self.read_csv(self.transacoes_csv)
        contas_lines = self.read_csv(self.contas_csv)

        for conta in contas_lines:
            pass

        for transacao in transacoes_lines:
            pass
        
    def run(self):
        #contas que tem saldos
        #percorrer as transacoes pegar as contas e aplicar as transacoes

        for transacao in self.transacoes:
            for conta in self.contas:
                conta.identificadot = transacao.identificadot_conta
                conta.aplica_transacao(transacao)

        [print(c) for c in self.contas]