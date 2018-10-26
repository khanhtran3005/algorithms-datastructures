def winningLotteryTicket(tickets):
    count = 0
    table = [0]*1024

    for ticket in tickets:
        mask = bitmasking(ticket)
        table[mask] += 1

    for i in range(1023):
        for j in range(i + 1, 1024):
            if i | j == 1023:
                count += table[i] * table[j]

    count += table[1023] * (table[1023] - 1) / 2
    return int(count)

def bitmasking(string):
    result = 0
    for i in string:
        result |= 1 << int(i)
    return result

print(winningLotteryTicket(['129300455', '5559948277', '012334556', '56789', '0123456879']))
print(winningLotteryTicket(['01234', '56789', '456789', '0123456879']))