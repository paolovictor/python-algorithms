import sys

def check_parenthesis(source_file):
    line = source_file.readline()
    n = 1
    parens = []

    while line:
        for c in line:
            if c == '(':
                parens.append(c)
            elif c == ')':
                if not parens:
                    print "Missing opening parenthesis for char at line %s" % n
                    return
                else:
                    parens.pop()
        n += 1
        line = source_file.readline()

    if parens:
        print "Missing closing parenthesis for char at line %s" % parens.pop()

if __name__ == '__main__':
    check_parenthesis(sys.stdin)
