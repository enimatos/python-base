#!/usr/bin/env python3
""" Hello World Multi Linguas

Dependendo dca lingua configurada no ambiente o programa exibr a mensagem correspondente 

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__autor__ = "Elaine Matos"
__license__ = "Unlicense"
# Dunder

import os
current_language = os.getenv("LANG", "en_US")[:5]
#snake Case

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Mondo!"
print(msg)