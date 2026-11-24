def is_pangram(sentence):
    lowercased_sentence = sentence.lower()

    return all(char in lowercased_sentence for char in 'abcdefghijklmnopqrstuvwxyz')