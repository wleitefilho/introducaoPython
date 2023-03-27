'''
Created on 24 de mar de 2020

@author: Wilson
'''

if __name__ == '__main__':
    
        
    '''Listas'''
    
    L = [1, 2, 3, 'quatro', 5.0, 'seis', 7, 8]
    print ('Imprime a Lista L:')
    print (L)

    print ('Imprime do segundo ao quito elemento da Lista L:')
    print (L[1:4])
    
    print ('Imprime o oitavo elemento da Lista L:')
    print (L[7])
    
    '''adiciona elementos a lista'''
    L.append(9)
    L+=['dez']
    print ('Adiciona elementos a lista')
    print (L)
    
    '''remove elementos da lista'''
    del(L[0:3])
    print ('Remove elementos da lista')
    print (L)
    print ('\n')
    
    '''percorrendo a lista'''
    print ('Percorrendo a lista')    
    for e in L:
        print (e)
        
    
    
    