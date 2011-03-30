'''
Copyright (C) 2011 by Paolo Victor, paolovictor@gmail.com

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

def permutation_generator(l, start = 0):
    '''
    Returns a generator that yields all the permutations of the elements from the list l

    Example:
        input: [1, 2, 3]

        generated output:
            [1, 2, 3]
            [1, 3, 2]
            [2, 1, 3]
            [2, 3, 1]
            [3, 2, 1]
            [3, 1, 2]
    '''
    if start == len(l): yield l

    for i in xrange(start, len(l)):
        l[start], l[i] = l[i], l[start]
    
        for p in permutation_generator(l, start + 1):
            yield p

        l[start], l[i] = l[i], l[start]

    
def permutation_list(l):
    '''
    Returns a list with all the permutations of the elements from the list l

    Example:
        input: [1, 2, 3]

        generated output:
            [1, 2, 3]
            [1, 3, 2]
            [2, 1, 3]
            [2, 3, 1]
            [3, 2, 1]
            [3, 1, 2]
    '''
    res = []
    __permutations__(l, res)
    return res

def __permutations__(l, res, start = 0):
    if start >= len(l):
        res.append(l[:])
        return

    for i in xrange(start, len(l)):
        l[start], l[i] = l[i], l[start]
    
        __permutations__(l, res, start + 1)

        l[start], l[i] = l[i], l[start]
