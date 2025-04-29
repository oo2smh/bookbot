def get_book_text(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        file_contents = f.read()
    return file_contents


def count_words(book_contents):
    num_words = len(book_contents.split())
    return num_words


def count_chars(book_contents):
    hash_map = {}
    # loop through each char and count
    for char in book_contents:
        char = char.lower()
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    return hash_map


def sort_dict(dict):
    list = []
    # add all of the entries
    for key in dict:
        if not key.isalpha():
            continue
        list.append({"char": key, "num": dict[key]})

    # sort the new_dict key
    list.sort(reverse=True, key=lambda item: item["num"])

    # list each entry
    for entry in list:
        print(f"{entry['char']}: {entry['num']}")
