"""
Flask web application logic for DictionMap.
"""
from flask import Flask, render_template, request, redirect, url_for
import os, random, requests
from categoriser import categoriser, get_all_words

app = Flask(__name__)

word_to_categories, category_to_words = categoriser()

# Map a lowercase word to its stored, possibly capitalised equivalent.
lowercase_to_word = {word.lower(): word for word in word_to_categories.keys()}

@app.route('/', methods=['GET', 'POST'])
def index():
  categories = None
  word = None
  example_words = None

  if request.method == 'POST':
    word = request.form['word'].strip()
    lowercase_word = word.lower()

    num_words_to_output = int(request.form.get('num_words', 20))
    num_cats_to_output = int(request.form.get('num_cats', 5))

    if lowercase_word in lowercase_to_word:
        word = lowercase_to_word[lowercase_to_word]
        categories = word_to_categories[word]

        # Todo: get all words linked with each category in this list.
    else:
        categories = ["Word not found."]

  else:
    words = [word for word in word_to_categories.keys()]
    example_words = random.sample(list(words), min(len(words), 15))

  return render_template('index.html', example_words=example_words)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))