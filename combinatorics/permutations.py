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

def k_permutation_generator(l, k, start = 0, n = 0, used = None):
    '''
    Returns a generator for all the k-permutations of the elements from the list l

    Example: k_permutation_generator([1, 2, 3], 2) yields:

     [[1, 2], [1, 3], [2, 1], [2, 3], [3, 2], [3, 1]]
    '''
    if not used : used = [] # Python gotcha!

    if n == k:
        yield used
        return

    for i in xrange(start, len(l)):
        l[start], l[i] = l[i], l[start]
       
        used.append(l[start])
 
        for perm in k_permutation_generator(l, k, start + 1, n + 1, used):
            yield perm

        used.remove(l[start])

        l[start], l[i] = l[i], l[start]

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

def __jt_move__(x, a, p, d):
    w = a[p[x] + d[x]]
    a[p[x] + d[x]] = x
    a[p[x]] = w
    p[w] = p[x]
    p[x] = p[x] + d[x]

def __jt_nest__(a, d, p, k):
    if k < len(a):
        for i in xrange(0, k + 1):
            for r in __jt_nest__(a, d, p, k + 1):
                yield r

            if i < k:
                __jt_move__(k, a, p, d)
                yield a[:]

        d[k] = -d[k] 

def permutations_jt(n):
    '''
    Generates all the permutations of l using the johnson trotter algorithm
    (recursive version)
    '''
    p = range(n)
    a = range(n)
    d = [-1 for i in p]

    yield range(n)

    for result in __jt_nest__(a, d, p, 1):
        yield result
