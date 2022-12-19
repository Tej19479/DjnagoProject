def sum1(n):
    return n * (n + 1) // 2


def sum2(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + i
    return sm


t = int(input())
while t:
    n = int(input("Enter a number of "))
    print("tej", n)
    print("sum1 are execute{} ".format(sum1(n)))
    print("sum2 are execute{} ".format(sum2(n)))

    t = t - 1
