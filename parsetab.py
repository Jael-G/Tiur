
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND BY COMMA DIVIDE DIV_SYMBOL DOUBLE EQUAL EQUAL_TO EXPO_SYMBOL IF INT IS LBRACKET LESS_OR_EQUAL LESS_THAN LIST LPAREN MINUS MINUS_SYMBOL MORE_OR_EQUAL MORE_THAN MULTIPLY MULT_SYMBOL NAME NOT_EQUAL OF PLUS PLUS_SYMBOL RAISE RBRACKET RECEIVE RPAREN SHOW STRING SUBSTRACT TIMES TOstatement : RECEIVE LPAREN data RPARENstatement : ADD math_Term PLUS math_Term\n               | math_Term PLUS_SYMBOL math_Termstatement : SUBSTRACT math_Term MINUS math_Term\n               | math_Term MINUS_SYMBOL math_Termstatement : MULTIPLY math_Term TIMES math_Term\n               | math_Term MULT_SYMBOL math_Termstatement : DIVIDE math_Term BY math_Term\n               | math_Term DIV_SYMBOL math_Termstatement : RAISE math_Term TO math_Term\n               | math_Term EXPO_SYMBOL math_Termmath_Term : data\n               | NAMEstatement : data EQUAL_TO data\n               | data MORE_THAN data\n               | data LESS_THAN data\n               | data MORE_OR_EQUAL data\n               | data LESS_OR_EQUAL data\n               | data NOT_EQUAL datastatement : SHOW LPAREN data RPAREN\n  |  SHOW LPAREN NAME RPARENdata : INT\n          | DOUBLE\n          | STRING\n          | list\n          | statementlist_term : data\n          | data COMMA list_termlist :  LIST OF list_term\n          | LBRACKET list_term RBRACKETstatement : NAME IS data\n               | NAME EQUAL datastatement : NAME'
    
