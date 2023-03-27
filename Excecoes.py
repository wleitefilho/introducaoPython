'''
Created on 4 de abr de 2020

@author: Wilson
'''

if __name__ == '__main__':
    
    entrada = input ("Digite um número: ")
    
    try:
        iEntrada = int(entrada)
        dobro = iEntrada * 2
        print ("O dobro de %s é %s." % (entrada, str(dobro)))
        
    except ValueError:
        print ("Ops, valor digitado não é válido!")
        
    