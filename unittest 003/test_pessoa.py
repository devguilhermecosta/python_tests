"""
método para criar uma instância dentro da própria classe: setUp()

from unittest.mock import patch
request.return_value.ok = True ou False

class Pessoa:
    nome:
    sobrenome: str
    dados_obtidos: bool
    
    API:
        obter_todos_os_dados -> method
            OK
            404
            
            (dados obtidos se torna True se dados obtidos com sucesso)
"""
import unittest
from unittest.mock import patch
from pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        """Cria instância de Pessoa"""
        self.p1 = Pessoa('Guilherme', 'Costa')

    def test_pessoa_attr_nome_deve_sert_str(self):
        self.assertIsInstance(self.p1.nome, str)
        
    def test_pessoa_attr_sobrenome_deve_ser_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        
    def test_pessoa_attr_dados_obtidos_inicia_com_false(self):
        self.assertEqual(self.p1.dados_obtidos, False)
        
    def test_pessoa_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')


    def test_pessoa_obter_todos_os_dados_erro_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            
    def test_pessoa_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False
            
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
