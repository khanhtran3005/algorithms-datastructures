from classes.stack import Stack


def parChecker(string):
    s = Stack()
    index = 0

    while index < len(string):
        if string[index] == "(":
            s.push("(")
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
        index += 1

    return s.isEmpty()


# print(parChecker('((()))'))
# print(parChecker('(()'))
# print(parChecker('())'))


def balancedSymbolsChecker(string):
    s = Stack()
    index = 0

    while index < len(string):
        if string[index] in "[{(":
            s.push(string[index])
        else:
            if s.isEmpty():
                return False
            elif isMatched(s.peek(), string[index]):
                s.pop()
            else:
                return False
        index += 1

    return s.isEmpty()


def isMatched(open, close):
    opens = "[{("
    closes = "]})"
    return opens.index(open) == closes.index(close)


# print(balancedSymbolsChecker('{{([][])}()}'))
# print(balancedSymbolsChecker('[{()]'))


def isBalanced(s):
    parentheses = []
    index = 0

    while index < len(s):
        if s[index] in "[{(":
            parentheses.append(s[index])
        else:
            if len(s) == 0:
                return "NO"
            elif isMatched(parentheses[len(parentheses) - 1], s[index]):
                parentheses.pop()
            else:
                return "NO"
        index += 1

    return "YES" if len(parentheses) == 0 else "NO"


print(isBalanced("{{([][])}()}"))
print(isBalanced("[{()]"))