_lr_action_items = {'RECEIVE':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'ADD':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'SUBSTRACT':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'MULTIPLY':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'DIVIDE':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'RAISE':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'SHOW':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'NAME':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[11,27,27,27,27,27,11,11,11,11,11,11,11,11,27,27,27,27,27,62,11,11,11,27,27,27,27,27,11,]),'INT':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'DOUBLE':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'STRING':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'LIST':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'LBRACKET':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'$end':([1,11,12,13,14,15,26,27,28,43,45,46,47,48,49,50,52,53,54,55,56,63,64,65,66,68,69,70,71,72,73,74,75,76,],[0,-33,-22,-23,-24,-25,-12,-13,-26,-27,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'EQUAL_TO':([1,3,11,12,13,14,15,26,27,28,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,19,-33,-22,-23,-24,-25,19,-13,-26,19,19,19,19,19,19,19,19,-3,-5,-7,-9,-11,19,-33,19,19,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'MORE_THAN':([1,3,11,12,13,14,15,26,27,28,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,20,-33,-22,-23,-24,-25,20,-13,-26,20,20,20,20,20,20,20,20,-3,-5,-7,-9,-11,20,-33,20,20,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'LESS_THAN':([1,3,11,12,13,14,15,26,27,28,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,21,-33,-22,-23,-24,-25,21,-13,-26,21,21,21,21,21,21,21,21,-3,-5,-7,-9,-11,21,-33,21,21,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'MORE_OR_EQUAL':([1,3,11,12,13,14,15,26,27,28,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,22,-33,-22,-23,-24,-25,22,-13,-26,22,22,22,22,22,22,22,22,-3,-5,-7,-9,-11,22,-33,22,22,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'LESS_OR_EQUAL':([1,3,11,12,13,14,15,26,27,28,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,23,-33,-22,-23,-24,-25,23,-13,-26,23,23,23,23,23,23,23,23,-3,-5,-7,-9,-11,23,-33,23,23,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'NOT_EQUAL':([1,3,11,12,13,14,15,26,27,28,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,24,-33,-22,-23,-24,-25,24,-13,-26,24,24,24,24,24,24,24,24,-3,-5,-7,-9,-11,24,-33,24,24,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'PLUS_SYMBOL':([1,3,5,11,12,13,14,15,25,26,27,28,34,35,36,37,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,-12,29,-13,-22,-23,-24,-25,29,-12,-13,-26,29,29,29,29,-12,-12,-12,-12,-12,-12,-12,-12,29,29,29,29,29,-12,-13,-12,-12,-29,-30,-1,29,29,29,29,29,-20,-21,-28,]),'MINUS_SYMBOL':([1,3,5,11,12,13,14,15,25,26,27,28,34,35,36,37,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,-12,30,-13,-22,-23,-24,-25,30,-12,-13,-26,30,30,30,30,-12,-12,-12,-12,-12,-12,-12,-12,30,30,30,30,30,-12,-13,-12,-12,-29,-30,-1,30,30,30,30,30,-20,-21,-28,]),'MULT_SYMBOL':([1,3,5,11,12,13,14,15,25,26,27,28,34,35,36,37,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,-12,31,-13,-22,-23,-24,-25,31,-12,-13,-26,31,31,31,31,-12,-12,-12,-12,-12,-12,-12,-12,31,31,31,31,31,-12,-13,-12,-12,-29,-30,-1,31,31,31,31,31,-20,-21,-28,]),'DIV_SYMBOL':([1,3,5,11,12,13,14,15,25,26,27,28,34,35,36,37,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,-12,32,-13,-22,-23,-24,-25,32,-12,-13,-26,32,32,32,32,-12,-12,-12,-12,-12,-12,-12,-12,32,32,32,32,32,-12,-13,-12,-12,-29,-30,-1,32,32,32,32,32,-20,-21,-28,]),'EXPO_SYMBOL':([1,3,5,11,12,13,14,15,25,26,27,28,34,35,36,37,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-26,-12,33,-13,-22,-23,-24,-25,33,-12,-13,-26,33,33,33,33,-12,-12,-12,-12,-12,-12,-12,-12,33,33,33,33,33,-12,-13,-12,-12,-29,-30,-1,33,33,33,33,33,-20,-21,-28,]),'LPAREN':([2,10,],[18,38,]),'IS':([11,27,62,],[39,39,39,]),'EQUAL':([11,27,62,],[40,40,40,]),'COMMA':([11,12,13,14,15,26,27,28,43,45,46,47,48,49,50,52,53,54,55,56,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-33,-22,-23,-24,-25,-12,-13,-26,67,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'RBRACKET':([11,12,13,14,15,26,27,28,42,43,45,46,47,48,49,50,52,53,54,55,56,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-33,-22,-23,-24,-25,-12,-13,-26,66,-27,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'RPAREN':([11,12,13,14,15,26,27,28,43,44,45,46,47,48,49,50,52,53,54,55,56,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-33,-22,-23,-24,-25,-12,-13,-26,-27,68,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,74,75,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'PLUS':([11,12,13,14,15,25,26,27,28,43,45,46,47,48,49,50,52,53,54,55,56,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-33,-22,-23,-24,-25,51,-12,-13,-26,-27,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'MINUS':([11,12,13,14,15,26,27,28,34,43,45,46,47,48,49,50,52,53,54,55,56,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-33,-22,-23,-24,-25,-12,-13,-26,57,-27,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'TIMES':([11,12,13,14,15,26,27,28,35,43,45,46,47,48,49,50,52,53,54,55,56,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-33,-22,-23,-24,-25,-12,-13,-26,58,-27,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'BY':([11,12,13,14,15,26,27,28,36,43,45,46,47,48,49,50,52,53,54,55,56,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-33,-22,-23,-24,-25,-12,-13,-26,59,-27,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'TO':([11,12,13,14,15,26,27,28,37,43,45,46,47,48,49,50,52,53,54,55,56,63,64,65,66,68,69,70,71,72,73,74,75,76,],[-33,-22,-23,-24,-25,-12,-13,-26,60,-27,-14,-15,-16,-17,-18,-19,-3,-5,-7,-9,-11,-31,-32,-29,-30,-1,-2,-4,-6,-8,-10,-20,-21,-28,]),'OF':([16,],[41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[1,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'data':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[3,26,26,26,26,26,43,44,45,46,47,48,49,50,26,26,26,26,26,61,63,64,43,26,26,26,26,26,43,]),'math_Term':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[5,25,34,35,36,37,5,5,5,5,5,5,5,5,52,53,54,55,56,5,5,5,5,69,70,71,72,73,5,]),'list':([0,4,6,7,8,9,17,18,19,20,21,22,23,24,29,30,31,32,33,38,39,40,41,51,57,58,59,60,67,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'list_term':([17,41,67,],[42,65,76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> RECEIVE LPAREN data RPAREN','statement',4,'p_receive','tiur.py',74),
  ('statement -> ADD math_Term PLUS math_Term','statement',4,'p_addition','tiur.py',81),
  ('statement -> math_Term PLUS_SYMBOL math_Term','statement',3,'p_addition','tiur.py',82),
  ('statement -> SUBSTRACT math_Term MINUS math_Term','statement',4,'p_substraction','tiur.py',94),
  ('statement -> math_Term MINUS_SYMBOL math_Term','statement',3,'p_substraction','tiur.py',95),
  ('statement -> MULTIPLY math_Term TIMES math_Term','statement',4,'p_multiplcation','tiur.py',107),
  ('statement -> math_Term MULT_SYMBOL math_Term','statement',3,'p_multiplcation','tiur.py',108),
  ('statement -> DIVIDE math_Term BY math_Term','statement',4,'p_division','tiur.py',120),
  ('statement -> math_Term DIV_SYMBOL math_Term','statement',3,'p_division','tiur.py',121),
  ('statement -> RAISE math_Term TO math_Term','statement',4,'p_exponent','tiur.py',133),
  ('statement -> math_Term EXPO_SYMBOL math_Term','statement',3,'p_exponent','tiur.py',134),
  ('math_Term -> data','math_Term',1,'p_math_Term','tiur.py',146),
  ('math_Term -> NAME','math_Term',1,'p_math_Term','tiur.py',147),
  ('statement -> data EQUAL_TO data','statement',3,'p_if_expression','tiur.py',155),
  ('statement -> data MORE_THAN data','statement',3,'p_if_expression','tiur.py',156),
  ('statement -> data LESS_THAN data','statement',3,'p_if_expression','tiur.py',157),
  ('statement -> data MORE_OR_EQUAL data','statement',3,'p_if_expression','tiur.py',158),
  ('statement -> data LESS_OR_EQUAL data','statement',3,'p_if_expression','tiur.py',159),
  ('statement -> data NOT_EQUAL data','statement',3,'p_if_expression','tiur.py',160),
  ('statement -> SHOW LPAREN data RPAREN','statement',4,'p_show','tiur.py',177),
  ('statement -> SHOW LPAREN NAME RPAREN','statement',4,'p_show','tiur.py',178),
  ('data -> INT','data',1,'p_data','tiur.py',190),
  ('data -> DOUBLE','data',1,'p_data','tiur.py',191),
  ('data -> STRING','data',1,'p_data','tiur.py',192),
  ('data -> list','data',1,'p_data','tiur.py',193),
  ('data -> statement','data',1,'p_data','tiur.py',194),
  ('list_term -> data','list_term',1,'p_list_term','tiur.py',201),
  ('list_term -> data COMMA list_term','list_term',3,'p_list_term','tiur.py',202),
  ('list -> LIST OF list_term','list',3,'p_list','tiur.py',208),
  ('list -> LBRACKET list_term RBRACKET','list',3,'p_list','tiur.py',209),
  ('statement -> NAME IS data','statement',3,'p_is','tiur.py',219),
  ('statement -> NAME EQUAL data','statement',3,'p_is','tiur.py',220),
  ('statement -> NAME','statement',1,'p_variable','tiur.py',227),
]
