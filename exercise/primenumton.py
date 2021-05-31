def run(n):
    if n <= 1: 
        return print('no prime num')
    c = 0
    q = [ i for i in range(2,n+1)]
    #print(q)
    o = []
    if n > 1:
        for j in q:          
            for i in range(2, (j//2)+1):
                if(j%i)==0:
                    break
            else:
                o.append(j)
        print(o)                #"no es primo"
    else: 
        print('no')


if __name__ =='__main__':
    n = (int(input('num ')))
    run(n)