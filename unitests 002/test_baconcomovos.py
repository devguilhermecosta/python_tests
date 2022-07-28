import unittest
from baconcomovos import bacon_com_ovos

"""
PRIMEIRO CRIAR O TESTE E VER FALHAR;
CRIAR O CÓDIGO E VER O TESTE PASSAR;
MELHORAR O CÓDIGO.
"""

class TestBaconComOvos(unittest.TestCase):
    
    def test_deve_receber_um_numero_inteiro_senao_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('str')


if __name__ == '__main__':
    unittest.main(verbosity=2)
