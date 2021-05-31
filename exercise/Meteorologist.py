def run(n):
    q = [i for i in n]
    m = n.index(max(n))
    if n[m+1] > n[m-1]:
        return n[m]-n[m-1]
    else: 
        return n[m]-n[m+1]

    




if __name__ == '__main__':
    n = [7, 2, 10, 8 , 9, 1]
    print(run(n))
    
