import sys

from tensorflow.keras.models import load_model

from src.extract import *
from src.preprocess import *


class PasswordDetector:
    def __init__(self, model_path, word_len=12, padding_char='^'):
        self.model = load_model(model_path)
        self.word_len = word_len
        self.padding_char = padding_char

    def detect_passwords(self, strings):
        prep_strings = preprocess_words(strings, word_len=self.word_len, padding_char=self.padding_char)
        X_test = [encode_str(w) for w in prep_strings]
        y_pred = self.model.predict(X_test) > 0.5
        return y_pred[:, 0]
