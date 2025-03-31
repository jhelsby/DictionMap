"""
Flask web application logic for DictionMap.
"""
from flask import Flask, render_template, request, redirect, url_for
import os, random, requests, itertools
from categoriser import categoriser, get_all_words
from utilities import shuffle_and_combine_prioritised_words

app = Flask(__name__)

word_to_categories, category_to_prioritised_words = categoriser()

all_words = [word for word in word_to_categories.keys()]
all_cats  = [word for word in category_to_prioritised_words.keys()]

# Map a lowercase word to its stored, possibly capitalised equivalent.
lowercase_to_word = {word.lower(): word for word in all_words}
lowercase_to_category = {category.lower(): category for category in all_cats}

@app.route('/', methods=['GET', 'POST'])
def index():
  global word_to_categories, category_to_prioritised_words

  categories_and_words = None

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
        combined_words = shuffle_and_combine_prioritised_words(lists)
        truncated_words = combined_words[:num_words_to_output]

        categories_and_words.append((category, truncated_words))

    elif lowercase_word in lowercase_to_category:
      word = lowercase_to_category[lowercase_word]
      return redirect(url_for('category', word=word))
    else:
      categories_and_words = None

    return render_template('index.html', categories_and_words=categories_and_words, num_words=num_words_to_output, num_cats=num_cats_to_output, last_word=word)

  categories = [category for category in all_cats]
  words      = [word for word in all_words]

  example_categories = random.sample(list(categories), min(len(categories), 5))
  example_words      = random.sample(list(words), min(len(words), 15))

  return render_template('index.html', example_categories=example_categories, example_words=example_words)

@app.route('/category/<string:word>', methods=['GET', 'POST'])
def category(word):
    prioritised_words = category_to_prioritised_words[word]
    words = shuffle_and_combine_prioritised_words(prioritised_words)
    return render_template('category.html', category=word, words=words)

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    return render_template('categories.html', categories=random.sample(all_cats, len(all_cats)))

@app.route('/words', methods=['GET', 'POST'])
def words():
    return render_template('words.html', words=random.sample(all_words, int(request.form.get('num_words', 100))))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))