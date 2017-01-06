from compiler import parser

def test_labels():
    assert parser.parse('LABEL0:\nJMP LABEL0\nMOV A, M\nLABEL1:\nMOV A, M\nJMP LABEL1') == [0xC3, 0x00, 0x00, 0x7E, 0x7E, 0xC3, 0x04, 0x00]

def test_nullar():
    assert parser.parse('NOP') == 0x00
    assert parser.parse('STC') == 0x37
    assert parser.parse('RC') == 0xD8

def test_two_rg():
    assert parser.parse('MOV M, A') == 0x77
    assert parser.parse('MOV C, L') == 0x4D

def test_one_num():
    assert parser.parse('CMA 09') == [0x2F, 0x09]

def test_address():
    assert parser.parse('CALL 0830') == [0xCD, 0x30, 0x08]

def test_multiline():
    assert parser.parse('STA 1918\nMOV A, M\nMOV A, M') == [0x32, 0x18, 0x19, 0x7E, 0x7E]
