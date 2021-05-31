def run(n):
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
    for i in range(n,0,-1):
        for j in range(1, i,1):
            print((j), end="")
        print()
    # for i in range (n-1,1,-1):
    #     for j in range(i, n)

if __name__ =='__main__':
    #n = (int(input('num ')))
    n = 4
    run(n)