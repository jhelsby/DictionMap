# DictionMap

Categorise words using fastText word embeddings.

### Run

1. Download `crawl-300d-2M.vec` from fastText [here](https://fasttext.cc/docs/en/english-vectors.html) and place it in root.

2. Create a `categories.txt` file in root and list the categories you want, space-separated. For example:
    ```
    Red Blue Green Yellow Purple Pink Brown Black White Magenta
    ```
    Capitalisation is ignored.

3. Create a `words.txt` file in root and list the words you want to categorise, space-separated. For example:
    ```
    Apple Banana Mango Pineapple Strawberry Blueberry Raspberry Blackberry Watermelon Cantaloupe Honeydew Grapes Kiwi Papaya Pear Peach Plum Cherry Pomegranate Fig Date Coconut Guava Lychee Passionfruit Dragonfruit Jackfruit Persimmon Mulberry Avocado
    ```
    Capitalisation is ignored.

4. After installing requirements, run:
    ```
    python parse_files.py
    ```

    This will extract your words and categories from `crawl-300d-2M.vec`, and assign words to each category. In our example, we are trying to categorise fruit into a collection of colours. The internal representation looks like:

    ```python
    # Category: ([most-linked items], [secondmost-linked items], [thirdmost-linked items]).
    {
        'Brown':   (['Apple', 'Kiwi', 'Mulberry'], [], []),
        'magenta': (['FIG', 'BlackBerry', 'raspberry', 'persimmon'],
                    ['Apple', 'plum', 'papaya', 'guava', 'passionfruit'],
                    ['mango', 'lychee', 'dragonfruit']
                ),
        'green':   (['coconut', 'avocado'],
                    ['FIG', 'Kiwi', 'jackfruit'],
                    ['Apple', 'banana']
                ),
        'yellow': (['banana', 'papaya', 'honeydew', 'jackfruit'],
                    ['peach', 'mango', 'watermelon', 'pear', 'cantaloupe'],
                    ['FIG', 'coconut', 'grapes', 'pineapple', 'avocado', 'strawberry', 'guava', 'persimmon']
                ),
        'purple': (['plum', 'blueberry', 'pomegranate'],
                   ['banana', 'grapes', 'pineapple', 'avocado', 'strawberry', 'lychee', 'persimmon', 'dragonfruit'],
                   ['cherry', 'BlackBerry', 'peach', 'watermelon', 'pear', 'raspberry', 'Mulberry', 'cantaloupe', 'passionfruit', 'honeydew', 'jackfruit']
                ),
        'pink': (['cherry', 'pineapple', 'strawberry', 'peach', 'mango', 'watermelon', 'pear', 'cantaloupe', 'guava', 'lychee', 'passionfruit', 'dragonfruit'],
                 ['coconut', 'BlackBerry', 'raspberry', 'blueberry', 'Mulberry', 'honeydew'],
                 ['plum', 'pomegranate', 'papaya']
                ),
        'red': (['grapes'], ['cherry', 'pomegranate'], []),
        'white': ([], [], ['Kiwi']),
        'blue': ([], [], ['blueberry'])
    }
    ```

    Note the capitalisation in our example for "Apple" and "BlackBerry". This is because DictionMap uses the most common capitalisation (and associated embedding) for each word.

5. Run
    ```
    python app.py
    ```

    This starts a Flask web app which allows you to interact with your categories.

### To-Do

* Let you browse categories.

* Manually add categories.

* Randomise which show a bit.