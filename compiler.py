import ply.yacc as yacc

from compiler_utils import construct_list, resolve_name
from lexer import lexer, tokens

def p_exp_list(p):
    """exp_list : exp_list term
                | term
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = construct_list(p[1], p[2])

def p_ID(p):
    'term : ID'
    addr = lexer.symtable[p[1]]
    p[0] = [addr & 0xFF, addr >> 8]

def p_two_rg_names(p):
    'term : CMD RG_NAME RG_NAME'
    opcode = resolve_name(p)
    p[0] = opcode

def p_two_words(p):
    'term : CMD WORD WORD'
    opcode = resolve_name(p[:2])
    p[0] = [opcode, p[3], p[2]]

def p_rg_name_cmd(p):
    'term : CMD RG_NAME'
    opcode = resolve_name(p)
    p[0] = opcode

def p_one_word(p):
    'term : CMD WORD'
    opcode = resolve_name(p[:2])
    p[0] = [opcode, p[2]] #format_hex(opcode) + format_hex(p[2])

def p_nular(p):
    'term : CMD'
    opcode = resolve_name(p)
    p[0] = opcode

def p_word(p):
    'term : WORD'
    p[0] = p[1]

parser = yacc.yacc()
