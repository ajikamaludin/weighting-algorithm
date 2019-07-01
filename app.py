import pprint
from tfidf import TfIdf
from widf import WIdf
from tfrf import TFRF
from bm25 import BM25

document = [
    'Shipment of gold damaged in a fire',
    'Delivery of silver arrived in a silver truck',
    'Shipment of gold arrived in a truck'
]
# document = [
#     'Shipment of gold damaged in a fire Delivery of silver arrived in a silver truck Shipment of gold arrived in a truck truck truck truck'
# ]

q = 'gold'

dictOf = { i : document[i] for i in range(0, len(document) ) }

print('+----------------------------------+')
print('documents : ')
pprint.pprint(dictOf)
print('')
print('query :' + q)
print('+----------------------------------+')

print('')
print('Pembobotan TF-IDF')
tfidf = TfIdf().transform(q=q, document=document)
print("Bobot rata-rata: " + str(tfidf.weight_average()))
pprint.pprint(tfidf.get_weight())
print("+---------------------------------+")

print('')
print('Pembobotan W-IDF')
widf = WIdf().transform(q=q, document=document)
print("Bobot rata-rata: " + str(widf.weight_average()))
pprint.pprint(widf.get_weight())
print("+---------------------------------+")

print('')
print('Pembobotan TFRF')
tfrf = TFRF().transform(q=q,document=document)
print("Bobot rata-rata: " + str(tfrf.weight_average()))
pprint.pprint(tfrf.get_weight())
print("+---------------------------------+")

print('')
print('Pembobotan BM25')
bm25 = BM25().transform(q=q, document=document)
pprint.pprint(bm25.weigth())
print("+---------------------------------+")