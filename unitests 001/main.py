def soma(x, y):
    """Função que soma X + Y"""
    assert isinstance(x, (int, float)), 'X precisa ser int ou float'
    assert isinstance(y, (int, float)), 'Y precisa ser int ou float' 
    return x +y
