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

def longest_common_substring(str_a, str_b):
    m = [[0 for i in range(len(str_b) + 1)] for k in range(len(str_a) + 1)]
    
    lcs = None
    max_len = 0
    for y in range(1, len(str_a) + 1):
        for x in range(1, len(str_b) + 1):
            m[y][x] = m[y - 1][x - 1] + 1 if (str_a[y - 1] == str_b[x - 1]) else 0

            if m[y][x] > max_len:
                max_len = m[y][x]
                lcs = str_a[(y - max_len):y]

    return max_len, lcs   

if __name__ == '__main__':
    print longest_common_substring('a brand new option in orange juice', 'brand newb opx ju')
    print longest_common_substring('GACT', 'GCTA')
