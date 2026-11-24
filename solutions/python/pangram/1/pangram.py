def is_pangram(sentence):
    lowercasedSentence = sentence.lower()

    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in lowercasedSentence:
            return False
    return True
