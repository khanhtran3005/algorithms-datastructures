def plusMinus(arr):
    positive = negative = zero = 0
    length = len(arr)
    for i in range(length):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1

print("{:.6f}".format(positive/length))
print("{:.6f}".format(negative/length))
print("{:.6f}".format(zero/length))