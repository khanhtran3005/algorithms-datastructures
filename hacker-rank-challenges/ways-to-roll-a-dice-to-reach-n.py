def totalSolutions(n: int):
    """Caculate how many ways of rolling a six-sided dice to reach n

    Arguments:
        n {int} -- finishing point

    Returns:
        int -- total solutions

    n = 1 => 1 | n = 2 => 2 | n = 3 => 4
    n = 4 => 8 | n = 5 => 16 | n = 6 => 32
    n = 7 => 63 | n = 8 => 125 | n = 9 => 248

    [1, 2, 4, 8, 16, 32, 63, 125, 248]

    If n equals 7, n equals the sum of 6 figures before 6-th.and so on.
    Therefore, if n equals 1, n equals the sum of [0, 0 ,0 , 0, 0, 1]

    """

    memo = [0] * 6
    memo[5] = 1
    if n == 1:
        return 1

    for i in range(n):
        solutions = sum(memo)
        memo.pop(0)
        memo.append(solutions)

    return memo.pop()


print(totalSolutions(610))
