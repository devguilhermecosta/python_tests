try:
    import sys
    import os
    
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../nome_da_pasta'
            )
        )
    )
except Exception as error:
    print(f'{error}')


"""
O trecho de código acima serve para dizermos ao arquivo atual de qual pasta
ele deve fazer os imports.

Vamos supor que todos os nossos arquivos de importação tenham sido transferidos
para outros pacotes.
Para não ter que reescrever os imports, podemos dizer ao sistema em qual local
buscar os arquivos.
"""
