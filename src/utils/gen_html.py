from lxml import etree
import lxml.html

def write_html(path, file_name, file_class, xml_file):
    xslt_doc = etree.parse('./templates/' + file_class + '.xslt')
    xslt_transformer = etree.XSLT(xslt_doc)
    
    source_doc = etree.fromstring(xml_file)
    output_doc = xslt_transformer(source_doc)
    
    output_doc.write(path + file_name + '.html', pretty_print=True)

def gen_html(lang, dict_words):
    index_xml = '<index><meta><lang>{}</lang></meta><words>'.format(lang)

    for word in dict_words:
        index_xml += '<word>{}</word>'.format(word)
        sugestion_xml = '<sugestion><meta><word>{}</word></meta><rhymes>'.format(word)

        word_obj = dict_words[word]

        for syl in word_obj['rhymes']:
            sugestion_xml += '<syl n="{}">'.format(syl)

            for w in word_obj['rhymes'][syl]:
                sugestion_xml += '<rhyme>{}</rhyme>'.format(w)
            
            sugestion_xml += '</syl>'
        
        sugestion_xml += '</rhymes><similars>'

        for s in word_obj['similar']:
            sugestion_xml += '<similar>{}</similar>'.format(s)
        
        sugestion_xml += '</similars></sugestion>'

        write_html('./out/html/words/', word, 'sugestion', sugestion_xml)
    
    index_xml += '</words></index>'

    write_html('./out/html/', 'index', 'index', index_xml)
