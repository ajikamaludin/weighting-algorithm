import math

class TfIdf():

    def __init__(self):
        self.tf = 0
        self.document = []
        self.query = {}
        self.document_contains = 0

    def transform(self, q, document):
        self.query = q
        self.document = document
        for item in self.document:
            words = item.split(' ')
            last_counter = self.tf
            for word in words:
                if(self.query.lower() == word.lower()):
                    self.tf += 1
            if(last_counter < self.tf):
                self.document_contains += 1 
        return self
    
    def idf(self):
        return math.log( len(self.document)/self.document_contains, 10)

    def get_weight(self):
        return self.tf * (self.idf() + 1)


# document = [
#     'Shipment of gold damaged in a fire',
#     'Delivery of silver arrived in a silver truck',
#     'Shipment of gold arrived in a truck'
# ]

# q = 'truck'

# weight = TfIdf().transform(q=q, document=document)

# print(weight.idf())
# print(weight.get_weight())