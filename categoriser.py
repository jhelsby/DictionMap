import numpy as np
from collections import defaultdict

categories_per_word = 3

# Categorise all words.
def categoriser():
  words_list, words_vectors           = load_embeddings_file('words.vec')
  categories_list, categories_vectors = load_embeddings_file('categories.vec')

  # Maps each word to its associated categories,
  # in descending order of link.
  word_to_categories = dict()

  # Maps a category to all associated words, ordered in the tuple by priority.
  # categories["some_category"] = ([the most linked words], [the secondmost linked words],
  #                               ... [the n-most linked]).
  category_to_words = defaultdict(lambda: tuple([] for _ in range(categories_per_word)))

  for word, vector in zip(words_list, words_vectors):

    similarities = cosine_similarities(vector, categories_vectors)
    most_similar_idx = np.argsort(similarities)[::-1]

    most_similar_categories = [[categories_list[i]] for i in most_similar_idx[:categories_per_word]]

    word_to_categories[word] = most_similar_categories

    for i in range(len(most_similar_categories)):
      curr_category = str(most_similar_categories[i][0])
      category_to_words[curr_category][i].append(word)

  return word_to_categories, category_to_words

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

  return words, word_vectors

def get_all_words():
  with open('words.vec', 'r') as f:
    f.readline()

    words = []

    for line in f:
        word, *_ = line.rstrip().split(' ')
        words.append(word)

  return words

if __name__ == "__main__":
  categoriser()