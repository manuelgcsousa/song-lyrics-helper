#!/usr/bin/env python3

import sys
sys.path.append('../')

import json
import pdfkit
from jinja2 import Template
from utils.en_dict import build_dict_en
from utils.pt_dict import build_dict_pt
from utils.gen_html import gen_html
from utils.random_dict import build_dict_random

doc = '''
    Programa que dada uma lista de palavras trata de construir
    um dicionário contendo rimas e palavras similares.

    => FLAGS:
       -o -> Indica o formato do output (json || html || pdf);
       -l -> Indica a língua (pt || en);
       -w -> Indica que seguidamente se apresentam palavras.

       Ex.: ./main.py -o html -l pt -w cão gato sapato
'''

def main():
    if (len(sys.argv[1:]) >= 6):
        flag_output = sys.argv[1]
        flag_lang   = sys.argv[3]
        flag_words  = sys.argv[5]
        
        if (flag_output == '-o' and flag_lang == '-l' and flag_words == '-w'):
            output = sys.argv[2] 
            lang   = sys.argv[4]
            words  = sys.argv[6:]
            
            if (output == 'json' or output == 'html' or output == 'pdf'):
                dict_words = {}
                if (lang == 'pt'):
                    dict_words = build_dict_pt(words)
                elif (lang == 'en'):
                    dict_words = build_dict_en(words)
                else:
                    print('Error: Language not available...')
                    return
                
                if (output == 'json'):
                    # Escreve o dicionário num ficheiro JSON.
                    with open('./out/json/suggestions.json', 'w') as out:
                        json.dump(dict_words, out)
                elif (output == 'html'):
                    # Função que gera as diversas páginas HTML para consulta.
                    gen_html(lang, dict_words)
                else:
                    # Construir o dicionário aleatório
                    dict_random = build_dict_random(dict_words)

                    html_text = open('templates/suggestion.html', 'r').read()
                    template = Template(html_text)

                    html = template.render(summary='Não está disponível...', words=dict_random)

                    # Gerar pdf com as sugestões.
                    pdf = pdfkit.from_string(html, 'out/pdf/worksheet.pdf')
            else:
                print('Error: Output formar not available...')
        else:
            print('Error: Options not available...')
    elif (sys.argv[1] == '-h'):
        print(doc)   
    else:
        print('Error: Incorrect number of arguments...')


if __name__ == '__main__':
    main()
