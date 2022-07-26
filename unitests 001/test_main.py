from main import soma
import unittest

class TesteSoma(unittest.TestCase):
    """Classe responsável por testar a função soma()"""
    def test_soma_1_e_1_deve_retornar_2(self):
        self.assertEqual(soma(1, 1), 2)
        
    def test_soma_10_e_20_deve_retornar_30(self):
        self.assertEqual(soma(10, 20), 30)
        
    def test_varias_entradas(self):
        x_y_saida = (
            (10, 20, 30),
            (1, 1, 2),
            (-10, -10, -20),
            (100, 159, 259)
        )
        
        for saidas in x_y_saida:
            with self.subTest(saidas=saidas):
                x, y, resultado = saidas
                self.assertEqual(soma(x, y), resultado)
    
    def test_x_diferente_de_int_ou_float(self):
        with self.assertRaises(AssertionError):
            soma('10', 20)
            
    def test_y_diferente_de_int_ou_float(self):
        with self.assertRaises(AssertionError):
            soma(10, '20')
            
#  -> importar a biblioteca UNITTEST
 
#  -> importar a classe ou função que será testada
 
#  -> criar uma classe para testar uma função específica ou uma classe específica
#  -> a classe deve herdar de unittest.TestCase
 
#  -> cada função de teste deve ter seu nome iniciado com TEST e também explicar do que se trata o teste
#  -> cada função de teste terá um self.assert de acordo com o que está sendo testado
 
#  -> podemos ter um gerenciador de contexto para testar listas de testes ou assertRaises (with)
 
#  -> para instanciar/iniciar os testes usar -> unittest.main()
#  -> podemos usar o parâmetro verbosity=2 para ver no terminal todos os resultados, inclusive aqueles que passaram no teste

if __name__ == '__main__':
    unittest.main(verbosity=2)
