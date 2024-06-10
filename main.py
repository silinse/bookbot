def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_char_count = sort_characters(char_count)


    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char_dict in sorted_char_count:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_count = {}
    for c in text.lower():
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1
    return character_count

def sort_on(dict):
    return dict["count"]

def sort_characters(char_count):
    characters = []
    for char in char_count:
        if char.isalpha():
            char_dict = {"char": char, "count": char_count[char]}
            characters.append(char_dict)
    characters.sort(reverse=True, key=sort_on)
    return characters

main()