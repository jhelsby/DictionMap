"""
Flask web application logic for DictionMap.
"""
from flask import Flask, render_template, request, redirect, url_for
import os, random, requests, itertools
from categoriser import categoriser, get_all_words

app = Flask(__name__)

word_to_categories, category_to_prioritised_words = categoriser()

# Map a lowercase word to its stored, possibly capitalised equivalent.
lowercase_to_word = {word.lower(): word for word in word_to_categories.keys()}

@app.route('/', methods=['GET', 'POST'])
def index():
  global word_to_categories

  if request.method == 'POST':
    word = request.form['word'].strip()
    lowercase_word = word.lower()

    num_words_to_output = int(request.form.get('num_words', 20))
    num_cats_to_output = int(request.form.get('num_cats', 3))

    word_to_categories, category_to_prioritised_words = categoriser(num_cats_to_output)

    if lowercase_word in lowercase_to_word:
      word = lowercase_to_word[lowercase_word]
      categories = word_to_categories[word]

      selected_categories = [(category, category_to_prioritised_words[category]) for category in categories]
      categories_and_words = []

      for category, lists in selected_categories:
         # Shuffle each sublist
        for sublist in lists:
          random.shuffle(sublist)

        # Flatten the shuffled lists
        combined_words = list(itertools.chain(*lists))
        categories_and_words.append((category, combined_words[:num_words_to_output]))

    else:
      categories_and_words = None

    return render_template('index.html', categories_and_words=categories_and_words, num_words=num_words_to_output, num_cats=num_cats_to_output, last_word=word)

  words = [word for word in word_to_categories.keys()]
  example_words = random.sample(list(words), min(len(words), 15))

  return render_template('index.html', example_words=example_words)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))