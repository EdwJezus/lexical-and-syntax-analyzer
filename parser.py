import ply.yacc as yacc
from main import tokens

def p_programa(p):
    '''
    programa : elemento
             | programa elemento
    '''

def p_elemento(p):
    '''
    elemento : funcao_completa
             | bloco
             | comando
    '''

def p_funcao_completa(p):
    '''
    funcao_completa : declara_funcao bloco
    '''

def p_bloco(p):
    '''
    bloco : INICIO PONTO comandos FIM PONTO
    '''

def p_comandos(p):
    '''
    comandos : comando
             | comandos comando
    '''

def p_comando(p):
    '''
    comando : declaracao
            | atribuicao
            | se
            | enquanto
            | para
            | neg
    '''

############################################ COMANDOS

def p_declaracao(p):
    '''
    declaracao : NUMERO IDENTIFICADOR PONTO
               | RES_INTEIRO IDENTIFICADOR PONTO
               | declara_funcao
    '''
    print("Declaração válida")

def p_atribuicao(p):
    '''
    atribuicao : IDENTIFICADOR ATRIBUICAO expressao PONTO
               | ELGIO ATRIBUICAO expressao PONTO
    '''
    print("Atribuição válida")

def p_se(p):
    '''
    se : SE expressao_logica PONTO ENTAO PONTO bloco SENAO PONTO bloco
       | SE expressao_logica PONTO ENTAO PONTO bloco 
    '''
    print("Comando Se válido")

def p_enquanto(p):
    '''
    enquanto : ENQUANTO expressao_logica PONTO bloco
    '''
    print("Comando Enquanto válido")

def p_para(p):
    '''
    para : PARA IDENTIFICADOR INTEIRO PONTO bloco
         | PARA IDENTIFICADOR IDENTIFICADOR PONTO bloco
    '''
    print("Comando Para válido")

def p_neg(p):
    '''
    neg : NEG IDENTIFICADOR PONTO
    '''
    print("Comando NEG válido")

############################################ FUNÇÃO

def p_chama_funcao(p):
    '''
    chama_funcao : FUNCAO ABRE_PARENTESES parametros FECHA_PARENTESES
    '''

def p_declara_funcao(p):
    '''
    declara_funcao : NUMERO FUNCAO ABRE_PARENTESES declara_parametros FECHA_PARENTESES PONTO
                   | RES_INTEIRO FUNCAO ABRE_PARENTESES declara_parametros FECHA_PARENTESES PONTO
    '''

def p_declara_parametros(p):
    '''
    declara_parametros : NUMERO IDENTIFICADOR
                       | NUMERO IDENTIFICADOR VIRGULA declara_parametros
                       | RES_INTEIRO IDENTIFICADOR
                       | RES_INTEIRO IDENTIFICADOR VIRGULA declara_parametros
    '''

def p_parametros(p):
    '''
    parametros : expressao
               | expressao VIRGULA parametros
    '''

############################################ EXPRESSÕES

def p_expressao_variaveis(p):
    '''
    expressao : INTEIRO
              | IDENTIFICADOR
              | NADA
              | chama_funcao
    '''

def p_expressao_operador(p):
    '''
    operador  : MAIS
              | EXP
              | MENOS
              | DIVISAO
              | MULTIPLICACAO
              | MODULO
    '''

def p_expressao_operador_expressao(p):
    '''
    expressao : expressao operador expressao
    '''

def p_expressao_logica(p):
    '''
    expressao_logica : expressao IGUAL expressao
                     | expressao MAIOR expressao
                     | expressao MENOR expressao
                     | expressao DIFERENTE expressao
                     | expressao MAIOR_IGUAL expressao
                     | expressao MENOR_IGUAL expressao
    '''

############################################

erro_sintatico = False

def p_error(p):
    global erro_sintatico
    erro_sintatico = True

    if p:
        print(
            f"[ERRO SINTATICO] "
            f"Linha {p.lineno} "
            f"Token {p.type} "
            f"Valor '{p.value}'"
        )
    else:
        print("[ERRO SINTATICO] Final inesperado do arquivo")

parser = yacc.yacc()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python parser.py arquivo.txt")
        exit()

    nome_arquivo = sys.argv[1]

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        codigo = arquivo.read()

    print(f"\nAnalisando arquivo: {nome_arquivo}\n")

    parser.parse(codigo)

    if not erro_sintatico:
        print("\nPrograma sintaticamente válido!")
    else:
        print("\nPrograma contém erros sintáticos.")
