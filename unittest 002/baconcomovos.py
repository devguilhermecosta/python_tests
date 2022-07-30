"""
TDD - TEST DRIVEN DEVELOPMENT - DESENVOLVIMENTO DIRIGIDO A TESTES
    DIVIDIDO EM: RED, GREEN E REFACTOR
    
    RED
        PARTE 1 - CRIAR O TESTE E VER FALHAR
        
    GREEN
        PARTE 2 - CRIAR O CÓDIGO E VER O TESTE PASSAR
        
    REFACTOR
        PARTE 3 - MELHORAR O CÓDIGO


1 - RECEBER UM NÚMERO INTEIRO; OK
2 - SABER SE O NUM É MULT DE 3 E 5 OK
        RETORNAR 'BACON COM OVOS';
3 - SABER SE O NÚMERO NÃO É MULT DE 3 E 5 OK
        RETORNAR 'PASSAR FOME';
4 - SABER SE O NÚMERO É MULT SOMENTE DE 3 OK
        RETORNAR 'BACON';
5 - SABER SE O NÚMERO É MULT SOMENTE DE 5
        RETORNAR 'OVOS'.
"""

def bacon_com_ovos(n):
        assert isinstance(n, int), 'n deve ser um int'
    
        if n % 3 == 0 and n % 5 == 0:
                return 'Bacon com Ovos'

        if n % 3 != 0 and n % 5 != 0:
                return 'Passar Fome'

        if n % 3 == 0 and n % 5!= 0:
                return 'Bacon'
        
        if n % 3 != 0 and n % 5 == 0:
                return 'Ovos'
        
print(bacon_com_ovos('1'))

