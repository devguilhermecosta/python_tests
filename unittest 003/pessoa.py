import requests


class Pessoa:
    """Classe que cria um objeto do tipo Pessoa"""
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        dados = requests.get('https://www.google.com.br')
        
        if dados.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'
