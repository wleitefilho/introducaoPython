'''
Created on 29 de mar de 2020

@author: Wilson
'''


def leArquivo ():
    
    arq = open ("c:\\temp\\arquivo.txt", "r")
    
    for linha in arq:
        print (linha)
        
    arq.close()
    
def criaArquivoeEscreveNele():
    
    arq = open ("c:\\temp\\arquivoNovo.txt", "w")
    conteudoAquivo = ["linha1 arquivo novo",
                      "linha2 arquivo novo",
                      "linha3 arquivo novo"]
    
    for c in conteudoAquivo:
        arq.write (c + '\n')
        
    arq.close()    
    
if __name__ == '__main__':
    
    criaArquivoeEscreveNele()
