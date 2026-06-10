import ply.lex as lex
import re

reservadas = {
	'elgio': 	'ELGIO',
	'enquanto': 'ENQUANTO',
	'se': 		'SE',
	'entao': 	'ENTAO',
	'senao': 	'SENAO',
	'para': 	'PARA',
	'numero': 	'NUMERO',
	'NADA': 	'NADA',
	'NEG': 		'NEG',
	'EXP': 		'EXP',
	'inicio': 	'INICIO',
	'fim': 		'FIM',
	'igual': 	'IGUAL',
	'menor': 	'MENOR',
	'maior': 	'MAIOR',
	'diferente': 'DIFERENTE',
	'Migual': 	'MAIOR_IGUAL',
	'migual': 	'MENOR_IGUAL',
	'inteiro':	'RES_INTEIRO'
 }

tokens = ('IDENTIFICADOR','INTEIRO', 'FUNCAO', 'MAIS', 'MENOS', 'DIVISAO', 'MULTIPLICACAO', 'ATRIBUICAO', 'MODULO', 'PONTO', 'VIRGULA', 'ABRE_PARENTESES', 'FECHA_PARENTESES') + tuple(reservadas.values())

t_ignore = ' \t'

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMENTARIO(t):
	r'\*[^\n]*'
	pass

def t_PALAVRA(t):
	r'[a-zA-Z]{2,}'

	if t.value in reservadas:
		t.type = reservadas[t.value]

	elif re.fullmatch(r'[A-Z][A-Za-z]{2,}[a-z]', t.value):
		t.type = 'IDENTIFICADOR'

	else:
		print(f"Identificador invalido: {t.value}")
		return

	return t

def t_INTEIRO(t):
	r'[1-9][0-9]*'
	t.value = int(t.value)
	return t

def t_FUNCAO(t):
	r'[_][A-Z][A-Za-z]{2,}[a-z]'
	return t

t_MAIS = r'\+'
t_MENOS = r'\-'
t_DIVISAO = r'\/'
t_MULTIPLICACAO = r'x'
t_ATRIBUICAO = r'='
t_MODULO = r'\%'
t_PONTO = r'\.'
t_VIRGULA = r'\,'
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'

def t_error(t):
	print(f"Caracter Invalido: {t.value[0]}")
	t.lexer.skip(1)

lexer = lex.lex()

###################################### TESTE

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python main.py arquivo.txt")
        exit()

    nome_arquivo = sys.argv[1]

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        codigo = arquivo.read()

    lexer.input(codigo)

    print(f"\nAnalisando arquivo: {nome_arquivo}\n")

    for token in lexer:
        print(
            f"Tipo: {token.type:17} "
            f"Valor: {str(token.value):15} "
            f"Linha: {token.lineno}"
        )
