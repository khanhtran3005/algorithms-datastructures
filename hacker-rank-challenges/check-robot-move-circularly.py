def doesCircleExist(commands):
    """
    check whether the robot move circularly or not with given command "RRLG" and
    R: turn right
    L: turn left
    G: move forward 1 step

    RRLL => YES
    RRRG => YES
    RLRG => NO
    """
    result = []
    N = 0
    E = 1
    S = 2
    W = 3

    for command in commands:
        x, y = (0, 0)
        direction = N
        command = command * 4

        for i in command:
            if i == "R":
                direction = (direction + 1) % 4
            elif i == "L":
                direction = (4 + direction - 1) % 4
            else:
                if direction == N:
                    y += 1
                elif direction == E:
                    x += 1
                elif direction == S:
                    y -= 1
                elif direction == W:
                    x -= 1

        if x == 0 and y == 0:
            result.append("YES")
        else:
            result.append("NO")

    return result


print(doesCircleExist(["R", "GGGR", "RRRRG"]))
