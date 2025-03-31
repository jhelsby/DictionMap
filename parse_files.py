from tqdm import tqdm

# Stores the words in words.txt and
# categories.txt, in lowercase.
words = set()
categories = set()

manual_tags_file = 'manual_tags.txt'

def parse_files():
  load_wordsets()
  filter_files()

def load_wordsets():
  load_wordfile(words, "./words.txt")
  load_wordfile(categories, "./categories.txt")
  load_manually_tagged_words()

def load_wordfile(wordset, filename):
  with open(filename, "r") as f:
    words = [word.lower() for word in f.read().split()]
    wordset.update(words)

def load_manually_tagged_words():
  extract_new_tags()

  with open(manual_tags_file, "r") as f:
    # Stop manually tagged words getting
    # added to for_manual_tagging.txt again.
    for line in f:
      word, _ = line.split(" ", 1)
      words.remove(word)

# Add any new manually tagged words in their own file.
def extract_new_tags():
  file_to_extract_from = "for_manual_tagging.txt"

  with open(file_to_extract_from, "r") as f:
    lines = f.readlines()

  untagged = []
  tagged = []

  # Any line with multiple words on it should be interpreted
  # as "word category1 category2 ... categoryN", i.e. tagged.
  for line in lines:
    if len(line.split()) > 1:
      tagged.append(line)
    else:
      untagged.append(line)

  # Keep the untagged words in their old file.
  with open(file_to_extract_from, "w") as f:
    f.writelines(untagged)

  # Permanently store the tagged words.
  with open(manual_tags_file, "a") as f:
    f.writelines(tagged)

def filter_files():
  filter_crawl()
  get_untagged()

def filter_crawl():
  with open('crawl-300d-2M.vec', 'r') as f_in, open('words.vec', 'w') as words_out, open('categories.vec', 'w') as categories_out:
    """
    Create a new word vector file for each of words and categories.
    """

    # Use tqdm to create a progress bar
    for line in tqdm(f_in, total=2000000, desc="Processing lines", unit="line"):
        # Word is first space separated element in line.
        lowercase_word = line.split()[0].lower()

        if (lowercase_word in words):
            words_out.write(line)

            # Don't add different capitalisations of a word twice
            words.remove(lowercase_word)

        if (lowercase_word in categories):
          categories_out.write(line)

          # Don't add different capitalisations of a word twice
          categories.remove(lowercase_word)

# Run after filter_crawl(), which removes
# all tagged words from word.
def get_untagged():
  # Catch any words that aren't in crawl-300d-2M.vec.
  # These will need to be tagged manually.
  with open('for_manual_tagging.txt', 'w') as file:
    for word in tqdm(words, total=len(words)):
      file.write(word + '\n')

  # Catch any categories that aren't in crawl-300d-2M.vec.
  # These are probably misspellings and should be
  # corrected.
  with open('category_errors.txt', 'w') as file:
    for word in tqdm(words, total=len(words)):
      file.write(word + ' ')

if __name__ == "__main__":
  parse_files()