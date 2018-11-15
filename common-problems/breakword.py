DICTIONARY = [
    "i","like","python","php"
]


def contains(string):
    print('contain:', string)
    for word in DICTIONARY:
        if word == string:
            return True

    return False

def wordbreak(string):
    length = len(string)
    string = string.lower()

    if length == 0: return True

    print('wordbreak:', length, string)
    for i in range(1, length+1):
        if contains(string[:i]) and wordbreak(string[i:]):
            print('in:', string)
            return True

    print('out:', string)
    return False


print(wordbreak("likePython"))

# print all possible results: 
#   https://www.tutorialspoint.com/Word-Break-Problem
#   http://www.zrzahid.com/word-break-problem/