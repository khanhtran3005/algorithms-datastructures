def hanoiTower(disks, a, b, c):
    if disks == 1:
        moveDisk(a, c)
    else:
        hanoiTower(disks - 1, a, c, b)
        hanoiTower(1, a, b, c)
        hanoiTower(disks - 1, b, a, c)


def moveTower(disks, a, b, c):
    if disks >= 1:
        moveTower(disks - 1, a, c, b)
        moveDisk(a, c)
        moveTower(disks - 1, b, a, c)


def moveDisk(f, t):
    print("Move {} to {}".format(f, t))


moveTower(3, "A", "B", "C")
