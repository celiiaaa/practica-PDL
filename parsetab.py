
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'axiomaleftDISJUNCTIONleftCONJUNCTIONnonassocEQnonassocLTGTLEGEleftPLUSMINUSleftTIMESDIVrightUPLUSUMINUSrightNEGBIN BOOLEAN BRACKETCLOSE BRACKETOPEN CHAR CHARACTER COLON COMA CONJUNCTION DISJUNCTION DIV DOT ELSE ENTERO EQ EQUAL FL FLOAT FUNCTION GE GT HEX ID IF INT LE LET LLAVEA LLAVEC LT MINUS NCIENT NEG NULL OCT PARENTHESISCLOSE PARENTHESISOPEN PLUS REAL RETURN SEMICOLON STRING TIMES TR TYPE WHILEempty :axioma : programa\n                  | emptyprograma : bloque_programabloque_programa : sentencia\n                           | sentencia bloque_programasentencia : declaracion SEMICOLON\n                     | asignacion SEMICOLON\n                     | condicion\n                     | bucle \n                     | funcion\n                     | declaracion_objeto SEMICOLON\n                     | asignacion_objeto SEMICOLON\n                     | function_call SEMICOLONexpresion : binaria\n                     | unaria\n                     | PARENTHESISOPEN expresion PARENTHESISCLOSEbinaria : expresion PLUS expresion\n                   | expresion MINUS expresionbinaria : expresion TIMES expresion\n                   | expresion DIV expresionbinaria : expresion LT expresion\n                   | expresion GT expresion\n                   | expresion LE expresion\n                   | expresion GE expresionbinaria : expresion EQ expresionbinaria : expresion CONJUNCTION expresion\n                   | expresion DISJUNCTION expresionunaria : PLUS expresion %prec UPLUS\n                  | MINUS expresion %prec UMINUS\n                  | NEG expresionexpresion : IDexpresion : ENTERO\n                     | BIN\n                     | OCT\n                     | HEXexpresion : REAL\n                     | NCIENTexpresion : CHARexpresion : TR\n                     | FLexpresion : NULLexpresion : function_call\n                     | acceso_propiedad\n                     | objeto_asgacceso_propiedad : ID DOT ID acceso_propiedad_rec\n                            | ID BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_recacceso_propiedad_rec : \n                                | DOT ID acceso_propiedad_rec\n                                | BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_recdeclaracion : LET lista_id\n                       | LET lista_id EQUAL expresionlista_id : ID\n                    | ID COMA lista_idasignacion : lista_id EQUAL expresioncondicion : IF PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves otra_condicionotra_condicion : \n                          | ELSE bloque_llavesbloque_llaves : LLAVEA bloque_programa LLAVECbucle : WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llavestipo : INT\n                | FLOAT\n                | CHARACTER\n                | BOOLEANfuncion : FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA axioma RETURN expresion SEMICOLON LLAVEClista_arg : \n                     | lista_arg_reclista_arg_rec : ID COLON tipo\n                         | ID COLON tipo COMA lista_arg_recfunction_call : ID PARENTHESISOPEN lista_param PARENTHESISCLOSElista_param : \n                       | lista_param_reclista_param_rec : expresion COMA lista_param_rec\n                           | expresiondeclaracion_objeto : TYPE ID EQUAL objeto_decobjeto_dec : LLAVEA propiedades_dec LLAVECpropiedades_dec : \n                           | propiedad_dec\n                           | propiedad_dec COMA propiedades_decpropiedad_dec : ID COLON tipo\n                         | STRING COLON tipopropiedad_dec : ID COLON ID\n                         | STRING COLON IDpropiedad_dec : ID COLON objeto_dec\n                         | STRING COLON objeto_decasignacion_objeto : LET ID COLON ID\n                             | LET ID COLON ID EQUAL objeto_asgobjeto_asg : LLAVEA propiedades_asg LLAVECpropiedades_asg : \n                           | propiedad_asg\n                           | propiedad_asg COMA propiedades_asgpropiedad_asg : ID COLON expresion\n                         | STRING COLON expresion'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,8,9,10,21,22,23,24,25,26,120,122,138,154,155,174,],[-1,0,-2,-3,-4,-5,-9,-10,-11,-6,-7,-8,-12,-13,-14,-57,-60,-56,-58,-59,-65,]),'LET':([0,5,8,9,10,22,23,24,25,26,120,121,122,138,154,155,168,174,],[14,14,-9,-10,-11,-7,-8,-12,-13,-14,-57,14,-60,-56,-58,-59,14,-65,]),'IF':([0,5,8,9,10,22,23,24,25,26,120,121,122,138,154,155,168,174,],[16,16,-9,-10,-11,-7,-8,-12,-13,-14,-57,16,-60,-56,-58,-59,16,-65,]),'WHILE':([0,5,8,9,10,22,23,24,25,26,120,121,122,138,154,155,168,174,],[17,17,-9,-10,-11,-7,-8,-12,-13,-14,-57,17,-60,-56,-58,-59,17,-65,]),'FUNCTION':([0,5,8,9,10,22,23,24,25,26,120,121,122,138,154,155,168,174,],[18,18,-9,-10,-11,-7,-8,-12,-13,-14,-57,18,-60,-56,-58,-59,18,-65,]),'TYPE':([0,5,8,9,10,22,23,24,25,26,120,121,122,138,154,155,168,174,],[20,20,-9,-10,-11,-7,-8,-12,-13,-14,-57,20,-60,-56,-58,-59,20,-65,]),'ID':([0,5,8,9,10,14,18,20,22,23,24,25,26,29,30,31,33,34,36,37,41,56,57,58,59,62,71,72,73,74,75,76,77,78,79,80,81,83,98,100,117,118,119,120,121,122,131,138,148,149,150,154,155,156,168,171,174,],[19,19,-9,-10,-11,28,32,35,-7,-8,-12,-13,-14,42,42,42,42,66,42,70,42,42,42,42,90,94,42,42,42,42,42,42,42,42,42,42,42,114,42,128,90,42,42,-57,19,-60,151,-56,128,159,163,-58,-59,94,19,42,-65,]),'RETURN':([2,3,4,5,8,9,10,21,22,23,24,25,26,120,122,138,154,155,168,170,174,],[-2,-3,-4,-5,-9,-10,-11,-6,-7,-8,-12,-13,-14,-57,-60,-56,-58,-59,-1,171,-65,]),'LLAVEC':([5,8,9,10,21,22,23,24,25,26,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,59,85,86,87,88,89,97,100,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,120,122,126,127,132,134,135,136,137,138,140,142,143,144,145,147,148,151,153,154,155,158,159,160,161,162,163,164,165,166,169,173,174,],[-5,-9,-10,-11,-6,-7,-8,-12,-13,-14,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-89,-29,-30,-31,116,-90,-70,-77,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-88,-89,-57,-60,147,-78,-46,-48,-91,-92,-93,-56,155,-61,-62,-63,-64,-76,-77,-48,-47,-58,-59,-79,-82,-80,-84,-81,-83,-85,-49,-48,-50,174,-65,]),'SEMICOLON':([6,7,11,12,13,27,28,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,66,67,69,70,85,86,87,97,99,102,103,104,105,106,107,108,109,110,111,112,113,114,116,130,132,134,147,151,153,165,166,169,172,],[22,23,24,25,26,-51,-53,-55,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-53,-54,-52,-86,-29,-30,-31,-70,-75,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-88,-87,-46,-48,-76,-48,-47,-49,-48,-50,173,]),'EQUAL':([15,19,27,28,35,66,67,70,],[29,-53,36,-53,68,-53,-54,101,]),'PARENTHESISOPEN':([16,17,19,29,30,31,32,33,36,41,42,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[30,31,33,41,41,41,62,41,41,41,33,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'COMA':([19,28,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,65,66,85,86,87,89,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,127,132,134,136,137,141,142,143,144,145,147,151,153,159,160,161,162,163,164,165,166,169,],[34,34,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,98,34,-29,-30,-31,117,-70,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-88,148,-46,-48,-92,-93,156,-61,-62,-63,-64,-76,-48,-47,-82,-80,-84,-81,-83,-85,-49,-48,-50,]),'COLON':([28,90,91,94,124,128,129,],[37,118,119,123,146,149,150,]),'ENTERO':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'BIN':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'OCT':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'HEX':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'REAL':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'NCIENT':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'CHAR':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'TR':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'FL':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'NULL':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'PLUS':([29,30,31,33,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61,65,69,71,72,73,74,75,76,77,78,79,80,81,82,85,86,87,97,98,102,103,104,105,106,107,108,109,110,111,112,113,114,116,118,119,132,134,136,137,151,153,165,166,169,171,172,],[56,56,56,56,56,71,-15,-16,56,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,56,56,56,71,71,71,71,56,56,56,56,56,56,56,56,56,56,56,71,-29,-30,-31,-70,56,-18,-19,-20,-21,71,71,71,71,71,71,71,-17,-48,-88,56,56,-46,-48,71,71,-48,-47,-49,-48,-50,56,71,]),'MINUS':([29,30,31,33,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61,65,69,71,72,73,74,75,76,77,78,79,80,81,82,85,86,87,97,98,102,103,104,105,106,107,108,109,110,111,112,113,114,116,118,119,132,134,136,137,151,153,165,166,169,171,172,],[57,57,57,57,57,72,-15,-16,57,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,57,57,57,72,72,72,72,57,57,57,57,57,57,57,57,57,57,57,72,-29,-30,-31,-70,57,-18,-19,-20,-21,72,72,72,72,72,72,72,-17,-48,-88,57,57,-46,-48,72,72,-48,-47,-49,-48,-50,57,72,]),'NEG':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'LLAVEA':([29,30,31,33,36,41,56,57,58,68,71,72,73,74,75,76,77,78,79,80,81,92,93,98,101,118,119,139,142,143,144,145,149,150,157,171,],[59,59,59,59,59,59,59,59,59,100,59,59,59,59,59,59,59,59,59,59,59,121,121,59,59,59,59,121,-61,-62,-63,-64,100,100,168,59,]),'PARENTHESISCLOSE':([33,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,62,63,64,65,82,85,86,87,95,96,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,125,132,134,141,142,143,144,145,151,153,165,166,167,169,],[-71,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,92,93,-66,97,-72,-74,113,-29,-30,-31,124,-67,-70,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-88,-73,-46,-48,-68,-61,-62,-63,-64,-48,-47,-49,-48,-69,-50,]),'TIMES':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[73,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,73,73,73,73,73,-29,-30,-31,-70,73,73,-20,-21,73,73,73,73,73,73,73,-17,-48,-88,-46,-48,73,73,-48,-47,-49,-48,-50,73,]),'DIV':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[74,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,74,74,74,74,74,-29,-30,-31,-70,74,74,-20,-21,74,74,74,74,74,74,74,-17,-48,-88,-46,-48,74,74,-48,-47,-49,-48,-50,74,]),'LT':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[75,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,75,75,75,75,75,-29,-30,-31,-70,-18,-19,-20,-21,None,None,None,None,75,75,75,-17,-48,-88,-46,-48,75,75,-48,-47,-49,-48,-50,75,]),'GT':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[76,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,76,76,76,76,76,-29,-30,-31,-70,-18,-19,-20,-21,None,None,None,None,76,76,76,-17,-48,-88,-46,-48,76,76,-48,-47,-49,-48,-50,76,]),'LE':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[77,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,77,77,77,77,77,-29,-30,-31,-70,-18,-19,-20,-21,None,None,None,None,77,77,77,-17,-48,-88,-46,-48,77,77,-48,-47,-49,-48,-50,77,]),'GE':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[78,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,78,78,78,78,78,-29,-30,-31,-70,-18,-19,-20,-21,None,None,None,None,78,78,78,-17,-48,-88,-46,-48,78,78,-48,-47,-49,-48,-50,78,]),'EQ':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[79,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,79,79,79,79,79,-29,-30,-31,-70,-18,-19,-20,-21,-22,-23,-24,-25,None,79,79,-17,-48,-88,-46,-48,79,79,-48,-47,-49,-48,-50,79,]),'CONJUNCTION':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[80,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,80,80,80,80,80,-29,-30,-31,-70,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,80,-17,-48,-88,-46,-48,80,80,-48,-47,-49,-48,-50,80,]),'DISJUNCTION':([38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,60,61,65,69,82,85,86,87,97,102,103,104,105,106,107,108,109,110,111,112,113,114,116,132,134,136,137,151,153,165,166,169,172,],[81,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,81,81,81,81,81,-29,-30,-31,-70,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-17,-48,-88,-46,-48,81,81,-48,-47,-49,-48,-50,81,]),'DOT':([42,114,134,151,166,],[83,131,131,131,131,]),'BRACKETOPEN':([42,114,134,151,166,],[84,133,133,133,133,]),'STRING':([59,84,100,117,133,148,],[91,115,129,91,152,129,]),'BRACKETCLOSE':([115,152,],[134,166,]),'ELSE':([120,155,],[139,-59,]),'INT':([123,146,149,150,],[142,142,142,142,]),'FLOAT':([123,146,149,150,],[143,143,143,143,]),'CHARACTER':([123,146,149,150,],[144,144,144,144,]),'BOOLEAN':([123,146,149,150,],[145,145,145,145,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'axioma':([0,168,],[1,170,]),'programa':([0,168,],[2,2,]),'empty':([0,168,],[3,3,]),'bloque_programa':([0,5,121,168,],[4,21,140,4,]),'sentencia':([0,5,121,168,],[5,5,5,5,]),'declaracion':([0,5,121,168,],[6,6,6,6,]),'asignacion':([0,5,121,168,],[7,7,7,7,]),'condicion':([0,5,121,168,],[8,8,8,8,]),'bucle':([0,5,121,168,],[9,9,9,9,]),'funcion':([0,5,121,168,],[10,10,10,10,]),'declaracion_objeto':([0,5,121,168,],[11,11,11,11,]),'asignacion_objeto':([0,5,121,168,],[12,12,12,12,]),'function_call':([0,5,29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,121,168,171,],[13,13,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,13,13,53,]),'lista_id':([0,5,14,34,121,168,],[15,15,27,67,15,15,]),'expresion':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[38,60,61,65,69,82,85,86,87,102,103,104,105,106,107,108,109,110,111,112,65,136,137,172,]),'binaria':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'unaria':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'acceso_propiedad':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,118,119,171,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'objeto_asg':([29,30,31,33,36,41,56,57,58,71,72,73,74,75,76,77,78,79,80,81,98,101,118,119,171,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,130,55,55,55,]),'lista_param':([33,],[63,]),'lista_param_rec':([33,98,],[64,125,]),'propiedades_asg':([59,117,],[88,135,]),'propiedad_asg':([59,117,],[89,89,]),'lista_arg':([62,],[95,]),'lista_arg_rec':([62,156,],[96,167,]),'objeto_dec':([68,149,150,],[99,161,164,]),'bloque_llaves':([92,93,139,],[120,122,154,]),'propiedades_dec':([100,148,],[126,158,]),'propiedad_dec':([100,148,],[127,127,]),'acceso_propiedad_rec':([114,134,151,166,],[132,153,165,169,]),'otra_condicion':([120,],[138,]),'tipo':([123,146,149,150,],[141,157,160,162,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> axioma","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','parsersin.py',33),
  ('axioma -> programa','axioma',1,'p_axioma','parsersin.py',38),
  ('axioma -> empty','axioma',1,'p_axioma','parsersin.py',39),
  ('programa -> bloque_programa','programa',1,'p_programa','parsersin.py',44),
  ('bloque_programa -> sentencia','bloque_programa',1,'p_bloque_programa','parsersin.py',49),
  ('bloque_programa -> sentencia bloque_programa','bloque_programa',2,'p_bloque_programa','parsersin.py',50),
  ('sentencia -> declaracion SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',59),
  ('sentencia -> asignacion SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',60),
  ('sentencia -> condicion','sentencia',1,'p_sentencia','parsersin.py',61),
  ('sentencia -> bucle','sentencia',1,'p_sentencia','parsersin.py',62),
  ('sentencia -> funcion','sentencia',1,'p_sentencia','parsersin.py',63),
  ('sentencia -> declaracion_objeto SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',64),
  ('sentencia -> asignacion_objeto SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',65),
  ('sentencia -> function_call SEMICOLON','sentencia',2,'p_sentencia','parsersin.py',66),
  ('expresion -> binaria','expresion',1,'p_expresion','parsersin.py',74),
  ('expresion -> unaria','expresion',1,'p_expresion','parsersin.py',75),
  ('expresion -> PARENTHESISOPEN expresion PARENTHESISCLOSE','expresion',3,'p_expresion','parsersin.py',76),
  ('binaria -> expresion PLUS expresion','binaria',3,'p_binaria_aritmetica1','parsersin.py',86),
  ('binaria -> expresion MINUS expresion','binaria',3,'p_binaria_aritmetica1','parsersin.py',87),
  ('binaria -> expresion TIMES expresion','binaria',3,'p_binaria_aritmetica2','parsersin.py',128),
  ('binaria -> expresion DIV expresion','binaria',3,'p_binaria_aritmetica2','parsersin.py',129),
  ('binaria -> expresion LT expresion','binaria',3,'p_binaria_booleana1','parsersin.py',172),
  ('binaria -> expresion GT expresion','binaria',3,'p_binaria_booleana1','parsersin.py',173),
  ('binaria -> expresion LE expresion','binaria',3,'p_binaria_booleana1','parsersin.py',174),
  ('binaria -> expresion GE expresion','binaria',3,'p_binaria_booleana1','parsersin.py',175),
  ('binaria -> expresion EQ expresion','binaria',3,'p_binaria_booleana2','parsersin.py',207),
  ('binaria -> expresion CONJUNCTION expresion','binaria',3,'p_binaria_conjunto','parsersin.py',231),
  ('binaria -> expresion DISJUNCTION expresion','binaria',3,'p_binaria_conjunto','parsersin.py',232),
  ('unaria -> PLUS expresion','unaria',2,'p_unaria','parsersin.py',249),
  ('unaria -> MINUS expresion','unaria',2,'p_unaria','parsersin.py',250),
  ('unaria -> NEG expresion','unaria',2,'p_unaria','parsersin.py',251),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','parsersin.py',268),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','parsersin.py',280),
  ('expresion -> BIN','expresion',1,'p_expresion_entero','parsersin.py',281),
  ('expresion -> OCT','expresion',1,'p_expresion_entero','parsersin.py',282),
  ('expresion -> HEX','expresion',1,'p_expresion_entero','parsersin.py',283),
  ('expresion -> REAL','expresion',1,'p_expresion_real','parsersin.py',288),
  ('expresion -> NCIENT','expresion',1,'p_expresion_real','parsersin.py',289),
  ('expresion -> CHAR','expresion',1,'p_expresion_char','parsersin.py',294),
  ('expresion -> TR','expresion',1,'p_expresion_bool','parsersin.py',299),
  ('expresion -> FL','expresion',1,'p_expresion_bool','parsersin.py',300),
  ('expresion -> NULL','expresion',1,'p_expresion_nulo','parsersin.py',308),
  ('expresion -> function_call','expresion',1,'p_expresion_otra','parsersin.py',313),
  ('expresion -> acceso_propiedad','expresion',1,'p_expresion_otra','parsersin.py',314),
  ('expresion -> objeto_asg','expresion',1,'p_expresion_otra','parsersin.py',315),
  ('acceso_propiedad -> ID DOT ID acceso_propiedad_rec','acceso_propiedad',4,'p_acceso_propiedad','parsersin.py',319),
  ('acceso_propiedad -> ID BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec','acceso_propiedad',5,'p_acceso_propiedad','parsersin.py',320),
  ('acceso_propiedad_rec -> <empty>','acceso_propiedad_rec',0,'p_acceso_propiedad_rec','parsersin.py',324),
  ('acceso_propiedad_rec -> DOT ID acceso_propiedad_rec','acceso_propiedad_rec',3,'p_acceso_propiedad_rec','parsersin.py',325),
  ('acceso_propiedad_rec -> BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec','acceso_propiedad_rec',4,'p_acceso_propiedad_rec','parsersin.py',326),
  ('declaracion -> LET lista_id','declaracion',2,'p_declaracion','parsersin.py',330),
  ('declaracion -> LET lista_id EQUAL expresion','declaracion',4,'p_declaracion','parsersin.py',331),
  ('lista_id -> ID','lista_id',1,'p_lista_id','parsersin.py',353),
  ('lista_id -> ID COMA lista_id','lista_id',3,'p_lista_id','parsersin.py',354),
  ('asignacion -> lista_id EQUAL expresion','asignacion',3,'p_asignacion','parsersin.py',362),
  ('condicion -> IF PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves otra_condicion','condicion',6,'p_condicion','parsersin.py',379),
  ('otra_condicion -> <empty>','otra_condicion',0,'p_otra_condicion','parsersin.py',397),
  ('otra_condicion -> ELSE bloque_llaves','otra_condicion',2,'p_otra_condicion','parsersin.py',398),
  ('bloque_llaves -> LLAVEA bloque_programa LLAVEC','bloque_llaves',3,'p_bloque_llaves','parsersin.py',410),
  ('bucle -> WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves','bucle',5,'p_bucle','parsersin.py',416),
  ('tipo -> INT','tipo',1,'p_tipo','parsersin.py',428),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parsersin.py',429),
  ('tipo -> CHARACTER','tipo',1,'p_tipo','parsersin.py',430),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','parsersin.py',431),
  ('funcion -> FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA axioma RETURN expresion SEMICOLON LLAVEC','funcion',13,'p_funcion','parsersin.py',451),
  ('lista_arg -> <empty>','lista_arg',0,'p_lista_arg','parsersin.py',473),
  ('lista_arg -> lista_arg_rec','lista_arg',1,'p_lista_arg','parsersin.py',474),
  ('lista_arg_rec -> ID COLON tipo','lista_arg_rec',3,'p_lista_arg_rec','parsersin.py',482),
  ('lista_arg_rec -> ID COLON tipo COMA lista_arg_rec','lista_arg_rec',5,'p_lista_arg_rec','parsersin.py',483),
  ('function_call -> ID PARENTHESISOPEN lista_param PARENTHESISCLOSE','function_call',4,'p_function_call','parsersin.py',491),
  ('lista_param -> <empty>','lista_param',0,'p_lista_param','parsersin.py',497),
  ('lista_param -> lista_param_rec','lista_param',1,'p_lista_param','parsersin.py',498),
  ('lista_param_rec -> expresion COMA lista_param_rec','lista_param_rec',3,'p_lista_param_rec','parsersin.py',502),
  ('lista_param_rec -> expresion','lista_param_rec',1,'p_lista_param_rec','parsersin.py',503),
  ('declaracion_objeto -> TYPE ID EQUAL objeto_dec','declaracion_objeto',4,'p_declaracion_objeto','parsersin.py',509),
  ('objeto_dec -> LLAVEA propiedades_dec LLAVEC','objeto_dec',3,'p_objeto_dec','parsersin.py',528),
  ('propiedades_dec -> <empty>','propiedades_dec',0,'p_propiedades_dec','parsersin.py',533),
  ('propiedades_dec -> propiedad_dec','propiedades_dec',1,'p_propiedades_dec','parsersin.py',534),
  ('propiedades_dec -> propiedad_dec COMA propiedades_dec','propiedades_dec',3,'p_propiedades_dec','parsersin.py',535),
  ('propiedad_dec -> ID COLON tipo','propiedad_dec',3,'p_propiedad_dec','parsersin.py',545),
  ('propiedad_dec -> STRING COLON tipo','propiedad_dec',3,'p_propiedad_dec','parsersin.py',546),
  ('propiedad_dec -> ID COLON ID','propiedad_dec',3,'p_propiedad_dec2','parsersin.py',554),
  ('propiedad_dec -> STRING COLON ID','propiedad_dec',3,'p_propiedad_dec2','parsersin.py',555),
  ('propiedad_dec -> ID COLON objeto_dec','propiedad_dec',3,'p_propeidad_dec3','parsersin.py',565),
  ('propiedad_dec -> STRING COLON objeto_dec','propiedad_dec',3,'p_propeidad_dec3','parsersin.py',566),
  ('asignacion_objeto -> LET ID COLON ID','asignacion_objeto',4,'p_asignacion_objeto','parsersin.py',572),
  ('asignacion_objeto -> LET ID COLON ID EQUAL objeto_asg','asignacion_objeto',6,'p_asignacion_objeto','parsersin.py',573),
  ('objeto_asg -> LLAVEA propiedades_asg LLAVEC','objeto_asg',3,'p_objeto_asg','parsersin.py',577),
  ('propiedades_asg -> <empty>','propiedades_asg',0,'p_propiedades_asg','parsersin.py',581),
  ('propiedades_asg -> propiedad_asg','propiedades_asg',1,'p_propiedades_asg','parsersin.py',582),
  ('propiedades_asg -> propiedad_asg COMA propiedades_asg','propiedades_asg',3,'p_propiedades_asg','parsersin.py',583),
  ('propiedad_asg -> ID COLON expresion','propiedad_asg',3,'p_propiedad_asg','parsersin.py',587),
  ('propiedad_asg -> STRING COLON expresion','propiedad_asg',3,'p_propiedad_asg','parsersin.py',588),
]
