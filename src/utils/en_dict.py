import re
import subprocess
import json

datamuse_api = 'https://api.datamuse.com'

def clean_words(input_words):
    words = []
    
    for word in input_words:
        words.append(word.lower())

    return words

def get_rhyming_words(word):
    res = subprocess.check_output(['curl', datamuse_api + '/words?rel_rhy=' + word])
    str_res = res.decode('utf-8')
    words = json.loads(str_res)

    return words

def get_similar_words(word):
    res = subprocess.check_output(['curl', datamuse_api + '/words?ml=' + word])
    str_res = res.decode('utf-8')
    words = json.loads(str_res)

    return words


def build_dict_en(input_words):
    dict_en = {}

    words = clean_words(input_words)

    for word in words:
        if not word in dict_en:
            dict_en[word] = { "rhymes": {}, "similar": [] }
            word_obj = dict_en[word]
            
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
    
    return dict_en

