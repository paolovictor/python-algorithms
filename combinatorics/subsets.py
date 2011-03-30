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

def k_sized_subsets_n(k, n):
    '''
    Returns a generator of the subsets (combinations) of the {0, 1, ... , n} subset
    with k elements

    Examples:
  
        input: k = 3, n = 4

        output: Generator that yields
        [1, 2, 3]
        [0, 2, 3]
        [0, 1, 3]
        [0, 1, 2]
       
    It uses the binomial recursive formula:

        combinations(n, k) = combinations(n - 1, k - 1) + combinations(n - 1, k)
    '''
    if n == k:
        yield range(n) # Base case: when k == n, only one combination is possible
    elif k == 0 or n < k:
        yield []
    else:
        # yield all k - 1 sized subsets WITH n and
        # all k sized subsets WITHOUT n
        for s in k_sized_subsets_n(k - 1, n - 1):
            s.append(n - 1)
            yield s

        for s in k_sized_subsets_n(k, n - 1):
            yield s

def all_subsets(n):
    '''
    Returns a generator that yields all the subsets of the subset {0, 1, ... , n-1}

    Note: even though t
    '''
    num_subsets = 2 ** n
    current_subset = 0

    while current_subset < num_subsets:
        subset = []
        i = current_subset
        k = 0

        while i != 0:
            if i & (1 << k):
                subset.append(k)
                i ^= (1 << k)
            k += 1

        yield subset

        current_subset += 1
