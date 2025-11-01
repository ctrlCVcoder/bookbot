import sys
from stats import count_words, count_char, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main(path):
    print(get_book_text(path))    

#book_path = "books/frankenstein.txt"

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
book_path = sys.argv[1]

book_text = get_book_text(book_path)
#main(book_path)

word_count = count_char(book_text)
char_dict = sort_char_count(word_count)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print (f"Found {count_words(book_text)} total words")
print("--------- Character Count -------")
for item in char_dict:
    print(f"{item['char']}: {item['count']}")
#print (word_count)
#print (f"/n /n /n Sorted Character Count: /n")
#print (sort_char_count(word_count))
