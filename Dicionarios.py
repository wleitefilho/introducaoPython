'''
Created on 24 de mar de 2020

@author: Wilson
'''

if __name__ == '__main__':

    '''conjutos'''
    '''    eh uma lista de valor cujos itens nao se repetem'''
    C = {0,1,2,3,4,5,6,7,8,9,0}
    print ("Conjunto: ", C)

            
    '''dicionario, relaciona uma chave a um valor'''
    D = {1:   "joao", 
         234: "jose",
         3:   "maria",
         776: "pedro",
         333: "paulo"}
    print ("Imprime dicionário: ")
    print (D)
    print ("")
    
    '''imprime um elemento específico, acessando-o pela chave'''
    print ("Imprime um elemento específico, acessando-o pela chave: ")
    print (D[234])
    
    chaves  = D.keys()
    valores = D.values()
    print (chaves)
    print (valores)
    
    
    
    
    
    
    