def run(a, b):
    xx = [char for char in a]
    yy = [char for char in b]
    lx = len(a)
    ly = len(b)

    if ly == lx:
        for i in range(0,len(xx)):
            l += xx[i] + yy[i]
        return l
    elif lx > ly:
        for i in range(0,len(yy)):
            l += xx[i] + yy[i]
        del xx[:ly]
        for i in range(0,len(xx)):
            l += xx[i]
        return l
    elif ly > lx:
        for i in range(0,len(xx)):
            l += xx[i] + yy[i]
        del yy[:lx]
        for i in range(0,len(yy)):
            l += yy[i]
        return l

if __name__ == '__main__':
    a = 'abc'
    b = 'deffasd'
    print(run(a,b))