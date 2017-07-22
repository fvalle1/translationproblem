import pandas as pd
from translate import TranslationManager as tr

in_file = open("KEYFILE","r")
key = in_file.read()
in_file.close()

#paste here your key
#get a key from https://cloud.google.com/translate/docs/getting-started
translator=tr(key)

first_translation=translator.translate_text('en','Finito')
print first_translation
second_translation=translator.translate_text('ja',first_translation)
print second_translation

languages=['it','fr','es','de','en','ru','am','co','cy','da']
words=['gatto','world']

translated=[]
previous=''

for word in words:
    previous=translator.translate_text('it',word)
    for lang in languages:
        previous=translator.translate_text(lang,previous)
        print previous, translator.translate_text(lang,word)
