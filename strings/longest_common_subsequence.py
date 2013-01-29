'''
Copyright (C) 2011 by Paolo Victor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

# Longest common subsequence
# http://en.wikipedia.org/wiki/Longest_common_subsequence_problem

def longest_common_subsequence(str_a, str_b):
    # Creates a |str_a| + 1 x |str_b| + 1 matrix with zeroes
    m = [[0 for i in range(len(str_b) + 1)] for k in range(len(str_a) + 1)]

    for y in range(1, len(str_a) + 1):
        for x in range(1, len(str_b) + 1):
            # Is the same char? Then add one to the latest
            # maximum without the cars
            if str_a[y - 1] == str_b[x - 1]:
                m[y][x] = m[y - 1][x - 1] + 1
            # Else, the maximum is the maximum of choosing one char
            # from str_a and choosing one char of str_b
            else:
                m[y][x] = max(m[y - 1][x], m[y][x - 1])
   
    return m[len(str_a)][len(str_b)], reconstruct_lcs(m, str_a, str_b)

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

if __name__ == '__main__':
    print longest_common_subsequence('a brand new option in orange juice', 'abc')
    print longest_common_subsequence('GACT', 'GCTA')
