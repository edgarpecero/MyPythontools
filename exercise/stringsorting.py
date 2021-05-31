
def run(order, str):
        output = ""
        d = {x:str.count(x) for x in str}
        print(d)
        #print(d['c'])

        
        #print('c'*d)
        
        for s in order:
            if s in str:
                output += s*d[s]
                #print(s*d[s])
            str = str.replace(s, '')
            #print(str)            
        print (output+str)
        

if __name__ == '__main__':
    order = (input('order '))
    str = (input('str '))
    run(order, str)
