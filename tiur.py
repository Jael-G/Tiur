import ply.lex as lex
import ply.yacc as yacc
from ply.lex import LexToken
TEMP_LIST = []
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
  '''statement : RECEIVE LPAREN DATA RPAREN'''
  value = input(f"{(p.slice[3].value)}")
  p[0] = value
  return p

def p_show(p):
  '''statement : SHOW LPAREN DATA RPAREN
  |  SHOW LPAREN NAME RPAREN'''
  if p.slice[3].type == 'NAME':
    print(Variables[p.slice[3].value])
  else:
    print(p.slice[3].value)

def p_data(p):
  '''DATA : INT
          | STRING
          | list
          | statement'''
  p[0] = p[1]
  return p

def p_term(p):
  '''term : DATA
          | DATA COMMA term'''
  global TEMP_LIST
  TEMP_LIST.append(p.slice[1].value)
  return p

def p_list(p):
  '''list : LBRACKET term RBRACKET'''
  global TEMP_LIST
  COPY = TEMP_LIST.copy()
  COPY.reverse()
  TEMP_LIST = []
  p[0] = COPY
  return COPY


def p_is(p):
  '''statement : NAME IS DATA'''

  Variables[p[1]] = p.slice[3].value
  # print(Variables)


def p_variable(p):
  'statement : NAME'
  
  return Variables[p.slice[1].value]


def p_error(p):
  print("Syntax error at %s"%p)

lexer = lex.lex()
yacc.yacc()

with open('./examples/code.tiur','r') as file:
  code = file.read().splitlines()

for line in code:
  try:
    s = line
    if s == '' or  s[0]=='#':
      continue  
  except EOFError:
    break
  yacc.parse(s)