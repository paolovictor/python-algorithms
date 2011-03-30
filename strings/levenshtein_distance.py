# http://en.wikipedia.org/wiki/Levenshtein_distance

def med(str_a, str_b):
    m = [[0 for i in range(len(str_b) + 1)] for k in range(len(str_a) + 1)]

    for y in range(1, len(str_a) + 1):
        m[y][0] = y

    for x in range(1, len(str_b) + 1):
        m[0][x] = x

    for y in range(1, len(str_a) + 1):
        for x in range(1, len(str_b) + 1):
            if str_a[y - 1] == str_b[x - 1]:
                m[y][x] = m[y - 1][x - 1]
            else:
                m[y][x] = min(m[y - 1][x - 1], m[y - 1][x], m[y][x - 1]) + 1

    return m[len(str_a)][len(str_b)]

print med('a brand new option in orange juice', 'abc')
print med('abc', 'a brand new option in orange juice')
print med('GACT', 'GCTA')
print med('ABC', 'A')
print med('sitting', 'kitten')
print med('sunday', 'saturday')
