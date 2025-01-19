def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    eil = elements_in_list(text)
    # print(text)
    # print(f"Number of words: {num_words}")
    print(eil)


def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def elements_in_list(text):
    lower_text = text.lower()
    element_dict = {}
    for i in set(lower_text):
        element_dict[i] = lower_text.count(i)
    return element_dict


main()
