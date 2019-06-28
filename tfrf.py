import math
import pprint

class TFRF():
    
    def __init__(self):
        self.total_weight = 0
        self.document = []
        self.query = ''
        self.corpus = {}
        self.document_contains = 0
        self.document_not_contains = 0

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
        self.document_not_contains = len(self.document) - self.document_contains
        return self

    def tf(self, val):
        return 1 + math.log(val, 10)
    
    def rf(self):
        return math.log(2 + (self.document_contains / max(1, self.document_not_contains)), 10)

    def weight(self):
        for key, value in self.corpus.items():
            if(value['tf'] > 0):
                weight = self.tf(val=value['tf']) * self.rf()
            else:
                weight = 0
            self.corpus[key]['weight'] = weight
            self.total_weight += weight
        # return self
    
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

# q = 'gold'

# weight = TFRF().transform(q=q,document=document)

# pprint.pprint(weight.corpus)
# pprint.pprint(weight.get_weight())
# print(weight.weight_average())