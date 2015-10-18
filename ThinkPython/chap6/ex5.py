def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        a = ack(m, n - 1)
        return ack(m - 1, a)

print ack(3, 4)
print ack(4, 4)

