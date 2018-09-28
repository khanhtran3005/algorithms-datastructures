from classes.dequeue import Dequeue

def palChecker(string: str):
    d = Dequeue()

    for c in string:
        d.addRear(c)

    while d.size() > 1:
        if d.removeRear() != d.removeFront():
            return False

    return True

    # arrStr = list(string)

    # while len(arrStr) > 1:
    #     if arrStr.pop() != arrStr.pop(0):
    #         return False

    # return True

print(palChecker("lsdkjfskf"))
print(palChecker("radar"))

print('/'.join(['a', 'b']))