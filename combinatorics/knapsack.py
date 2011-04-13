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

def unbounded_knapsack(W, v, w):
    '''
    Unbounded knapsack algorithm. The problem definition is:

    "Can a value of at least V be achieved without excedding
     a weight W?"

    On this case, there's no limit on the number of times
    you may use an item.

    This algorithm returns the maximum value that can be achieved
    by without exceeding a weight W.

    @param W the maximum weight
    @param v the object values
    @param w the object weights
    '''
    m = [0 for i in xrange(W + 1)]

    # TODO Try to divide all elements by the smallest element, to
    # decrease the space requirement
 
    start = min(w)
    for i in xrange(start, W + 1):
        m[i] = m[i-1]
        for k, vk in enumerate(v):
            if w[k] <= i and m[i] < m[i - w[k]] + vk:
                m[i] = m[i - w[k]] + vk

    return m[W]

def zero_one_knapsack(W, v, w):
    '''
    0-1 knapsack algorithm. The problem definition is:

    "Can a value of at least V be achieved without excedding
     a weight W?"

    On this case, you can only choose 0 or 1 items of the same type

    This algorithm returns the maximum value that can be achieved
    by without exceeding a weight W.

    @param W the maximum weight
    @param v the object values
    @param w the object weights
    '''
    m = [[0 for k in range(W + 1)] for i in range(len(w) + 1)]

    for i in range(len(v)):
        m[i][0] = 0

    for i in range(W + 1):
        m[0][i] = 0

    start = min(w)
    for item in range(1, len(v) + 1):
        for max_w in xrange(start, W + 1):
            w_i = w[item - 1]

            if w_i > max_w:
                m[item][max_w] = m[item - 1][max_w]
            else:
                m[item][max_w] = max(m[item - 1][max_w], m[item - 1][max_w - w_i] + w_i)

    return m[len(v)][W]
