def compareTriplets(a, b):
    result = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1
    return result


a = [5, 6, 7]
b = [3, 6, 10]

print(compareTriplets(a, b))