import numpy as np
from collections import defaultdict

categories_per_word = 3

# Categorise all words.
def categoriser():
  words_list, words_vectors = load_embeddings_file('words.vec')
  categories_list, categories_vectors = load_embeddings_file('categories.vec')

  # Maps a category to all associated words, ordered in the tuple by priority.
  # categories["some_category"] = ([the most linked words], [the secondmost linked words],
  #                               ... [the n-most linked]).
  categories = defaultdict(lambda: tuple([] for _ in range(categories_per_word)))

  for np_word, vector in zip(words_list, words_vectors):

    word = str(np_word)

    similarities = cosine_similarities(vector, categories_vectors)
    most_similar_idx = np.argsort(similarities)[::-1]

    most_similar_categories = [[categories_list[i]] for i in most_similar_idx[:categories_per_word]]

    for i in range(len(most_similar_categories)):
      curr_category = str(most_similar_categories[i][0])
      categories[curr_category][i].append(word)

  return categories

# Function to compute cosine similarity between a vector and a list of word vectors.
def cosine_similarities(query_vector, vectors):
    dot_products = np.dot(vectors, query_vector)
    norms = np.linalg.norm(vectors, axis=1) * np.linalg.norm(query_vector)
    return dot_products / norms

def load_embeddings_file(filename):
    with open(filename, 'r') as f:
        f.readline()

        words = []
        nparray_vectors_list = []

        for line in f:
            word, *vector = line.rstrip().split(' ')
            words.append(word)
            nparray_vectors_list.append(np.asarray(vector, dtype='float32'))

    word_vectors = np.stack(nparray_vectors_list)
    word_list = np.array(words)

    return word_list, word_vectors


if __name__ == "__main__":
  categoriser()