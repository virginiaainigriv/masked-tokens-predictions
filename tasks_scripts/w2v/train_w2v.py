from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import unicodedata
import numpy as np
import string
import gensim

def remove_diacritics(text):
    """Remove diacritics (accent marks) from the given text."""
    return ''.join(c for c in unicodedata.normalize('NFD', text) if not unicodedata.combining(c))

def process_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    sentences = [line.strip().split() for line in lines]
    return sentences

# Process the text file and remove diacritics from the words
sentences = process_text_file('/content/all_diorisis.txt')
sentences = [[remove_diacritics(word) for word in sentence] for sentence in sentences]

training_data = sentences
epochs = 10

model = Word2Vec(
  sentences=training_data,
  min_count=5,
  vector_size=100,
  workers=3,
  window=5,
  epochs=100,
  sg=1)

model.build_vocab(training_data)

model.train(training_data, total_examples=model.corpus_count, epochs=model.epochs)

model.wv.save('w2v_v1.bin')
