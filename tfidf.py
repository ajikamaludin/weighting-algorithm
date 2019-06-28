import math

class TfIdf():

    def __init__(self):
        self.document = []
        self.query = {}
        self.document_contains = 0
        self.corpus = {}
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
            self.corpus[index] = {"tf" : tf}
            if(0 < tf):
                self.document_contains += 1
        return self
    
    def idf(self):
        if self.document_contains >= 0:
            return math.log( len(self.document)/self.document_contains, 10)
        else:
            return 0

    def weight(self):
        for key, value in self.corpus.items():
            if(value['tf'] > 0):
                weight = value['tf'] * (self.idf() + 1)
            else:
                weight = 0
            self.corpus[key]['weight'] = weight
            self.total_weight += weight
    
    def get_weight(self):
        self.total_weight = 0
        self.weight()
        return self.corpus

    def weight_average(self): #bikinan sendiri
        self.total_weight = 0
        self.weight()
        return ((self.total_weight) / len(self.document))

# document = [
#     'Shipment of gold damaged in a fire',
#     'Delivery of silver arrived in a silver truck',
#     'Shipment of gold arrived in a truck'
# ]

# q = 'truck'

# weight = TfIdf().transform(q=q, document=document)

# print(weight.idf())
# print(weight.get_weight())