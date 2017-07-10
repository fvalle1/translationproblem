import requests #API


def translate_text(target, text):
    #update key
    key=''
    url='https://translation.googleapis.com/language/translate/v2'

    payload={'key':key, 'target':target, 'q':text}
    result=requests.get(url, params=payload)
    data=result.json()
    toReturn= data['data']['translations'][0]['translatedText']
    return toReturn
