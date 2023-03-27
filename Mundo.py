'''
Created on 29 de mar de 2020

@author: Wilson
'''

class Mundo (object):
    
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        '''1 - portugues
           2 - ingles    '''
        self.idioma = 1
        
    def digaOla(self):

        if (self.idioma==1):        
            print ("Ola, mundo!")
        elif (self.idioma==2):
            print ("Hello, world!")

class Continente (Mundo):
    
    def digaOla (self):
        
        if (self.idioma==1):        
            print ("Ola, America!")
        elif (self.idioma==2):
            print ("Hello, America!")
