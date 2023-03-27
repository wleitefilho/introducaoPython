'''
Created on 28 de mar de 2020

@author: Wilson
'''

if __name__ == '__main__':
    
    s = "Este é um texto armazenado em uma variável do tipo string."
    
    idx = s.find("tipo")
    print ("O texto procurado começa no índice: " + str(idx))
    idx = s.find("inteiro")
    print ("O texto procurado começa no índice: " + str(idx))
    
    
    listaFrutas = "banana;laranja;maça;pera;uva;maracuja"
    listaPrecos = "5-10-2-2-5-10"
    frutas = listaFrutas.split(';')
    precos = listaPrecos.split('-')
    
    print (frutas)
    print (precos)
   
    print ("") 
    listaProdutos = {}
    for i in range(len(frutas)):
        listaProdutos[frutas[i]] = precos[i]
    
    for fruta, preco in listaProdutos.items():
        '''formatacao de strings'''
        print ("O preço da {0} é R$ {1},00.".format (fruta, preco))
    
    
    
    
