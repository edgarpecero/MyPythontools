def run(a):
    la = len(a)
    c = 0
    for i in range(la):
        for j in range(0, la - i - 1): # O(a) * O(a) = O(a * a) = O(a**2)

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                c += 1

    print('Array is sorted in {} swaps.'.format(c))  
    print('First Element: {}'.format(a[0]))  
    print('Last Element: {}'.format(a[la-1]))

if __name__ == '__main__':
    a = [1,2,3]
    run(a)