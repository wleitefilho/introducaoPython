'''
Created on 23 de mar de 2020

@author: Wilson
'''

from Funcoes import digaOiAoMundo
import Funcoes

from Mundo import Mundo

if __name__ == '__main__':
    
    print ('Ola, mundo!')
    digaOiAoMundo()    
    Funcoes.digaAdeusAoMundo()
    
    m = Mundo()
    m.digaOla()
    