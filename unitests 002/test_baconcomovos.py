import unittest
from baconcomovos import bacon_com_ovos

"""
PRIMEIRO CRIAR O TESTE E VER FALHAR;
CRIAR O CÓDIGO E VER O TESTE PASSAR;
MELHORAR O CÓDIGO.
"""

class TestBaconComOvos(unittest.TestCase):
    
    def test_bacon_com_ovos_deve_receber_um_numero_inteiro_senao_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('str')

    def test_bacon_com_ovos_deve_retorna_bacon_com_ovos_se_numero_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com Ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    saida,
                    msg = f'"{entrada}" não retornou "{saida}"'
                    )

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_numero_nao_for_multiplo_de_3_e_5(self):
        entradas = (2, 4, 7, 8, 11)
        saida = 'Passar Fome'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    saida,
                    msg = f'"{entrada}" não retornou "{saida}"'
                    )

    def test_bacon_com_ovos_deve_retornar_bacon_se_numero_for_multiplo_somente_de_3(self):
        entradas = (3, 6, 9, 12)
        saida = 'Bacon'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    saida, 
                    msg = f'"{entrada}" não retornou "{saida}"'
                    )


    def test_bacon_com_ovos_deve_retornar_ovos_se_numero_for_multiplo_somente_de_5(self):
        entradas = (5, 10, 20, 25)
        saida = 'Ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg = f'"{entrada}" não retornou "{saida}"'
                )

if __name__ == '__main__':
    unittest.main(verbosity=2)
