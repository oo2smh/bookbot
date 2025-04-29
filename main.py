from stats import get_book_text, count_words, count_chars, sort_dict


def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_content = get_book_text(sys.argv[1])
    word_count = count_words(book_content)
    char_count = count_chars(book_content)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_dict = sort_dict(char_count)
    print("============= END ===============")


main()
