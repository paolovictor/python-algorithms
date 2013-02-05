def rabin_karp_substring(str_a, str_b):
    '''
    Checks whether str_b is a subtring of str_a using the rabin karp algorithm
    '''
    len_a = len(str_a)
    len_b = len(str_b)

    if len_b > len_a:
        return False

    a_hash = __hash__(str_a[:len_b])
    b_hash = __hash__(str_b)

    i = 0
    while i <= len_a - len_b:
        if b_hash == a_hash:
            if  str_a[i:i + len_b] == str_b:
                return True  

        if i < len_a - len_b:
            a_hash += __hash_c__(str_a[i + len_b], i + len_b)
            a_hash -= __hash_c__(str_a[i], i)

        i += 1

    return False

def __hash_c__(c, i, prime = 13):
    return ord(c)

def __hash__(s):
    return sum([__hash_c__(c, i) for i, c in enumerate(s)])

if __name__ == '__main__':
    print rabin_karp_substring("bar", "bar")
    print rabin_karp_substring("foobar", "bar")
    print rabin_karp_substring("foobartoel", "bar")
    print rabin_karp_substring("foobra", "bar")