# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
import time
def partition(arr, low, high):

    i = ( low - 1)  #index of smaller element   
    p = arr[high]   #pivot  = 5
    # print(i)          = -1
    # print(arr[5])     = 5 last arr position
    # print(arr[low])   = 10 first arr position
    #print(arr)
    #partition(arr, 0, n-1) 
    
    for x in range(low, high):
        #print(x)  = 0 , 1, 2, 3, 4,   = 5 positions
        #print(arr[x])
        #if current element is smaller than or equal to Pivot
        if arr[x] <= p: 
            #print('hola') 
            #increment index of smaller elment
            i += 1
            #print(i)  = 0    
            #print(x)  = position 2, is num 2, 2 < pivot(5), enter to IF condition
            # print('arr')
            # print(arr[i])   #  = 10 in arr[0]
            # print(arr[x])   #  = 2 in arr[2]
            # print('after') 
            #"""swaping elements smaller than Pivot"""
            arr[i], arr[x] = arr[x], arr[i] 
            #"""new arr contains swaping elements"""
            # print(arr[i])   #  = 2 in arr[0]
            # print(arr[x])   #  = 10 in arr[2]
            # print(' ')
    # print(arr)      #= new arr = [2,1,10,9,7,5]
    # print(i)        # i = 1; cause i counter took 2 if condition, fron 0 to 1
    # print(x)        # x = 4; cause for loop took 5 steps from 0 to 4
    # print('end')
    # print(arr[i + 1])   # arr[i + 1] = 10, Start of higher numbers than pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # print('after') 
    # print(arr[i + 1])   # pivot is now locate in the middle, as a pivot
    #                     # high number than pivot is locate at the end of the 
    #                     #  array, only because is higher;)
    #print(arr)
    return(i + 1) #position of the pivot

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

def quickSort(arr, low, high):
    # print(arr)
    # print('start')

    # print(low)
    # print(high)
    # time.sleep(1)
    # #(partition(arr, low, high)) = 2
    if low < high: 
        
        # print(arr)
        # print('salto')
        # # print(low)
        # # print(high)
        #time.sleep(1)

            # pi is partitioning index, arr[p] is now 
            # at right place 
        pi = partition(arr,low,high)
        #print(arr)
        #print(pi)
         # pi = 2, in arr[2] = to pivot's position
            # Separately sort elements before 
            # partition and after partition 
        #print(pi)
        quickSort(arr, low, pi-1)
        #print(pi)

        quickSort(arr, pi+1, high) 


if __name__ == '__main__':
    arr = [3, 7, 2, 9, 1, 5] 
    n = len(arr) 
    #print('len {}'.format(n))
    #print(partition(arr, 3, 5))
    quickSort(arr, 0, n-1) 
    print(arr)
    # print ("Sorted array is:") 
    # for i in range(n): 
    #     print(arr)
    #     print ("%d" %arr[i]), 