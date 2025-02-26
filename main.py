import argparse
import sys
from stats import get_num_text
from stats import get_each_char
from stats import sort_char_counts

def main():
    parser = argparse.ArgumentParser(description="Analyze a book and count characters and words.")
    parser.add_argument('file_path', type=str, help="Path to the book file")
    args = parser.parse_args()
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    file_path = sys.argv[1]
    words_count = get_num_text(file_path)
    chars_count = get_each_char(file_path)
    sorted = sort_char_counts(chars_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    print(sorted)
    print("============= END ===============")
    

if __name__ == "__main__":
    main()
