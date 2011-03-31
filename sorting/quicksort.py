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
import random

def partition(buf, l, r):
    '''
    Traditional partition function with randomized pivot
    '''
    i = l

    # swaps pivot with element from random position to
    # decrease chances of the pivot being the last element
    tmp = random.randint(l, r - 1)
    buf[i], buf[tmp] = buf[tmp], buf[i]

    for j in range(l + 1, r + 1):
        if buf[j] < buf[l]:
            i += 1
            buf[i], buf[j] = buf[j], buf[i]
    buf[i], buf[l] = buf[l], buf[i]
   
    return i

def qsort(buf):
    '''
    Traditional quicksort
    '''
    _qsort_(buf, 0, len(buf) - 1)

def _qsort_(buf, l, r):
    if r > l:
        p = partition(buf, l, r)
        _qsort_(buf, l, p - 1)
        _qsort_(buf, p + 1, r)

def qsort_lc(buf):
    '''
    Quicksort using python's list comprehension. Actually, it's said it's
    faster than the traditional! (I've still got to test that)

    Note that this version does _not_ sort the list in place!

    http://en.literateprograms.org/Quicksort_(Python)
    '''
    if not buf:
        return []

    pivot = buf[0]
    left = [x for x in buf[1:] if x < pivot]
    right = [x for x in buf[1:] if x >= pivot]

    return qsort_lc(left) + [pivot] + qsort_lc(right)

def qsort_oneliner(buf):
    '''
    Quicksort in one line. A compact version of qsort_lc
    '''
    return [] if not buf else \
           qsort_oneliner([x for x in buf[1:] if x < buf[0]]) + \
           [buf[0]] + \
           qsort_oneliner([x for x in buf[1:] if x >= buf[0]])

