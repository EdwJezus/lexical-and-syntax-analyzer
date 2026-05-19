import ply.lex as lex
import ply.yacc as yacc

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
 }

tokens = ('INTEIRO', 'IDENTIFICADOR', 'FUNCAO', 'MAIS', 'MENOS', 'DIVISAO', 'MULTIPLICACAO', 'ATRIBUICAO', 'MODULO', 'PONTO', 'VIRGULA', 'ABRE_PARENTESES', 'FECHA_PARENTESES') + tuple(reservadas.values())

t_ignore = ' \t'

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMENTARIO(t):
	r'\*[^\n]*'
	pass

def t_PALAVRA(t):
	r'[a-zA-Z]+'

	if t.value in reservadas:
		t.type = reservadas[t.value]
		return t

	elif re.fullmatch(r'[a-zA-Z]+')	

def t_RESERVADA(t):
	r'[a-zA-Z]+'
	if t.value in reservadas:
		t.type = reservadas[t.value]
		return t

def t_IDENTIFICADOR(t):
	r'[A-Z][A-Za-z]{2,}[a-z]'
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
	print(f"Palavra Invalida: {t.value[0]}")
	t.lexer.skip(1)

lexer = lex.lex()

#########################################################

with open("projeto2/exemplo.txt", "r", encoding="utf-8") as arquivo:
	teste = arquivo.read()

lexer.input(teste)

for token in lexer:
	print(token)