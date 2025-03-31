import random, itertools

"""
The output of the dict category_to_prioritised_words in categoriser.py
is a structured collection of words linked to a given category:

([the most linked words], [the secondmost linked words], ... [the n-most linked]).

This utility shuffles the words while preserving their prioritisation:
each sublist is shuffled before flattening the tuple.
"""
def shuffle_and_combine_prioritised_words(prioritised_words):
  # Shuffle each sublist
  for sublist in prioritised_words:
    random.shuffle(sublist)
  print("TEST")
  print(prioritised_words)

  # Flatten the shuffled lists
  return list(itertools.chain(*prioritised_words))