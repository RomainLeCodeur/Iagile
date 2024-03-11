from readmepp import ReadMe
#from langdetect import detect

class Readability:
    
    def __init__(self, text):
        self.text = text
        self.predictor = ReadMe(lang='en')  #detect(self.text))
        self.tab=['A1','A2','B1','B2','C1','C2']

    def calcul(self):
        return self.tab[self.predictor.predict(self.text)]

    def toString(self):
        return "Le niveau de langue du texte est estimé à :" + self.calcul()