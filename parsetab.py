
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'axiomaleftDISJUNCTIONleftCONJUNCTIONnonassocEQnonassocLTGTLEGEleftPLUSMINUSleftTIMESDIVrightUPLUSUMINUSrightNEGBIN BOOLEAN BRACKETCLOSE BRACKETOPEN CHAR CHARACTER COLON COMA CONJUNCTION DISJUNCTION DIV DOT ELSE ENTERO EQ EQUAL FL FLOAT FUNCTION GE GT HEX ID IF INT LE LET LLAVEA LLAVEC LT MINUS NCIENT NEG NULL OCT PARENTHESISCLOSE PARENTHESISOPEN PLUS REAL RETURN SEMICOLON STRING TIMES TR TYPE WHILEempty :axioma : programa\n                  | emptyprograma : bloque_programabloque_programa : sentencia\n                           | sentencia bloque_programasentencia : declaracion SEMICOLON\n                     | asignacion SEMICOLON\n                     | condicion\n                     | bucle \n                     | funcion\n                     | declaracion_objeto SEMICOLON\n                     | asignacion_objeto SEMICOLON\n                     | function_call SEMICOLONexpresion : binaria\n                     | unaria\n                     | PARENTHESISOPEN expresion PARENTHESISCLOSEbinaria : expresion PLUS expresion\n                   | expresion MINUS expresionbinaria : expresion TIMES expresion\n                   | expresion DIV expresionbinaria : expresion LT expresion\n                   | expresion GT expresion\n                   | expresion LE expresion\n                   | expresion GE expresionbinaria : expresion EQ expresionbinaria : expresion CONJUNCTION expresion\n                   | expresion DISJUNCTION expresionunaria : PLUS expresion %prec UPLUS\n                  | MINUS expresion %prec UMINUS\n                  | NEG expresionexpresion : IDexpresion : ENTERO\n                     | BIN\n                     | OCT\n                     | HEXexpresion : REAL\n                     | NCIENTexpresion : CHARexpresion : TR\n                     | FLexpresion : NULLexpresion : function_call\n                     | acceso_propiedad\n                     | objeto_asgacceso_propiedad : ID DOT ID acceso_propiedad_rec\n                            | ID BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_recacceso_propiedad_rec : \n                                | DOT ID acceso_propiedad_rec\n                                | BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_recdeclaracion : LET lista_id_otro\n                       | LET lista_id_otro EQUAL expresionlista_id_otro : ID\n                         | ID COMA lista_id_otrolista_id_otro : ID COLON tipo\n                         | ID COLON tipo COMA lista_id_otrolista_id : ID\n                    | ID COMA lista_idasignacion : lista_id EQUAL expresioncondicion : IF PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves otra_condicionotra_condicion : \n                          | ELSE bloque_llavesbloque_llaves : LLAVEA bloque_programa LLAVECbucle : WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llavestipo : INT\n                | FLOAT\n                | CHARACTER\n                | BOOLEANtipo : IDfuncion : FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA axioma RETURN expresion SEMICOLON LLAVEClista_arg : \n                     | lista_arg_reclista_arg_rec : ID COLON tipo\n                         | ID COLON tipo COMA lista_arg_recfunction_call : ID PARENTHESISOPEN lista_param PARENTHESISCLOSElista_param : \n                       | lista_param_reclista_param_rec : expresion COMA lista_param_rec\n                           | expresiondeclaracion_objeto : TYPE ID EQUAL objeto_decobjeto_dec : LLAVEA propiedades_dec LLAVECpropiedades_dec : \n                           | propiedad_dec\n                           | propiedad_dec COMA propiedades_decpropiedad_dec : ID COLON tipo\n                         | STRING COLON tipopropiedad_dec : ID COLON objeto_dec\n                         | STRING COLON objeto_decasignacion_objeto : LET ID COLON ID EQUAL objeto_asgobjeto_asg : LLAVEA propiedades_asg LLAVECpropiedades_asg : \n                           | propiedad_asg\n                           | propiedad_asg COMA propiedades_asgpropiedad_asg : ID COLON expresion\n                         | STRING COLON expresion'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,8,9,10,21,22,23,24,25,26,130,132,150,162,163,180,],[-1,0,-2,-3,-4,-5,-9,-10,-11,-6,-7,-8,-12,-13,-14,-61,-64,-60,-62,-63,-70,]),'LET':([0,5,8,9,10,22,23,24,25,26,130,131,132,150,162,163,174,180,],[14,14,-9,-10,-11,-7,-8,-12,-13,-14,-61,14,-64,-60,-62,-63,14,-70,]),'IF':([0,5,8,9,10,22,23,24,25,26,130,131,132,150,162,163,174,180,],[16,16,-9,-10,-11,-7,-8,-12,-13,-14,-61,16,-64,-60,-62,-63,16,-70,]),'WHILE':([0,5,8,9,10,22,23,24,25,26,130,131,132,150,162,163,174,180,],[17,17,-9,-10,-11,-7,-8,-12,-13,-14,-61,17,-64,-60,-62,-63,17,-70,]),'FUNCTION':([0,5,8,9,10,22,23,24,25,26,130,131,132,150,162,163,174,180,],[18,18,-9,-10,-11,-7,-8,-12,-13,-14,-61,18,-64,-60,-62,-63,18,-70,]),'TYPE':([0,5,8,9,10,22,23,24,25,26,130,131,132,150,162,163,174,180,],[20,20,-9,-10,-11,-7,-8,-12,-13,-14,-61,20,-64,-60,-62,-63,20,-70,]),'ID':([0,5,8,9,10,14,18,20,22,23,24,25,26,29,30,31,33,34,36,37,38,42,57,58,59,60,63,79,80,81,82,83,84,85,86,87,88,89,91,106,108,110,111,127,128,129,130,131,132,133,143,150,154,156,157,158,162,163,164,174,177,180,],[19,19,-9,-10,-11,28,32,35,-7,-8,-12,-13,-14,43,43,43,43,67,43,71,77,43,43,43,43,98,102,43,43,43,43,43,43,43,43,43,43,43,124,43,138,77,142,98,43,43,-61,19,-64,142,159,-60,142,138,142,142,-62,-63,102,19,43,-70,]),'RETURN':([2,3,4,5,8,9,10,21,22,23,24,25,26,130,132,150,162,163,174,176,180,],[-2,-3,-4,-5,-9,-10,-11,-6,-7,-8,-12,-13,-14,-61,-64,-60,-62,-63,-1,177,-70,]),'LLAVEC':([5,8,9,10,21,22,23,24,25,26,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,73,74,75,76,93,94,95,96,97,105,108,112,113,114,115,116,117,118,119,120,121,122,123,124,126,127,130,132,136,137,142,144,146,147,148,149,150,152,155,156,159,161,162,163,166,167,168,169,170,171,172,175,179,180,],[-5,-9,-10,-11,-6,-7,-8,-12,-13,-14,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-91,-65,-66,-67,-68,-29,-30,-31,126,-92,-75,-82,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-90,-91,-61,-64,155,-83,-69,-46,-48,-93,-94,-95,-60,163,-81,-82,-48,-47,-62,-63,-84,-85,-87,-86,-88,-49,-48,-50,180,-70,]),'SEMICOLON':([6,7,11,12,13,27,28,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,70,71,72,73,74,75,76,77,78,93,94,95,105,107,112,113,114,115,116,117,118,119,120,121,122,123,124,126,140,141,142,144,146,155,159,161,171,172,175,178,],[22,23,24,25,26,-51,-53,-59,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-52,-69,-55,-65,-66,-67,-68,-53,-54,-29,-30,-31,-75,-80,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-90,-89,-56,-69,-46,-48,-81,-48,-47,-49,-48,-50,179,]),'EQUAL':([15,19,27,28,35,67,68,71,72,73,74,75,76,77,78,141,142,],[29,-57,36,-53,69,-57,-58,109,-55,-65,-66,-67,-68,-53,-54,-56,-69,]),'PARENTHESISOPEN':([16,17,19,29,30,31,32,33,36,42,43,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[30,31,33,42,42,42,63,42,42,42,33,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'COMA':([19,28,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,66,67,71,72,73,74,75,76,77,93,94,95,97,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,137,142,144,146,148,149,153,155,159,161,167,168,169,170,171,172,175,],[34,38,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,106,34,-69,110,-65,-66,-67,-68,38,-29,-30,-31,127,-75,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-90,156,-69,-46,-48,-94,-95,164,-81,-48,-47,-85,-87,-86,-88,-49,-48,-50,]),'COLON':([28,77,98,99,102,134,138,139,],[37,111,128,129,133,154,157,158,]),'ENTERO':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'BIN':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'OCT':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'HEX':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'REAL':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'NCIENT':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'CHAR':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'TR':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'FL':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'NULL':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'PLUS':([29,30,31,33,36,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,66,70,79,80,81,82,83,84,85,86,87,88,89,90,93,94,95,105,106,112,113,114,115,116,117,118,119,120,121,122,123,124,126,128,129,144,146,148,149,159,161,171,172,175,177,178,],[57,57,57,57,57,79,-15,-16,57,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,57,57,57,79,79,79,79,57,57,57,57,57,57,57,57,57,57,57,79,-29,-30,-31,-75,57,-18,-19,-20,-21,79,79,79,79,79,79,79,-17,-48,-90,57,57,-46,-48,79,79,-48,-47,-49,-48,-50,57,79,]),'MINUS':([29,30,31,33,36,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,66,70,79,80,81,82,83,84,85,86,87,88,89,90,93,94,95,105,106,112,113,114,115,116,117,118,119,120,121,122,123,124,126,128,129,144,146,148,149,159,161,171,172,175,177,178,],[58,58,58,58,58,80,-15,-16,58,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,58,58,58,80,80,80,80,58,58,58,58,58,58,58,58,58,58,58,80,-29,-30,-31,-75,58,-18,-19,-20,-21,80,80,80,80,80,80,80,-17,-48,-90,58,58,-46,-48,80,80,-48,-47,-49,-48,-50,58,80,]),'NEG':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'LLAVEA':([29,30,31,33,36,42,57,58,59,69,73,74,75,76,79,80,81,82,83,84,85,86,87,88,89,100,101,106,109,128,129,142,151,157,158,165,177,],[60,60,60,60,60,60,60,60,60,108,-65,-66,-67,-68,60,60,60,60,60,60,60,60,60,60,60,131,131,60,60,60,60,-69,131,108,108,174,60,]),'PARENTHESISCLOSE':([33,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,73,74,75,76,90,93,94,95,103,104,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,135,142,144,146,153,159,161,171,172,173,175,],[-76,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,100,101,-71,105,-77,-79,-65,-66,-67,-68,123,-29,-30,-31,134,-72,-75,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-90,-78,-69,-46,-48,-73,-48,-47,-49,-48,-74,-50,]),'INT':([37,111,133,154,157,158,],[73,73,73,73,73,73,]),'FLOAT':([37,111,133,154,157,158,],[74,74,74,74,74,74,]),'CHARACTER':([37,111,133,154,157,158,],[75,75,75,75,75,75,]),'BOOLEAN':([37,111,133,154,157,158,],[76,76,76,76,76,76,]),'TIMES':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[81,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,81,81,81,81,81,-29,-30,-31,-75,81,81,-20,-21,81,81,81,81,81,81,81,-17,-48,-90,-46,-48,81,81,-48,-47,-49,-48,-50,81,]),'DIV':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[82,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,82,82,82,82,82,-29,-30,-31,-75,82,82,-20,-21,82,82,82,82,82,82,82,-17,-48,-90,-46,-48,82,82,-48,-47,-49,-48,-50,82,]),'LT':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[83,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,83,83,83,83,83,-29,-30,-31,-75,-18,-19,-20,-21,None,None,None,None,83,83,83,-17,-48,-90,-46,-48,83,83,-48,-47,-49,-48,-50,83,]),'GT':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[84,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,84,84,84,84,84,-29,-30,-31,-75,-18,-19,-20,-21,None,None,None,None,84,84,84,-17,-48,-90,-46,-48,84,84,-48,-47,-49,-48,-50,84,]),'LE':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[85,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,85,85,85,85,85,-29,-30,-31,-75,-18,-19,-20,-21,None,None,None,None,85,85,85,-17,-48,-90,-46,-48,85,85,-48,-47,-49,-48,-50,85,]),'GE':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[86,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,86,86,86,86,86,-29,-30,-31,-75,-18,-19,-20,-21,None,None,None,None,86,86,86,-17,-48,-90,-46,-48,86,86,-48,-47,-49,-48,-50,86,]),'EQ':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[87,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,87,87,87,87,87,-29,-30,-31,-75,-18,-19,-20,-21,-22,-23,-24,-25,None,87,87,-17,-48,-90,-46,-48,87,87,-48,-47,-49,-48,-50,87,]),'CONJUNCTION':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[88,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,88,88,88,88,88,-29,-30,-31,-75,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,88,-17,-48,-90,-46,-48,88,88,-48,-47,-49,-48,-50,88,]),'DISJUNCTION':([39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,61,62,66,70,90,93,94,95,105,112,113,114,115,116,117,118,119,120,121,122,123,124,126,144,146,148,149,159,161,171,172,175,178,],[89,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,89,89,89,89,89,-29,-30,-31,-75,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-90,-46,-48,89,89,-48,-47,-49,-48,-50,89,]),'DOT':([43,124,146,159,172,],[91,143,143,143,143,]),'BRACKETOPEN':([43,124,146,159,172,],[92,145,145,145,145,]),'STRING':([60,92,108,127,145,156,],[99,125,139,99,160,139,]),'BRACKETCLOSE':([125,160,],[146,172,]),'ELSE':([130,163,],[151,-63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'axioma':([0,174,],[1,176,]),'programa':([0,174,],[2,2,]),'empty':([0,174,],[3,3,]),'bloque_programa':([0,5,131,174,],[4,21,152,4,]),'sentencia':([0,5,131,174,],[5,5,5,5,]),'declaracion':([0,5,131,174,],[6,6,6,6,]),'asignacion':([0,5,131,174,],[7,7,7,7,]),'condicion':([0,5,131,174,],[8,8,8,8,]),'bucle':([0,5,131,174,],[9,9,9,9,]),'funcion':([0,5,131,174,],[10,10,10,10,]),'declaracion_objeto':([0,5,131,174,],[11,11,11,11,]),'asignacion_objeto':([0,5,131,174,],[12,12,12,12,]),'function_call':([0,5,29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,131,174,177,],[13,13,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,13,13,54,]),'lista_id':([0,5,34,131,174,],[15,15,68,15,15,]),'lista_id_otro':([14,38,110,],[27,78,141,]),'expresion':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[39,61,62,66,70,90,93,94,95,112,113,114,115,116,117,118,119,120,121,122,66,148,149,178,]),'binaria':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'unaria':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'acceso_propiedad':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,128,129,177,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'objeto_asg':([29,30,31,33,36,42,57,58,59,79,80,81,82,83,84,85,86,87,88,89,106,109,128,129,177,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,140,56,56,56,]),'lista_param':([33,],[64,]),'lista_param_rec':([33,106,],[65,135,]),'tipo':([37,111,133,154,157,158,],[72,72,153,165,167,169,]),'propiedades_asg':([60,127,],[96,147,]),'propiedad_asg':([60,127,],[97,97,]),'lista_arg':([63,],[103,]),'lista_arg_rec':([63,164,],[104,173,]),'objeto_dec':([69,157,158,],[107,168,170,]),'bloque_llaves':([100,101,151,],[130,132,162,]),'propiedades_dec':([108,156,],[136,166,]),'propiedad_dec':([108,156,],[137,137,]),'acceso_propiedad_rec':([124,146,159,172,],[144,161,171,175,]),'otra_condicion':([130,],[150,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> axioma","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','parsersin.py',37),
  ('axioma -> programa','axioma',1,'p_axioma','parsersin.py',42),
  ('axioma -> empty','axioma',1,'p_axioma','parsersin.py',43),
  ('programa -> bloque_programa','programa',1,'p_programa','parsersin.py',48),
  ('bloque_programa -> sentencia','bloque_programa',1,'p_bloque_programa','parsersin.py',53),
  ('bloque_programa -> sentencia bloque_programa','bloque_programa',2,'p_bloque_programa','parsersin.py',54),
  ('sentencia -> declaracion SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',63),
  ('sentencia -> asignacion SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',64),
  ('sentencia -> condicion','sentencia',1,'p_sentencia','parsersin.py',65),
  ('sentencia -> bucle','sentencia',1,'p_sentencia','parsersin.py',66),
  ('sentencia -> funcion','sentencia',1,'p_sentencia','parsersin.py',67),
  ('sentencia -> declaracion_objeto SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',68),
  ('sentencia -> asignacion_objeto SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',69),
  ('sentencia -> function_call SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',70),
  ('expresion -> binaria','expresion',1,'p_expresion','parsersin.py',78),
  ('expresion -> unaria','expresion',1,'p_expresion','parsersin.py',79),
  ('expresion -> PARENTHESISOPEN expresion PARENTHESISCLOSE','expresion',3,'p_expresion','parsersin.py',80),
  ('binaria -> expresion PLUS expresion','binaria',3,'p_binaria_aritmetica1','parsersin.py',90),
  ('binaria -> expresion MINUS expresion','binaria',3,'p_binaria_aritmetica1','parsersin.py',91),
  ('binaria -> expresion TIMES expresion','binaria',3,'p_binaria_aritmetica2','parsersin.py',138),
  ('binaria -> expresion DIV expresion','binaria',3,'p_binaria_aritmetica2','parsersin.py',139),
  ('binaria -> expresion LT expresion','binaria',3,'p_binaria_booleana1','parsersin.py',182),
  ('binaria -> expresion GT expresion','binaria',3,'p_binaria_booleana1','parsersin.py',183),
  ('binaria -> expresion LE expresion','binaria',3,'p_binaria_booleana1','parsersin.py',184),
  ('binaria -> expresion GE expresion','binaria',3,'p_binaria_booleana1','parsersin.py',185),
  ('binaria -> expresion EQ expresion','binaria',3,'p_binaria_booleana2','parsersin.py',217),
  ('binaria -> expresion CONJUNCTION expresion','binaria',3,'p_binaria_conjunto','parsersin.py',242),
  ('binaria -> expresion DISJUNCTION expresion','binaria',3,'p_binaria_conjunto','parsersin.py',243),
  ('unaria -> PLUS expresion','unaria',2,'p_unaria','parsersin.py',260),
  ('unaria -> MINUS expresion','unaria',2,'p_unaria','parsersin.py',261),
  ('unaria -> NEG expresion','unaria',2,'p_unaria','parsersin.py',262),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','parsersin.py',279),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','parsersin.py',297),
  ('expresion -> BIN','expresion',1,'p_expresion_entero','parsersin.py',298),
  ('expresion -> OCT','expresion',1,'p_expresion_entero','parsersin.py',299),
  ('expresion -> HEX','expresion',1,'p_expresion_entero','parsersin.py',300),
  ('expresion -> REAL','expresion',1,'p_expresion_real','parsersin.py',305),
  ('expresion -> NCIENT','expresion',1,'p_expresion_real','parsersin.py',306),
  ('expresion -> CHAR','expresion',1,'p_expresion_char','parsersin.py',311),
  ('expresion -> TR','expresion',1,'p_expresion_bool','parsersin.py',316),
  ('expresion -> FL','expresion',1,'p_expresion_bool','parsersin.py',317),
  ('expresion -> NULL','expresion',1,'p_expresion_nulo','parsersin.py',322),
  ('expresion -> function_call','expresion',1,'p_expresion_otra','parsersin.py',327),
  ('expresion -> acceso_propiedad','expresion',1,'p_expresion_otra','parsersin.py',328),
  ('expresion -> objeto_asg','expresion',1,'p_expresion_otra','parsersin.py',329),
  ('acceso_propiedad -> ID DOT ID acceso_propiedad_rec','acceso_propiedad',4,'p_acceso_propiedad','parsersin.py',333),
  ('acceso_propiedad -> ID BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec','acceso_propiedad',5,'p_acceso_propiedad','parsersin.py',334),
  ('acceso_propiedad_rec -> <empty>','acceso_propiedad_rec',0,'p_acceso_propiedad_rec','parsersin.py',338),
  ('acceso_propiedad_rec -> DOT ID acceso_propiedad_rec','acceso_propiedad_rec',3,'p_acceso_propiedad_rec','parsersin.py',339),
  ('acceso_propiedad_rec -> BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec','acceso_propiedad_rec',4,'p_acceso_propiedad_rec','parsersin.py',340),
  ('declaracion -> LET lista_id_otro','declaracion',2,'p_declaracion','parsersin.py',344),
  ('declaracion -> LET lista_id_otro EQUAL expresion','declaracion',4,'p_declaracion','parsersin.py',345),
  ('lista_id_otro -> ID','lista_id_otro',1,'p_lista_id_otro','parsersin.py',371),
  ('lista_id_otro -> ID COMA lista_id_otro','lista_id_otro',3,'p_lista_id_otro','parsersin.py',372),
  ('lista_id_otro -> ID COLON tipo','lista_id_otro',3,'p_lista_id_otro2','parsersin.py',385),
  ('lista_id_otro -> ID COLON tipo COMA lista_id_otro','lista_id_otro',5,'p_lista_id_otro2','parsersin.py',386),
  ('lista_id -> ID','lista_id',1,'p_lista_id','parsersin.py',397),
  ('lista_id -> ID COMA lista_id','lista_id',3,'p_lista_id','parsersin.py',398),
  ('asignacion -> lista_id EQUAL expresion','asignacion',3,'p_asignacion','parsersin.py',406),
  ('condicion -> IF PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves otra_condicion','condicion',6,'p_condicion','parsersin.py',423),
  ('otra_condicion -> <empty>','otra_condicion',0,'p_otra_condicion','parsersin.py',441),
  ('otra_condicion -> ELSE bloque_llaves','otra_condicion',2,'p_otra_condicion','parsersin.py',442),
  ('bloque_llaves -> LLAVEA bloque_programa LLAVEC','bloque_llaves',3,'p_bloque_llaves','parsersin.py',454),
  ('bucle -> WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves','bucle',5,'p_bucle','parsersin.py',460),
  ('tipo -> INT','tipo',1,'p_tipo','parsersin.py',472),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parsersin.py',473),
  ('tipo -> CHARACTER','tipo',1,'p_tipo','parsersin.py',474),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','parsersin.py',475),
  ('tipo -> ID','tipo',1,'p_tipo_objeto','parsersin.py',487),
  ('funcion -> FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA axioma RETURN expresion SEMICOLON LLAVEC','funcion',13,'p_funcion','parsersin.py',500),
  ('lista_arg -> <empty>','lista_arg',0,'p_lista_arg','parsersin.py',512),
  ('lista_arg -> lista_arg_rec','lista_arg',1,'p_lista_arg','parsersin.py',513),
  ('lista_arg_rec -> ID COLON tipo','lista_arg_rec',3,'p_lista_arg_rec','parsersin.py',519),
  ('lista_arg_rec -> ID COLON tipo COMA lista_arg_rec','lista_arg_rec',5,'p_lista_arg_rec','parsersin.py',520),
  ('function_call -> ID PARENTHESISOPEN lista_param PARENTHESISCLOSE','function_call',4,'p_function_call','parsersin.py',529),
  ('lista_param -> <empty>','lista_param',0,'p_lista_param','parsersin.py',545),
  ('lista_param -> lista_param_rec','lista_param',1,'p_lista_param','parsersin.py',546),
  ('lista_param_rec -> expresion COMA lista_param_rec','lista_param_rec',3,'p_lista_param_rec','parsersin.py',554),
  ('lista_param_rec -> expresion','lista_param_rec',1,'p_lista_param_rec','parsersin.py',555),
  ('declaracion_objeto -> TYPE ID EQUAL objeto_dec','declaracion_objeto',4,'p_declaracion_objeto','parsersin.py',566),
  ('objeto_dec -> LLAVEA propiedades_dec LLAVEC','objeto_dec',3,'p_objeto_dec','parsersin.py',587),
  ('propiedades_dec -> <empty>','propiedades_dec',0,'p_propiedades_dec','parsersin.py',593),
  ('propiedades_dec -> propiedad_dec','propiedades_dec',1,'p_propiedades_dec','parsersin.py',594),
  ('propiedades_dec -> propiedad_dec COMA propiedades_dec','propiedades_dec',3,'p_propiedades_dec','parsersin.py',595),
  ('propiedad_dec -> ID COLON tipo','propiedad_dec',3,'p_propiedad_dec','parsersin.py',605),
  ('propiedad_dec -> STRING COLON tipo','propiedad_dec',3,'p_propiedad_dec','parsersin.py',606),
  ('propiedad_dec -> ID COLON objeto_dec','propiedad_dec',3,'p_propeidad_dec2','parsersin.py',614),
  ('propiedad_dec -> STRING COLON objeto_dec','propiedad_dec',3,'p_propeidad_dec2','parsersin.py',615),
  ('asignacion_objeto -> LET ID COLON ID EQUAL objeto_asg','asignacion_objeto',6,'p_asignacion_objeto','parsersin.py',621),
  ('objeto_asg -> LLAVEA propiedades_asg LLAVEC','objeto_asg',3,'p_objeto_asg','parsersin.py',663),
  ('propiedades_asg -> <empty>','propiedades_asg',0,'p_propiedades_asg','parsersin.py',668),
  ('propiedades_asg -> propiedad_asg','propiedades_asg',1,'p_propiedades_asg','parsersin.py',669),
  ('propiedades_asg -> propiedad_asg COMA propiedades_asg','propiedades_asg',3,'p_propiedades_asg','parsersin.py',670),
  ('propiedad_asg -> ID COLON expresion','propiedad_asg',3,'p_propiedad_asg','parsersin.py',680),
  ('propiedad_asg -> STRING COLON expresion','propiedad_asg',3,'p_propiedad_asg','parsersin.py',681),
]
