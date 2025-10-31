###
# 03 - qUANTIFIERS
# Los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena.
###


import re

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"
macthes = re.findall(pattern, text)
print(macthes)  # ['aaa', '', 'a', '']
