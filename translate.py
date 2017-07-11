import requests #API

class TranslationManager(object):
    """docstring for TranslationManager."""
    def __init__(self):
        super(TranslationManager, self).__init__()
        self.key=''
    
    def __init__(self, key):
        super(TranslationManager,self).__init__()
        self.key=key
    
    def SetKey(key):
        self.key=key
    
    def translate_text(self, target, text):
        url='https://translation.googleapis.com/language/translate/v2'
        
        payload={'key':self.key, 'target':target, 'q':text}
        result=requests.get(url, params=payload)
        data=result.json()
        toReturn= data['data']['translations'][0]['translatedText']
        return toReturn
