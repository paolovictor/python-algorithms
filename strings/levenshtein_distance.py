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

# http://en.wikipedia.org/wiki/Levenshtein_distance

def levenshtein_distance(str_a, str_b):
    m = [[0 for i in range(len(str_b) + 1)] for k in range(len(str_a) + 1)]

    # The first row and collum represent going from an empty string
    # to the target string, only i additions are needed
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

if __name__ == '__main__':
    print levenshtein_distance('a brand new option in orange juice', 'abc')
    print levenshtein_distance('abc', 'a brand new option in orange juice')
    print levenshtein_distance('GACT', 'GCTA')
    print levenshtein_distance('ABC', 'A')
    print levenshtein_distance('sitting', 'kitten')
    print levenshtein_distance('sunday', 'saturday')
