
def pad_truncate_words(words, word_len, padding_char):
    return [word[:word_len].ljust(word_len, padding_char)
            for word in words]


def encode_str(s):
    return [[ord(char)] for char in s]


def preprocess_words(words, word_len=12, padding_char='^'):
    words = [w for w in words if w.isascii()]
    words = pad_truncate_words(words, word_len, padding_char)
    return words
