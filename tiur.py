import ply.lex as lex
import ply.yacc as yacc
from ply.lex import LexToken
import sys
TEMP_LIST = []
INSIDE_LOOP=False

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
  'if':'IF',
  'equal_to' : 'EQUAL_TO',
  'more_than' : 'MORE_THAN',
  'less_than' : 'LESS_THAN',
  'more_or_equal' : 'MORE_OR_EQUAL',
  'less_or_equal' : 'LESS_OR_EQUAL',
  'not_equal' : 'NOT_EQUAL',
  'then':'THEN',
  'to_int' :'TO_INT'
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
t_ignore = " \t"
t_PLUS_SYMBOL = r'\+'
t_MINUS_SYMBOL = r'\-'
t_MULT_SYMBOL = r'\*'
t_DIV_SYMBOL = r'\/'
t_EXPO_SYMBOL = r'\*\*'

def t_STRING(t):
  r'\".*?\"'
  t.value = t.value[1:-1]
  return t

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

def p_to_int(p):
  '''statement : TO_INT LPAREN data RPAREN'''
  p[0] = int(p.slice[3].value)
  return p
def p_receive(p):
  '''statement : RECEIVE LPAREN data RPAREN'''
  string = p.slice[3].value.replace('"','')
  value = input(f"{string}")
  p[0] = value
  return p

def p_addition(p):
  '''statement : ADD math_term PLUS math_term
               | math_term PLUS_SYMBOL math_term'''
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
  '''statement : SUBSTRACT math_term MINUS math_term
               | math_term MINUS_SYMBOL math_term'''
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
  '''statement : MULTIPLY math_term TIMES math_term
               | math_term MULT_SYMBOL math_term'''
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
  '''statement : DIVIDE math_term BY math_term
               | math_term DIV_SYMBOL math_term'''
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
  '''statement : RAISE math_term TO math_term
               | math_term EXPO_SYMBOL math_term'''
  try:
    if p.slice[2].value =='**':
      value = p.slice[1].value ** p.slice[3].value
    else:
      value = p.slice[2].value ** p.slice[4].value
    p[0]=value
    return p
  except:
    raise("Invalid division method between data types")

def p_math_term(p):
  '''math_term : data
               | NAME'''
  if p.slice[1].type=='NAME':
    p[0]=Variables[p.slice[1].value]
  else:
    p[0]=p[1]
  return p

def p_logical_operation(p):
  '''statement : data EQUAL_TO data
               | data MORE_THAN data
               | data LESS_THAN data
               | data MORE_OR_EQUAL data
               | data LESS_OR_EQUAL data
               | data NOT_EQUAL data'''

  operator = p.slice[2].value
  value1 = p.slice[1].value
  value2 = p.slice[3].value
  if operator == 'equal_to':
    p[0] = value1 == value2
  elif operator == 'more_than':
    p[0] = value1 > value2
  elif operator == 'less_than':
    p[0] = value1 < value2
  elif operator == 'more_or_equal':
    p[0] = value1 >= value2
  elif operator == 'less_or_equal':
    p[0] = value1 <= value2
  elif operator == 'not_equal':
    p[0] = value1 != value2
  else:
    raise("Invalid logical operation")
  
  return p

def p_if_statement(p):
  '''statement : IF data EQUAL_TO data THEN 
              | IF data MORE_THAN data THEN 
              | IF data LESS_THAN data THEN 
              | IF data MORE_OR_EQUAL data THEN 
              | IF data LESS_OR_EQUAL data THEN 
              | IF data NOT_EQUAL data THEN ''' 

  global INSIDE_LOOP
  operator = p.slice[3].value
  value1 = p.slice[2].value
  value2 = p.slice[4].value
  if operator == 'equal_to':
    p[0] = value1 == value2
  elif operator == 'more_than':
    p[0] = value1 > value2
  elif operator == 'less_than':
    p[0] = value1 < value2
  elif operator == 'more_or_equal':
    p[0] = value1 >= value2
  elif operator == 'less_or_equal':
    p[0] = value1 <= value2
  elif operator == 'not_equal':
    p[0] = value1 != value2
  else:
    raise("Invalid logical operation")

  if p[0] == True:
    INSIDE_LOOP = True
    return p
  else:
    return p

def p_show(p):
  '''statement : SHOW LPAREN data RPAREN
  |  SHOW LPAREN NAME RPAREN'''
  if p.slice[3].type == 'NAME':
    value =Variables[p.slice[3].value]
  else:
    value = p.slice[3].value

  if type(value)==str:
      value = value.replace('"', '')
  
  print(value)

def p_data(p):
  '''data : INT
          | DOUBLE
          | STRING
          | list
          | statement
          | NAME'''
  if p.slice[1].type == 'NAME':
    p[0] = Variables[p.slice[1].value]
  else:
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

if file_path[-5::]!='.tiur':
  print("Invalid file format. Must be of .tiur extension")
  quit()

with open(file_path,'r') as file:
  code = file.read().splitlines()

for line in code:
  try:
    s = line
    if s == '' or  s[0]=='#':
      continue

    if s[0:4] =='    ' and not INSIDE_LOOP:
      continue
    elif s[0:4] != '    ' and INSIDE_LOOP:
      INSIDE_LOOP = False

    elif s[0:4]=='    ' and INSIDE_LOOP:
      s=s[4::]


  except EOFError:
    break

  yacc.parse(s)

