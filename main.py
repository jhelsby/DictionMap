from parse_files import parse_files
from categoriser import categoriser

def main():
  parse_files()
  print(categoriser())

if __name__ == "__main__":
  main()