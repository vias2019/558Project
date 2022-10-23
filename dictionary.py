
class Translator:

# "quick brown fox jump over lazy dog"
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
        else: return ("N/A")
     


#if __name__ == "__main__":
#    a = Translator()
#    print(a.searchDictionary("hello"))
