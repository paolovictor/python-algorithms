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

def partition(buf, l, r):
    # TODO: randomize!
    i = l
    for j in range(l + 1, r):
        if buf[j] < buf[l]:
            i += 1
            buf[i], buf[j] = buf[j], buf[i]
    buf[i], buf[l] = buf[l], buf[i]
   
    print l, r, i, buf 
    return i

def qsort(buf):
    _qsort_(buf, 0, len(buf))

def _qsort_(buf, l, r):
    if r > l:
        p = partition(buf, l, r)
        _qsort_(buf, l, p - 1)
        _qsort_(buf, p + 1, r)
