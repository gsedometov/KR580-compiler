import ply.lex as lex

from symbols import cmds, rg_names, tokens

def t_DECLARATION(t):
    r'[A-Za-z]+[0-9]*\:'
    line = t.lexer.counter
    if line - t.lexer.last_declaration == 1:
        line -= 1
    t.lexer.symtable[t.value[:-1]] = line
    t.lexer.last_declaration = t.lexer.counter

def t_CMD(t):
    r'([A-Z]|[a-z])+\b'
    if t.value in cmds:
        t.type = 'CMD'
    elif t.value in rg_names:
        t.type = 'RG_NAME'
    else:
        t.type = 'ID'
    t.lexer.counter += 1
    return t

t_ID = r'[A-Za-z]*[0-9]+'

def t_WORD(t):
    r'([\da-f0-9]{2}){1}'
    t.value = int(t.value, 16)
    t.lexer.counter += 1
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = '\t, '

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.symtable = {}
lexer.last_declaration = 0
lexer.counter = 0
