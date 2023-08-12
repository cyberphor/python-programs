import string

def get_wordlist(path: str, min_length: int, max_length: int):
    word_list = []
    with open(path, "r") as input_file:
        for word in given_file:
            wordlength = [len(c) for c in word.split()][0]
            if wordlength >= minlength and word_length < max_length:
                common_words.append(word.rstrip())
    return common_words

def contains_real_words(wordlist, sentence) -> bool:
    counter = 0
    sentence = version.split()
    for word in sentence:
        if counter >= 2:
            print(version)
        else:
            if word in common_words:
                counter += 1
    

def solution(data: any, min_length: int = 3, max_length: int = 6):
    versions = []
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation + " "
    common_words = get_common_words(path = "common_words.txt", min_length = 3, max_length = 6)
    for n in range(26):
        version = []
        for l in data:
            if l in punctuation or l in digits:
                version.append(l)
            else:
                if l.isupper():                    
                    shift = upper.index(l) - n
                    version.append(upper[shift])    
                else:
                    shift = lower.index(l) - n
                    version.append(lower[shift]) 
        versions.append("".join(version))
    for version in versions:
        contains_real_words(version)

challenge = 'Wylkpjapvu pz clyf kpmmpjbsa, lzwljphssf hivba aol mbabyl. - Uplsz Ivoy'
solution(challenge)
