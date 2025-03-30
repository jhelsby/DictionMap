# DictionMap

Categorise words using fastText word embeddings.

1. Download `crawl-300d-2M.vec` from fastText [here](https://fasttext.cc/docs/en/english-vectors.html) and place it in root.

2. Create a `categories.txt` file in root and list the categories you want, space-separated. For example:
    ```
    Red Blue Green Yellow Orange Purple Pink Brown Black White
    ```
    Capitalisation is ignored.

3. Create a `words.txt` file in root and list the words you want to categorise, space-separated. For example:
    ```
    Apple Banana Orange Mango Pineapple Strawberry Blueberry Raspberry Blackberry Watermelon Cantaloupe Honeydew Grapes Kiwi Papaya Pear Peach Plum Cherry Pomegranate Fig Date Coconut Guava Lychee Passionfruit Dragonfruit Jackfruit Persimmon Mulberry Avocado
    ```
    Capitalisation is ignored.

4. After installing requirements, run:
    ```
    python main
    ```

    This will extract your words and categories from `crawl-300d-2M.vec`, and print the top 3 categories associated with each word to terminal. For our example, we are trying to categorise fruit into a collection of colours. The output looks like:

    ```
    Apple:        Brown green purple
    FIG:          green yellow blue
    coconut:      green pink yellow
    grapes:       red purple yellow
    banana:       yellow purple green
    cherry:       pink red purple
    BlackBerry:   pink purple white
    pineapple:    pink purple yellow
    avocado:      green purple yellow
    strawberry:   pink purple yellow
    peach:        pink yellow purple
    mango:        pink yellow purple
    watermelon:   pink yellow purple
    pear:         pink yellow purple
    plum:         purple pink red
    raspberry:    pink purple red
    Kiwi:         Brown green white
    blueberry:    purple pink blue
    pomegranate:  purple red pink
    Mulberry:     Brown pink purple
    papaya:       yellow pink green
    cantaloupe:   pink yellow purple
    guava:        pink yellow purple
    lychee:       pink purple yellow
    persimmon:    purple yellow red
    passionfruit: pink purple yellow
    honeydew:     yellow pink purple
    jackfruit:    yellow green purple
    dragonfruit:  pink purple green
    ```

    Note the capitalisation in our example for "Apple" and "BlackBerry". This is because DictionMap uses the most common capitalisation (and associated embedding) for each word.