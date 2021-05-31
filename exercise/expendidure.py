def run(expenditure, d):
    s = sorted(expenditure)
    n = len(expenditure)
    if n%2 != 0:
        m =  n//2 #median
    else: 
        m = n//2
        m = float((s[m]+s[m-1])/2)
        #print(m)
    mm = int(2*m)
    print(m)



if __name__ == '__main__':
    expenditure = [1,2,3,4]
    
    #expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    run(expenditure,d)