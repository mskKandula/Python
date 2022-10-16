import spacy
nlp = spacy.load('en_core_web_sm')

with open("../V1/file.txt", 'r') as f:
    data = f.read()

with open("../V1/file1.txt", 'r') as f:
    data1 = f.read()

doc1 = nlp(data)
doc2 = nlp(data1)

# 95
print(doc1.similarity(doc2))