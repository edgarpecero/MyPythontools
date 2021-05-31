def run(n):
    ln = len(n)
    l = []
    c = 0
    for i in range(0,ln):
        # print('ooooo')
        # print(n[i])
        # print('---')
        # # print(i)
        
        # j = i + 1
        for j in range(i+1,ln):
            # # print(j)
            # print(n[j])

            #print('end')
            if n[i] == n[j]:
                l.append(n[i])
    

    return len(l)


if __name__ == '__main__':
    n=[1,2,3,1,1,3]
    print(run(n))