def DecimalToBinary(n):
    
    # r = "{0:b}".format(int(n))
    c = [int(i) for i in str(n)]
    o = 0
    for i in c:
        if i == 1:
            o += 1
    return o
    # for i in range(0, len(c)):
    #     c[i] = int(c[i])
    # o = 0
    # z = 0
    # stop = False
    # for i in c:
    #     if i == 1:
    #         o += 1
    #         z = 0
    #         if o > 1:
    #             return stop
    #     else:
    #         z += 1
    #         o = 0
    #         if z > 1:
    #             return stop
    



    # if num >= 1:
    #     DecimalToBinary(num // 2)
    # print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    n = (int(input('num ')))
     
    # Calling functionp
    print(DecimalToBinary(n))