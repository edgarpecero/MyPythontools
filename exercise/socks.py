def run():
    #n = int(input('number of socks '))
    # input_string = input('Enter elements of a list separated by space ')
    # print("\n")
    # ar = input_string.split()
    # # print list
    # #print('list: ', user_list)

    # # convert each item to int type
    # for x in range(len(ar)):
    #     # convert each item to int type
    #     ar[x] = int(ar[x])
    # print(ar)
    # q = [0 for x in range(101)]
    l=[int(x) for x in input('colors ').split()]
    #print(l)
    
    #q = [0 for p in range(len(l))]
    q = [0 for p in l[::2]]
    
    print (q)
    for i in l:
        q[i] += 1
        #print(q)
    ans = 0
    for i in q:
        if i > 1:
            ans += i//2
    print(ans)



if __name__ == '__main__':
    run()