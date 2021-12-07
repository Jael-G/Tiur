
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND BY COMMA DIVIDE DIV_SYMBOL DOUBLE EXPO_SYMBOL INT IS LBRACKET LIST LPAREN MINUS MINUS_SYMBOL MULTIPLY MULT_SYMBOL NAME PLUS PLUS_SYMBOL RAISE RBRACKET RECEIVE RPAREN SHOW STRING SUBSTRACT TIMES TOstatement : RECEIVE LPAREN data RPARENstatement : ADD data PLUS math_Term\n               | data PLUS_SYMBOL math_Termstatement : SUBSTRACT data MINUS math_Term\n               | data MINUS_SYMBOL math_Termstatement : MULTIPLY data TIMES math_Term\n               | data MULT_SYMBOL math_Termstatement : DIVIDE data BY math_Term\n               | data DIV_SYMBOL math_Termstatement : RAISE data TO math_Term\n               | data EXPO_SYMBOL math_Termmath_Term : datastatement : SHOW LPAREN data RPAREN\n  |  SHOW LPAREN NAME RPARENdata : INT\n          | DOUBLE\n          | STRING\n          | list\n          | statementlist_term : data\n          | data COMMA list_termlist : LBRACKET list_term RBRACKETstatement : NAME IS datastatement : NAME'
    
