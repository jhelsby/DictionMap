from tqdm import tqdm

# Stores the words in words.txt and
# categories.txt, in lowercase.
words = set()
categories = set()

def parse_files():
  load_wordsets()
  filter_files()

def load_wordsets():
  load_wordfile(words, "./words.txt")
  load_wordfile(categories, "./categories.txt")

def load_wordfile(wordset, filename):
  with open(filename, "r") as file:
    words = [word.lower() for word in file.read().split()]
    wordset.update(words)

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
  with open('untagged.txt', 'w') as file:
    for word in tqdm(words, total=len(words)):
      file.write(word + ' ')

  # Catch any categories that aren't in the crawl.
  # These will need to be manually assigned words.
  with open('category_errors.txt', 'w') as file:
    for word in tqdm(words, total=len(words)):
      file.write(word + ' ')

if __name__ == "__main__":
  parse_files()