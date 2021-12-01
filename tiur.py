import ply.lex as lex
import ply.yacc as yacc
from ply.lex import LexToken

reserved = {
  'is' : "IS",
  'show' : "SHOW",
  'receive': "RECEIVE",
  'list':'LIST',
}

tokens = ['LPAREN','RPAREN','LBRACKET', 'RBRACKET', 'COMMA', 'STRING', 'NAME', 'INT'] + list(reserved.values())

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'NAME')    # Check for reserved words
  return t


t_LPAREN =r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_STRING = r'\".*?\"'
t_ignore = " \t"

def t_INT(t):
     r'\d+'
     t.value = int(t.value)    
     return t


def t_error(t):
  print("Syntax error at %s"%t.value)


Variables = {}


def p_receive(p):
  '''statement : NAME IS RECEIVE LPAREN STRING RPAREN'''
  value = input(f"{(p.slice[5].value[1:-1])}")
  Variables[p.slice[1].value]=value

def p_show(p):
  '''statement : SHOW LPAREN DATA RPAREN'''
  
  print(p.slice[3].value)

def p_data(p):
  '''DATA : INT
          | STRING'''
  p[0] = p[1]
  return p


def p_list(p):
  '''statement : LBRACKET term RBRACKET
  
  term : DATA
       | DATA COMMA term
  
  '''
  print(p.slice)


def p_is(p):
  '''statement : NAME IS DATA'''
  Variables[p[1]] = p[3]


def p_variable(p):
  'statement : NAME'
  return Variables[p.slice[1].value]


def p_error(p):
  print("Syntax error at %s"%p)

lexer = lex.lex()
yacc.yacc()

with open('./examples/CODE.txt','r') as file:
  code = file.read().splitlines()

for line in code:
  try:
    s = line   
  except EOFError:
    break
  yacc.parse(s)