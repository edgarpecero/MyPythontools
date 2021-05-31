def run(n):
    ln = len(n)
    l = []
    c = 0
    q = set([x for x in n if n.count(x)>1])
    return len(q)
    
    # for i in (0,ln):
    #     print(i)
    #     for j in (i+1,ln):
    #         print(j)
    #         if n[i] == n[j]:
                

                

if __name__ == '__main__':
    n = [1,2,2,3,3,4,5,6,6,6,5,6,7,8,8,8,8,8,9,9,1]
    print(run(n))