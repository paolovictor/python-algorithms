# Longest common subsequency
# http://en.wikipedia.org/wiki/Longest_common_subsequence_problem

def lcs(str_a, str_b):
    m = [[0 for i in range(len(str_b) + 1)] for k in range(len(str_a) + 1)]

    for y in range(1, len(str_a) + 1):
        for x in range(1, len(str_b) + 1):
            if str_a[y - 1] == str_b[x - 1]:
                m[y][x] = m[y - 1][x - 1] + 1
            else:
                m[y][x] = max(m[y - 1][x], m[y][x - 1])
   
    print reconstruct_lcs(m, str_a, str_b)
 
    return m[len(str_a)][len(str_b)]

# Actually, this one shows only ONE LCS! There may be multiple ones!
def reconstruct_lcs(m, str_a, str_b):
    y, x = len(str_a), len(str_b)
    s = ''

    if m[y][x] == 0:
        return s
    
    while x != 0 and y != 0:
        if str_a[y - 1] == str_b[x - 1]:
            s = str_a[y - 1] + s
            y -= 1
            x -= 1
        elif m[y - 1][x] > m[y][x - 1]:
            y -= 1
        else:
            x -= 1

    return s

print lcs('a brand new option in orange juice', 'abc')
print lcs('GACT', 'GCTA')
