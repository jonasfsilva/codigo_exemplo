import unittest


class TestConta(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_posso_adicionar_saldo(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_posso_remover_saldo(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_posso_aplicar_multa(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_nao_posso_aplicar_multa_em_transacoes_de_deposito(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestTransacao(unittest.TestCase):
    
    def test_posso_verificar_se_transacao_e_deposito(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_posso_recuperar_valor_absoluto_da_transacao(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


class TestGerenciaTrasacoes(unittest.TestCase):
    
    def test_posso_listar_corretamente_os_saldos(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_posso_ler_o_arquivo_e_carregar_dados(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_posso_executar_as_transacoes(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()