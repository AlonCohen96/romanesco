#Pre-processing script für Übung 4
#Geschrieben von Alon Cohen

from nltk import sent_tokenize

with open('poe.txt', 'r') as in_file, open('poe_new.txt', 'w', encoding='utf-8') as out_file:
    text = in_file.read()
    text = text.replace('\n', ' ')
    sen_list = sent_tokenize(text)
    for sen in sen_list:
        out_file.write(sen + '\n')