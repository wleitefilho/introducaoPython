'''
Created on 4 de abr de 2020

@author: Wilson
'''

import sqlite3

def exemplo1BandoDados():

    '''conecta com o banco de dados. cria o banco de dados se ele nao existir'''
    conexao = sqlite3.connect("bancodados1.db")
    
    '''obtem um objeto cursos, usado para enviar comandos e obter dados do banco de dados'''        
    cursor = conexao.cursor()
    
    '''cria a tabela registro, com dois campos: fone e nome'''
    cursor.execute ('CREATE TABLE registro (fone text, nome text)')
    
    '''insere dois registros novos na tabela registro'''    
    cursor.execute ('INSERT INTO registro VALUES (\'9999-9889\', \'joao\')')
    cursor.execute ('INSERT INTO registro VALUES (\'3333-4222\', \'maria\')')

    '''realiza um pesquisa na tabela'''
    pesquisa = cursor.execute ('SELECT * FROM registro')
    resultadoPesquisa = pesquisa.fetchall()
    for resultado in resultadoPesquisa:
        print (resultado)

    '''encerra a conexao'''        
    conexao.commit()
    cursor.close()
    conexao.close()
    
if __name__ == '__main__':
    
    exemplo1BandoDados()
