def main():
    book_path="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = book_word_count(text)
    character_count = book_character_count(text)
    count_list = list(character_count.items())
    sorted_char_list = sorted(count_list, key=lambda item: item[1], reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char, count in sorted_char_list:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def book_word_count(text):
    words = text.split()
    return len(words)

def book_character_count(text):
    lowered_book = text.lower()
    char_count = {}
    for char in lowered_book:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count

if __name__ == "__main__":
    main()