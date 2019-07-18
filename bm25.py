import pprint
import math

class BM25():

    k1 = 1.2
    b = 0.75

    def __init__(self):
        self.query = ''
        self.document = []
        self.corpus = {}
        self.lave = 0
        self.document_contains = 0
        self.total_weight = 0

    def transform(self, q, document):
        self.query = q
        self.document = document
        for index, item in enumerate(self.document):
            words = item.split(' ')
            tf = 0
            for word in words:
                if(self.query.lower() == word.lower()):
                    tf += 1
            self.corpus[index] = {"tf" : tf, "ldi" : len(words)}
            if(tf != 0):
                self.document_contains += 1

            self.lave += len(words)
        self.lave = self.lave / len(document)
        return self

    def K(self, ldi):
        return self.k1 * ((1 - self.b) + ( self.b * ( ldi / self.lave ) ))

    def idf(self):
        return math.log(len(self.document) / self.document_contains ,10)

    def weigth(self):
        for key, value in self.corpus.items():
            if(value['tf'] > 0):
                weight = self.idf() * ( ( ( self.k1 + 1 ) * value['tf'] ) / (self.K(value['ldi']) + value['tf']) )
            else:
                weight = 0
            self.corpus[key]["weight"] = weight
            self.total_weight += weight
        return self.corpus

    def weight_average(self): #bikinan sendiri
        self.total_weight = 0
        self.weigth()
        return ((self.total_weight) / len(self.document))