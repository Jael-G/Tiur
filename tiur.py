import ply.lex as lex
import ply.yacc as yacc
from ply.lex import LexToken
import sys
TEMP_LIST = []

reserved = {
  'is' : "IS",
  'show' : "SHOW",
  'receive': "RECEIVE",
  'list':'LIST',
  'of':'OF',
  'and': 'AND',
  'plus':'PLUS',
  'add':'ADD',
  'sub':'SUBSTRACT',
  'minus':'MINUS',
  'mult':'MULTIPLY',
  'times':'TIMES',
  'div':'DIVIDE',
  'by':'BY',
  'raise':'RAISE',
  'to':'TO',
}

tokens = ['EQUAL', 'LPAREN','RPAREN','LBRACKET', 'RBRACKET', 'COMMA', 'STRING', 'NAME', 'DOUBLE', 'INT', 'MULT_SYMBOL','DIV_SYMBOL', 'PLUS_SYMBOL','MINUS_SYMBOL','EXPO_SYMBOL'] + list(reserved.values())

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'NAME')    # Check for reserved words
  return t

t_EQUAL = r'\='
t_LPAREN =r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_STRING = r'\".*?\"'
t_ignore = " \t"
t_PLUS_SYMBOL = r'\+'
t_MINUS_SYMBOL = r'\-'
t_MULT_SYMBOL = r'\*'
t_DIV_SYMBOL = r'\/'
t_EXPO_SYMBOL = r'\*\*'

def t_DOUBLE(t):
     r'\d+\.\d+'
     t.value = float(t.value)    
     return t


def t_INT(t):
     r'\d+'
     t.value = int(t.value)    
     return t


def t_error(t):
  print("Syntax error at %s"%t.value)


Variables = {}


def p_receive(p):
  '''statement : RECEIVE LPAREN data RPAREN'''
  value = input(f"{(p.slice[3].value)}")
  p[0] = value
  return p

def p_addition(p):
  '''statement : ADD math_Term PLUS math_Term
               | math_Term PLUS_SYMBOL math_Term'''
  try:
    if p.slice[2].value =='+':
      value = p.slice[1].value + p.slice[3].value
    else:
      value = p.slice[2].value + p.slice[4].value
    p[0]=value
    return p
  except:
    raise("Invalid addition method between data types")

def p_substraction(p):
  '''statement : SUBSTRACT math_Term MINUS math_Term
               | math_Term MINUS_SYMBOL math_Term'''
  try:
    if p.slice[2].value =='-':
      value = p.slice[1].value - p.slice[3].value
    else:
      value = p.slice[2].value - p.slice[4].value
    p[0]=value
    return p
  except:
    raise("Invalid substraction method between data types")

def p_multiplcation(p):
  '''statement : MULTIPLY math_Term TIMES math_Term
               | math_Term MULT_SYMBOL math_Term'''
  try:
    if p.slice[2].value =='*':
      value = p.slice[1].value * p.slice[3].value
    else:
      value = p.slice[2].value * p.slice[4].value
    p[0]=value
    return p
  except:
    raise("Invalid multiplication method between data types")

def p_division(p):
  '''statement : DIVIDE math_Term BY math_Term
               | math_Term DIV_SYMBOL math_Term'''
  try:
    if p.slice[2].value =='/':
      value = p.slice[1].value / p.slice[3].value
    else:
      value = p.slice[2].value / p.slice[4].value
    p[0]=value
    return p
  except:
    raise("Invalid division method between data types")

def p_exponent(p):
  '''statement : RAISE math_Term TO math_Term
               | math_Term EXPO_SYMBOL math_Term'''
  try:
    if p.slice[2].value =='**':
      value = p.slice[1].value ** p.slice[3].value
    else:
      value = p.slice[2].value ** p.slice[4].value
    p[0]=value
    return p
  except:
    raise("Invalid division method between data types")

def p_math_Term(p):
  '''math_Term : data
               | NAME'''
  if p.slice[1].type=='NAME':
    p[0]=Variables[p.slice[1].value]
  else:
    p[0]=p[1]
  return p




def p_show(p):
  '''statement : SHOW LPAREN data RPAREN
  |  SHOW LPAREN NAME RPAREN'''
  if p.slice[3].type == 'NAME':
    print(Variables[p.slice[3].value])
  else:
    print(p.slice[3].value)

def p_data(p):
  '''data : INT
          | DOUBLE
          | STRING
          | list
          | statement'''
  p[0] = p[1]
  return p



def p_list_term(p):
  '''list_term : data
          | data COMMA list_term'''
  global TEMP_LIST
  TEMP_LIST.append(p.slice[1].value)
  return p

def p_list(p):
  '''list :  LIST OF list_term
          | LBRACKET list_term RBRACKET'''
  global TEMP_LIST
  COPY = TEMP_LIST.copy()
  COPY.reverse()
  TEMP_LIST = []
  p[0] = COPY
  return COPY


def p_is(p):
  '''statement : NAME IS data
               | NAME EQUAL data'''

  Variables[p[1]] = p.slice[3].value
  # print(Variables)


def p_variable(p):
  'statement : NAME'
  
  return Variables[p.slice[1].value]


def p_error(p):
  print("Syntax error at %s"%p)

lexer = lex.lex()
yacc.yacc()
if len(sys.argv)==1:
  print("Missing file path to run")
  quit()

file_path = sys.argv[1]

with open(file_path,'r') as file:
  code = file.read().splitlines()

for line in code:
  try:
    s = line
    if s == '' or  s[0]=='#':
      continue  
  except EOFError:
    break
  yacc.parse(s)