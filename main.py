from translate import translate_text


first_translation=translate_text('en','Finito')
print first_translation
second_translation=translate_text('ja',first_translation)
print second_translation
