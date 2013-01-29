import random

def random_7_from_random_5():
    outcome = 0

    n = 0
    while n < 3:
        r = random.randint(0, 5)

        if r >= 3:
            outcome |= (1 << n)
            n += 1
        elif r < 3:
            n += 1

    return outcome

if __name__ == '__main__':
    from collections import defaultdict

    res = defaultdict(int)
    for i in xrange(0, 100000):
        n = random_7_from_random_5()

        res[n] = res[n] + 1

    for k, v in res.iteritems():
        print k, v / 100000.0
