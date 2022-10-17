
class Translator:
    
    def __init__(self):
        self.a = 1
        
# "quick brown fox jumps over lazy dog"
# "hello world"

    dictionary = {
        "quick": "rapido",
        "brown": "marron",
        "fox": "zorro",
        "jumped": "saltó",
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


# if __name__ == "__main__":
#     a = Translator()
#     print(a.searchDictionary("hello"))
