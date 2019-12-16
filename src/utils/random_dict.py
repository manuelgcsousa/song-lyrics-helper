import random

def build_dict_random(dict_words):
    dict_random = {}

    for key in dict_words:
        word_obj = dict_words[key]

        key_obj = { "rhymes": [], "similar": [] }
        dict_random[key] = key_obj
        
        # Selecionar rimas.
        choice_elems = []
        for syl in word_obj['rhymes']:
            rhymes = word_obj['rhymes'][syl]

            if len(rhymes) < 2:
                choice_elems += rhymes
            else:
                choice_elems += random.sample(rhymes, 2)
        
        key_obj['rhymes'] += choice_elems
        
        # Selecionar palavras similares.
        if len(word_obj['similar']) < 10:
            key_obj['similar'] += word_obj['similar']
        else:
            key_obj['similar'] += random.sample(word_obj['similar'], 10)

    print(dict_random)
    return dict_random

