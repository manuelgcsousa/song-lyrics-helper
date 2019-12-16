#!/usr/bin/env python3

import sys
sys.path.append('../')

import re
import pdfkit
import random
import yake
from flask import Flask, render_template, request, make_response
from jinja2 import Template
from utils.en_dict import build_dict_en
from utils.pt_dict import build_dict_pt
from utils.random_dict import build_dict_random

app = Flask(__name__)

global lang
global summary
global keywords

@app.route('/add', methods=['POST'])
def add_keyword():
    global keywords

    if request.method == 'POST':
        keyword = request.form['word']
        
        if (keyword != ''):
            print('add_keyword: ' + keyword)

            if not keyword in keywords:
                keywords.append(keyword)

            print(keywords)
            return render_template('index.html', keywords=keywords)
    
    return render_template('index.html', error_add=True, keywords=keywords)

@app.route('/remove', methods=['POST'])
def remove_keyword():
    global keywords
    
    if request.method == 'POST':
        keyword = request.form['word']
        print('remove_keyword: ' + keyword)
        
        if keyword in keywords:
            keywords.remove(keyword)
        
        print(keywords)
        return render_template('index.html', keywords=keywords)

@app.route('/generate', methods=['POST'])
def gen_sugestions():
    global lang
    global summary
    global keywords

    if request.method == 'POST':
        # Encontrar rimas e similaridades para cada palavra.
        if (lang == 'pt'):
            dict_words = build_dict_pt(keywords)
        else:
            dict_words = build_dict_en(keywords)
        
        # Construir o dicionário aleatório
        dict_random = build_dict_random(dict_words)

        html_text = open('templates/suggestion.html', 'r').read()
        template = Template(html_text)

        html = template.render(summary=summary, words=dict_random)
        print(html)

        pdf = pdfkit.from_string(html, False)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=worksheet.pdf'

        return response


@app.route('/', methods=['GET', 'POST'])
def index():
    global lang
    global summary
    global keywords

    if request.method == 'POST':
        resumo = request.form['resumo']
        opt    = request.form['lang_opt']
        
        if (resumo != ''):    
            summary = resumo
            lang    = opt
            
            extractor  = yake.KeywordExtractor(lan="{}".format(opt), n=1, top=10)
            extraction = extractor.extract_keywords(resumo)

            keywords = [t[0] for t in extraction]

            return render_template('index.html', keywords=keywords)
 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
