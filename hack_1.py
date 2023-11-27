"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(texto):
    if len(texto) <= 2:
        return texto
    else:
        texto = texto[0] + texto[1].upper() + texto[2:]
        if len(texto) >= 5:
            texto = texto[:4] + texto[4].upper() + texto[5:]
            return texto
        else:
            return texto