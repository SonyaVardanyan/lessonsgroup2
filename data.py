#!/usr/bin/python3
biography_excerpt = """
Napoleon Bonaparte was a French military and political leader who rose to prominence during the French Revolution.
He became Emperor of the French in 1804 and led a series of successful campaigns known as the Napoleonic Wars.
His military strategies and political reforms had a significant impact on European history.
"""

def count_symbols(text):
    symbol_count = {}
    for el in text:
        if el.isalnum():
            if el in symbol_count:
                symbol_count[el] += 1
            else:
                symbol_count[el] = 1
    return symbol_count

def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

def count_sentences(text):
    sentences = text.split(".")
    return len(sentences)

def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

def main():
    with open("data.txt", "r") as file:
        excerpt = file.read()

    symbol_count = count_symbols(excerpt)
    longest_word = find_longest_word(excerpt)
    sentence_count = count_sentences(excerpt)
    reversed_words = reverse_words(excerpt)

    print("Symbol Counts:")
    for el, count in symbol_count.items():
        print(f"{el}: {count}")

    with open("result.txt", "w") as result_file:
        result_file.write("Symbol Counts:\n")
        for el, count in symbol_count.items():
            result_file.write(f"{el}: {count}\n")

        result_file.write(f"\nLongest Word: {longest_word}\n")
        result_file.write(f"Sentence Count: {sentence_count}\n")
        result_file.write(f"Reversed Words: {reversed_words}\n")

    print("Results written to result.txt")

if __name__ == "__main__":
    main()