def sort_string(phrase):
    words = phrase.split()
    return sorted(words, key=str.lower)


if __name__ == '__main__':
    print(sort_string("Bananana ORANGE apple"))
