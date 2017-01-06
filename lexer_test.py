from lexer import lexer
import pytest

def test_nop():
    lexer.input('NOP')
    t = lexer.next()
    assert t.type == 'CMD', t.value == 'NOP'

def test_lxi():
    lexer.input('LXI h, 0820')
    t = lexer.next()
    assert t.type == 'CMD', t.value == 'LXI'

def test_stax():
    lexer.input('STAX b')
    t = lexer.next()
    assert t.type == 'CMD', t.value == 'STAX'

def test_shld():
    lexer.input('SHLD 0820')
    t = lexer.next()
    assert t.type == 'CMD', t.value == 'SHLD'

def test_id():
    lexer.input('LABEL2')
    assert lexer.next().type == 'ID'

def test_rg_name():
    lexer.input('A SP')
    assert lexer.next().type == 'RG_NAME'
    assert lexer.next().type == 'RG_NAME'

def test_single_word():
    lexer.input('12')
    t = lexer.next()
    assert t.type == 'WORD', t.value == 0x12

def test_word():
    lexer.input('12\n0915')
    for i in [12, 9, 15]:
        t = lexer.next()
        assert t.type == 'WORD', t.value == i

def test_label_declaration():
    lexer.counter = 0
    lexer.input('LABEL0:\n\nLABEL1:')
    for t in lexer:
        print(t)
    print(lexer.symtable)
    assert lexer.symtable['LABEL0'] == 0
    assert lexer.symtable['LABEL1'] == 0
