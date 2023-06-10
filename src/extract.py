import re
import glob


def get_words_from_files(dir_name):
    words = set()
    for path in glob.glob(dir_name):
        content = open(path, 'rb').read().decode()
        file_words = [w for _, w in re.findall(r'([\'"])(.*?(?<!\\))(?:\\\\)*\1', content)]
        words = words.union(file_words)
    return words
