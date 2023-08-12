from argparse import ArgumentParser
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def get_common_words(word_list_path: str, min_word_len: int = 3, max_word_len: int = 6) -> list:
    common_words = []
    with open(word_list_path, "r") as word_list:
        for word in word_list:
            word_length = [len(c) for c in word.split()][0]
            if word_length >= min_word_len and word_length < max_word_len:
                common_words.append(word.rstrip())
    return common_words

def contains_common_words(common_words: list, sentence: str) -> bool:
    counter = 0
    for word in sentence.split():
        if counter >= 2:
            return True
        else:
            if word in common_words:
                counter += 1

def solution(data: any):
    versions = []
    common_words = get_common_words(word_list_path = "common_words.txt")
    for n in range(len(ascii_lowercase)):
        version = []
        for c in data:
            if c in punctuation or c == " " or c in digits:
                version.append(c)
            else:
                if c.isupper():    
                    shift = ascii_uppercase.index(c) - n
                    version.append(ascii_uppercase[shift])
                else:
                    shift = ascii_lowercase.index(c) - n
                    version.append(ascii_lowercase[shift]) 
        versions.append("".join(version))
    for version in versions:
        if contains_common_words(common_words = common_words, sentence = version):
            print(version)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d")
    args = parser.parse_args()
    solution(args.d)