def run(s):
    ln = len(s)
    count = 0
    for i in range (ln-1):
        if s[i] == s[i+1]:
            count +=1
    return count
if __name__ == '__main__':
    s = "BBBBB"
    run(s)