_lr_action_items = {'RECEIVE':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'ADD':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'SUBSTRACT':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'MULTIPLY':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'DIVIDE':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'RAISE':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'SHOW':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'NAME':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[10,10,10,10,10,10,10,10,10,10,10,10,10,45,10,10,10,10,10,10,10,]),'INT':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'DOUBLE':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'STRING':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'LBRACKET':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'$end':([1,10,11,12,13,14,23,33,34,35,36,37,38,46,47,49,50,51,52,53,54,55,56,],[0,-24,-15,-16,-17,-18,-19,-12,-3,-5,-7,-9,-11,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'PLUS_SYMBOL':([1,3,10,11,12,13,14,22,23,24,25,26,27,31,32,33,34,35,36,37,38,44,45,46,47,49,50,51,52,53,54,55,56,],[-19,17,-24,-15,-16,-17,-18,17,-19,17,17,17,17,17,17,17,-3,-5,-7,-9,-11,17,-24,17,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'MINUS_SYMBOL':([1,3,10,11,12,13,14,22,23,24,25,26,27,31,32,33,34,35,36,37,38,44,45,46,47,49,50,51,52,53,54,55,56,],[-19,18,-24,-15,-16,-17,-18,18,-19,18,18,18,18,18,18,18,-3,-5,-7,-9,-11,18,-24,18,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'MULT_SYMBOL':([1,3,10,11,12,13,14,22,23,24,25,26,27,31,32,33,34,35,36,37,38,44,45,46,47,49,50,51,52,53,54,55,56,],[-19,19,-24,-15,-16,-17,-18,19,-19,19,19,19,19,19,19,19,-3,-5,-7,-9,-11,19,-24,19,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'DIV_SYMBOL':([1,3,10,11,12,13,14,22,23,24,25,26,27,31,32,33,34,35,36,37,38,44,45,46,47,49,50,51,52,53,54,55,56,],[-19,20,-24,-15,-16,-17,-18,20,-19,20,20,20,20,20,20,20,-3,-5,-7,-9,-11,20,-24,20,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'EXPO_SYMBOL':([1,3,10,11,12,13,14,22,23,24,25,26,27,31,32,33,34,35,36,37,38,44,45,46,47,49,50,51,52,53,54,55,56,],[-19,21,-24,-15,-16,-17,-18,21,-19,21,21,21,21,21,21,21,-3,-5,-7,-9,-11,21,-24,21,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'LPAREN':([2,9,],[16,28,]),'IS':([10,45,],[29,29,]),'PLUS':([10,11,12,13,14,22,23,33,34,35,36,37,38,46,47,49,50,51,52,53,54,55,56,],[-24,-15,-16,-17,-18,39,-19,-12,-3,-5,-7,-9,-11,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'MINUS':([10,11,12,13,14,23,24,33,34,35,36,37,38,46,47,49,50,51,52,53,54,55,56,],[-24,-15,-16,-17,-18,-19,40,-12,-3,-5,-7,-9,-11,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'TIMES':([10,11,12,13,14,23,25,33,34,35,36,37,38,46,47,49,50,51,52,53,54,55,56,],[-24,-15,-16,-17,-18,-19,41,-12,-3,-5,-7,-9,-11,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'BY':([10,11,12,13,14,23,26,33,34,35,36,37,38,46,47,49,50,51,52,53,54,55,56,],[-24,-15,-16,-17,-18,-19,42,-12,-3,-5,-7,-9,-11,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'TO':([10,11,12,13,14,23,27,33,34,35,36,37,38,46,47,49,50,51,52,53,54,55,56,],[-24,-15,-16,-17,-18,-19,43,-12,-3,-5,-7,-9,-11,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'COMMA':([10,11,12,13,14,23,31,33,34,35,36,37,38,46,47,49,50,51,52,53,54,55,56,],[-24,-15,-16,-17,-18,-19,48,-12,-3,-5,-7,-9,-11,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),'RBRACKET':([10,11,12,13,14,23,30,31,33,34,35,36,37,38,46,47,49,50,51,52,53,54,55,56,57,],[-24,-15,-16,-17,-18,-19,47,-20,-12,-3,-5,-7,-9,-11,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,-21,]),'RPAREN':([10,11,12,13,14,23,32,33,34,35,36,37,38,44,45,46,47,49,50,51,52,53,54,55,56,],[-24,-15,-16,-17,-18,-19,49,-12,-3,-5,-7,-9,-11,55,56,-23,-22,-1,-2,-4,-6,-8,-10,-13,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[1,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'data':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[3,22,24,25,26,27,31,32,33,33,33,33,33,44,46,33,33,33,33,33,31,]),'list':([0,4,5,6,7,8,15,16,17,18,19,20,21,28,29,39,40,41,42,43,48,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'list_term':([15,48,],[30,57,]),'math_Term':([17,18,19,20,21,39,40,41,42,43,],[34,35,36,37,38,50,51,52,53,54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> RECEIVE LPAREN data RPAREN','statement',4,'p_receive','tiur.py',66),
  ('statement -> ADD data PLUS math_Term','statement',4,'p_addition','tiur.py',72),
  ('statement -> data PLUS_SYMBOL math_Term','statement',3,'p_addition','tiur.py',73),
  ('statement -> SUBSTRACT data MINUS math_Term','statement',4,'p_substraction','tiur.py',85),
  ('statement -> data MINUS_SYMBOL math_Term','statement',3,'p_substraction','tiur.py',86),
  ('statement -> MULTIPLY data TIMES math_Term','statement',4,'p_multiplcation','tiur.py',98),
  ('statement -> data MULT_SYMBOL math_Term','statement',3,'p_multiplcation','tiur.py',99),
  ('statement -> DIVIDE data BY math_Term','statement',4,'p_division','tiur.py',111),
  ('statement -> data DIV_SYMBOL math_Term','statement',3,'p_division','tiur.py',112),
  ('statement -> RAISE data TO math_Term','statement',4,'p_exponent','tiur.py',124),
  ('statement -> data EXPO_SYMBOL math_Term','statement',3,'p_exponent','tiur.py',125),
  ('math_Term -> data','math_Term',1,'p_math_Term','tiur.py',137),
  ('statement -> SHOW LPAREN data RPAREN','statement',4,'p_show','tiur.py',145),
  ('statement -> SHOW LPAREN NAME RPAREN','statement',4,'p_show','tiur.py',146),
  ('data -> INT','data',1,'p_data','tiur.py',153),
  ('data -> DOUBLE','data',1,'p_data','tiur.py',154),
  ('data -> STRING','data',1,'p_data','tiur.py',155),
  ('data -> list','data',1,'p_data','tiur.py',156),
  ('data -> statement','data',1,'p_data','tiur.py',157),
  ('list_term -> data','list_term',1,'p_list_term','tiur.py',164),
  ('list_term -> data COMMA list_term','list_term',3,'p_list_term','tiur.py',165),
  ('list -> LBRACKET list_term RBRACKET','list',3,'p_list','tiur.py',171),
  ('statement -> NAME IS data','statement',3,'p_is','tiur.py',181),
  ('statement -> NAME','statement',1,'p_variable','tiur.py',188),
]
