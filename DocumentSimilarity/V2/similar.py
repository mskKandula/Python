from sklearn.feature_extraction.text import TfidfVectorizer
import math
# from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer(stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    # print(tfidf.shape)
    return ((tfidf * tfidf.T).A)[0,1] * 100

# text1= "Rama killed Ravana"
# text2= "rama killed ravana"

with open("../V1/file.txt", 'r') as f:
    data = f.read()

with open("../V1/file1.txt", 'r') as f:
    data1 = f.read()


print(cosine_sim('a little bird', 'little bird'))
print(cosine_sim('a little bird', 'a little bird chirps'))


print(cosine_sim('Rama killed Ravana', 'Ravana was killed by Rama'))

# 66
print(cosine_sim(data,data1)) 

# print(cosine_similarity(vectorizer.fit_transform([text1, text2]),dense_output=True))
