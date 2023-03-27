'''
Created on 28 de mar de 2020

@author: Wilson
'''

print (__name__)
    
'''parametro idioma eh opcional. Se nao for informado, valor default eh usado.'''
def digaOiAoMundo (idioma=1):
    
    if (idioma==1):
        print ("Ola, mundo!")
    elif (idioma==2):
        print ("Hello, world!")

'''parametro idioma eh opcional. Se nao for informado, valor default eh usado.'''
def digaAdeusAoMundo (idioma=1):

    if (idioma==1):
        print ("Adeus, mundo!")
    elif (idioma==2):
        print ("Goodbye, world!")

'''funcao que recebe como parametro uma funcao'''
def digaAlgo (fDiga):

    fDiga()

def funcaoParametrosEmpacotados (param1, param2):
    
    print ("Parametro 1 = " + param1)
    print ("Parametro 2 = " + param2)

def funcaoNumeroParametrosIndeterminado (*paramentros):
    
    for p in paramentros:
        print (p)
                            
    print ("---")
    
if __name__ == '__main__':
    
    print ("Funcao chamada com número de parâmetros indeterminado.")
    funcaoNumeroParametrosIndeterminado ("param1", "param2")
    funcaoNumeroParametrosIndeterminado ("param1", "param2", "param3")
    
    