def main():
    book_path = "books/frankenstein.txt"

    # Calls the function get_book_text and passes the book_path variable as a paramitor.
    text = get_book_text(book_path)

    # Calls the function get_number_of_words and passes the text variable as a paramitor.
    num_words = get_number_of_words(text)

    # Calls the function elemts_in_list and passes the text variable as a paramitor.
    eil = elements_in_list(text)

    # Prints the entire text to the console.
    # print(text)

    # Prints the total number of words in the book.
    # print(f"Number of words: {num_words}")

    # Prints the Elemets in the list.
    # print(eil)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the text document\n")
    print_a_report(eil, text)
    print("-- End report --")


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


def sort_on(dict):
    return dict["num"]


def print_a_report(eil, text):
    new_eil = []

    for letter, count in eil.items():
        eil = {"char": letter, "num": count}
        if letter.isalpha():
            new_eil.append(eil)

    new_eil.sort(reverse=True, key=sort_on)

    for item in new_eil:
        letter = item["char"]
        count = item["num"]
        print(f"The '{letter}' characters was found {count} times")


main()
