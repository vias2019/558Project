
class Translator:
# "quick brown fox jumps over lazy dog"
# "hello world"

    dictionary = {
        "quick": "rapido",
        "brown": "marron",
        "fox": "zorro",
        "jumped": "salto'",
        "jump": "salto",
        "over": "sobre",
        "lazy": "perezosa",
        "dog": "perro",
        "hello": "hola",
        "world": "mundo"
        }
    
    def searchDictionary(self, str):
        for key  in self.dictionary:
           if str == key:
               return (self.dictionary[key]) 


    
