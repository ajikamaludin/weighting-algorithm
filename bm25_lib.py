from rank_bm25 import BM25Okapi

corpus = [
    'Shipment of gold damaged in a fire',
    'Delivery of silver arrived in a silver truck',
    'Shipment of gold arrived in a truck'
]

query = "gold truck"

tokenized_corpus = [doc.split(" ") for doc in corpus]
tokenized_query = query.split(" ")

bm25 = BM25Okapi(tokenized_corpus)

doc_scores = bm25.get_scores(tokenized_query)

print(doc_scores)