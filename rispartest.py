import csv
import argparse
from contas import Conta
from transacoes import Transacao
from utils import ManageOperations

parser = argparse.ArgumentParser()
parser.add_argument('contas_csv')
parser.add_argument('transacoes_csv')
args = parser.parse_args()

def read_contas_csv(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(Conta(row[0], row[1]))

def read_transacoes_csv(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(Transacao(row[0], row[1]))

def main():
    contas_csv = args.contas_csv
    transacoes_csv = args.transacoes_csv

    contas = ManageOperations.read_csv(contas_csv)
    transacoes = ManageOperations.read_csv(transacoes_csv)
    
    ManageOperations.load_contas()
    ManageOperations.load_transacoes()

    # opcoes passar os dois csvs pra dentro da classe manager
    # ou usar como interface fazendo operacoes no main

    manager_instance = ManageOperations(contas_csv, transacoes_csv)
    manager_instance.load_contas
    manager_instance.load_transacoes
    manager_instance.apply_transacoes
    
    manager_instance.show_saldos()
    
    # read_contas_csv(contas_csv)
    # read_transacoes_csv(transacoes_csv)

    return 

if __name__ == "__main__":
    main()