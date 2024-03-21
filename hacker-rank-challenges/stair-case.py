def staircase(n):
    for i in range(1, n + 1):
        print("{0:>{fill}}".format("#" * i, fill=n))
