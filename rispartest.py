import csv
import argparse
from contas import Conta
from transacoes import Transacao
from utils import ManageOperations

parser = argparse.ArgumentParser()
parser.add_argument('contas_csv')
parser.add_argument('transacoes_csv')
args = parser.parse_args()


def main():

    manage_operations = ManageOperations()
    manage_operations.load_data(args.contas_csv, args.transacoes_csv)
    manage_operations.execute()
    
    #manager_instance.show_saldos()
    
    return 

if __name__ == "__main__":
    main()