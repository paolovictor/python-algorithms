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

class Heap(object):

    NONE = -1
    
    def __init__(self, data):
        self.data = data
        for i in xrange(len(data)/2, -1, -1):
            self.__max_heapify__(i)

    def parent(self, i):
        return i >> 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2 # +2 instead of +1 because it's 0-indexed
 
    def __max_heapify__(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        n = len(self.data)
    
        largest = (left < n and self.data[left] > self.data[i]) and left or i
        largest = (right < n and self.data[right] > self.data[largest]) and right or largest

        if i != largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
        
            self.__max_heapify__(largest)

