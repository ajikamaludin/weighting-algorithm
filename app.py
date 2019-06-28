import pprint
from tfidf import TfIdf
from widf import WIdf
from tfrf import TFRF

document = [
    'Shipment of gold damaged in a fire',
    'Delivery of silver arrived in a silver truck',
    'Shipment of gold arrived in a truck'
]
# document = [
#     'Shipment of gold damaged in a fire Delivery of silver arrived in a silver truck Shipment of gold arrived in a truck truck truck truck'
# ]

q = 'gold'

print('Pembobotan TF-IDF')
tfidf = TfIdf().transform(q=q, document=document)
print('TF : ' + str(tfidf.tf))
print('Bobot ' + q + ' : ' + str(tfidf.get_weight()))
print("+---------------------------------+")

print('Pembobotan W-IDF : ' + q)
widf = WIdf().transform(q=q, document=document)
print("Bobot rata-rata: " + str(widf.weight_average()))
pprint.pprint(widf.get_weight())
print("+---------------------------------+")

print('Pembobotan TFRF : ' + q)
tfrf = TFRF().transform(q=q,document=document)
pprint.pprint(tfrf.get_weight())
print(tfrf.weight_average())
print("+---------------------------------+")