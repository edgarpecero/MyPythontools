def maximumToys(prices, k):
    l =[i for i in prices if i < k]
    if sum(l)<k:
        print(sum(l))       
        return len(l)
    else:
        l.sort()
        print(l)
        a = 0
        c = 0
        for i in range(len(l)):
            a += l[i]
            print(a)
            if a < k:
                c +=1 
        return c
 
            

        

if __name__ == '__main__':
    prices = [1,2,3,4]
    k = 7
    print(maximumToys(prices, k))