from gensim.models import KeyedVectors
import string

model = KeyedVectors.load('w2v_trained_diacritics.bin')
word = ['ἐγώ']
word = [w.lower().translate(str.maketrans('', '', string.punctuation)) for w in word]

print(model.most_similar(positive=word, topn=10))