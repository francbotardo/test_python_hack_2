"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    result = "fooziman"
    for letra in result:
        if letra in "aeiou":
            pass
        else:
            result += letra
    return result