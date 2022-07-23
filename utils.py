from queue import Empty
from typing import Union

def somar(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    '''Função que faz a soma entre um número X e Y
    
    :param X: número inteiro ou de ponto flutuante
    :type X: int or float
    
    :param Y: número inteiro ou de ponto flutuante
    :type Y: int or float
    
    :return: soma entre X e Y
    :rtype: int or float
    '''
    assert isinstance(x, (int, float)), 'informe um int ou float'
    assert x != 0 and x > 10, 'X precisa ser diferente de Zero e maior que 10'
    assert isinstance(y, (int, float)), 'informe um int ou float'
    return x + y
