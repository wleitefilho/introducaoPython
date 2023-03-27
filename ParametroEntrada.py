'''
Created on 4 de abr de 2020

@author: Wilson
'''

import sys

if __name__ == '__main__':
    
    '''o primeiro parametro eh o nome do programa'''
    nomePrograma = sys.argv[0]
    print ("Nome do programa: " + nomePrograma)
    parametro = sys.argv[1:]
    
    print ("Parâmetros: ")
    print (parametro)
    
    
    