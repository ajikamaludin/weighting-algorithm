import pprint


class WIdf():
    
    def __init__(self):
        self.total_tf = 0
        self.total_weight = 0
        self.document = []
        self.query = ''
        self.corpus = {}

    def transform(self, q, document):
        self.query = q
        self.document = document
        for index, item in enumerate(self.document):
            words = item.split(' ')
            tf = 0
            for word in words:
                if(self.query.lower() == word.lower()):
                    tf += 1
            self.total_tf += tf
            self.corpus[index] = {"tf" : tf}
        return self
    
    def weight(self):
        for key, value in self.corpus.items():
            weight = value['tf'] / self.total_tf
            self.corpus[key]['weight'] = weight
            self.total_weight += weight

    def get_weight(self):
        self.total_weight = 0
        self.weight()
        return self.corpus

    def weight_average(self): #bikinan sendiri
        self.total_weight = 0
        self.weight()
        return self.total_weight / len(self.document)


# document = [
#     'Shipment of gold damaged in a fire',
#     'Delivery of silver arrived in a silver truck',
#     'Shipment of gold arrived in a truck'
# ]

# q = 'truck'

# weight = WIdf().transform(q=q, document=document)

# print("Bobot rata-rata: " + str(weight.weight_average()))
# pprint.pprint(weight.get_weight())