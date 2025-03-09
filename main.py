import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]




def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    from stats import count_words, symbol_count, sort_character_count
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    character_count = symbol_count(book_text)
    sorted_chars = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        
        if char.isalpha():
            print(f"{char}: {count}")


    print("============= END ===============")



if __name__ == "__main__":
    main()
