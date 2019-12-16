from bs4 import BeautifulSoup
import re
import subprocess

url_rhymit = 'http://www.rhymit.com/pt/palavras-que-rimam-com-'
url_lexico = 'https://www.lexico.pt/'

def clean_words(input_words):
    words = []
    
    for w in input_words:
        word = w.lower()
        
        if re.search(r'ã|â|á|à', word):
            words.append(re.sub(r'ã|â|á|à', r'a', word))
        elif re.search(r'ê|é|è', word):
            words.append(re.sub(r'ê|é|è', r'e', word))
        elif re.search(r'î|í|ì', word):
            words.append(re.sub(r'î|í|ì', r'i', word))
        elif re.search(r'õ|ô|ó|ò', word):
            words.append(re.sub(r'õ|ô|ó|ò', r'o', word))
        elif re.search(r'û|ú|ù', word):
            words.append(re.sub(r'û|ú|ù', r'u', word))
        elif re.search(r'ç', word):
            words.append(re.sub(r'ç', r'c', word))
        else:
            words.append(word)

    return words
        
def get_rhyming_words(word):
    rhyming_words = []

    html = subprocess.check_output(['curl', url_rhymit + word])
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', {"class": "row wordsBlock"})
    for block in blocks:
        syl   = int(block["n"][0])
        words = block.find_all('div', {"class": "w"})

        for word in words:
            rhyme_obj = { "word": word.text, "numSyllables": syl }
            rhyming_words.append(rhyme_obj)

    return rhyming_words

def get_similar_words(word):
    similar_words = []

    html = subprocess.check_output(['curl', url_lexico + word + '/'])
    soup = BeautifulSoup(html, 'html.parser')
    
    blocks = soup.find_all('div', {"id": "relacionadas"}) 
    
    if len(blocks) != 0:
        block = blocks[0].find_all('div', {"class": "words"}) 
    
        anchors = block[0].find_all('a') 
        for a in anchors:
            similar_obj = { "word": a.text }
            similar_words.append(similar_obj)

    return similar_words


def build_dict_pt(input_words):
    dict_pt = {}
    
    # No caso da língua portuguesa é necessário a remoção de caracteres especiais
    # visto que as palavras são usadas nos URLs.
    words = clean_words(input_words)

    for word in words:
        if not word in dict_pt:
            dict_pt[word] = { "rhymes": {}, "similar": [] }
            word_obj = dict_pt[word]
            
            # Obter palavras que rimam e colocá-las no dicionário.
            rhyming_words = get_rhyming_words(word)
            for rhyme in rhyming_words:
                num_syl = str(rhyme["numSyllables"])

                if not num_syl in word_obj["rhymes"]:
                    word_obj["rhymes"][num_syl] = []
                    
                word_obj["rhymes"][num_syl].append(rhyme["word"])
            
            # Obter palavras similares e colocá-las no dicionário.
            similar_words = get_similar_words(word)
            for similar in similar_words:
                word_obj["similar"].append(similar["word"])

    return dict_pt

