def primo(l,r):
    odd = []
    #for i in range(l,r):
      #  if i % 2 ==0:
     #       odd.append(i)
    odd = [i for i in range(l,r+1) if i % 2 == 1]
    
    print(odd)    

def run():
    l = int(input('Escribe un número: '))
    r = int(input('Escribe otro número: '))
    primo(l,r)



if __name__ == '__main__':
    run()