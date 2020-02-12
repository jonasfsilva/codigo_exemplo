import csv
from collections import OrderedDict
from transacoes import Transacao 
from contas import Conta 


class ManageOperations:

    contas = []
    transacoes = []

    def read_csv(self, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            lines = OrderedDict() 
            for row in csv_reader:
                lines[row[0]] = row[1]
        return lines

    def load_data(self, contas_csv, transacoes_csv):
        transacoes_lines = self.read_csv(transacoes_csv)
        contas_lines = self.read_csv(contas_csv)

        for conta_id, conta_saldo  in contas_lines.items():
            self.contas.append(Conta(conta_id, conta_saldo))

        for transacao_id, transacao_valor in transacoes_lines.items():
            self.transacoes.append(Transacao(transacao_id, transacao_valor))
        
    def execute(self):
        #contas que tem saldos
        #percorrer as transacoes pegar as contas e aplicar as transacoes

        for transacao in self.transacoes:
            for conta in self.contas:
                conta.identificadot = transacao.identificadot_conta
                conta.aplica_transacao(transacao)

        [print(c) for c in self.contas]