def run(nums):
    ln = len(nums)
    l = []
    a =sum(nums)
    q = 0
    # for i in range(ln):
    #     q += sum(nums)
    # for i in range(ln):
    #     l.append(sum(nums[i:ln]))
    # return 
    for i in range(ln):
        l.append(sum(nums[0:i+1]))
    return l
    #return [sum(nums[0:i+1]) for i in range(len(nums))]
            
        

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(run(nums))