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

def mergesort(buf):
    if len(buf) <= 1:
        return buf

    m = len(buf) / 2
    return merge(mergesort(buf[:m]), mergesort(buf[m:]))

def merge(left, right):
    ret = []
    l_i, r_i = 0, 0

    if not left: return right
    if not right: return left

    while l_i + r_i < len(left) + len(right):
        if l_i < len(left) and (r_i >= len(right) or left[l_i] < right[r_i]):
            ret.append(left[l_i])
            l_i += 1
        else:
            ret.append(right[r_i])
            r_i += 1

    return ret
