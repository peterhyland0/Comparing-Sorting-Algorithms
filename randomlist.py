import time 
import random
from copy import deepcopy

from sorting_algorithms import *
from chatgptalgo import *


def checksorted(inlist,f):
    
    n = len(inlist)
    for index in range(0,(n-1)):
        if inlist[index] > inlist[index+1]:
            print("Error: "+ str(inlist) , inlist[index], inlist[index+1], f.__name__)
            break

def randomlist(n,k):
    rand_list=[]
    for num in range(1,(n+1)-k):
        rand_list.append(num)
    for dup in range(k):
        rand_list.append(random.randint(1,len(rand_list)))
        random.shuffle(rand_list)
    return rand_list

def partiallist(n,k,swaps):
    part_list=[]
    for num in range(1,(n+1)-k):
        part_list.append(num)
    for dup in range(k):
        part_list.append(random.randint(1,len(part_list)))
    
    part_list = sorted(part_list)    
    idx = range(len(part_list))
    for i in range(swaps):
        i1, i2 = random.sample(idx,2)
        part_list[i1], part_list[i2] = part_list[i2], part_list[i1]
        
        
    return part_list

def testonealg(inlist, f):
    if f.__name__ == "quicksort":
        start_time = time.perf_counter()
        outlist = f(inlist)
        end_time = time.perf_counter()
        checksorted(outlist, f)
    elif f.__name__ == "quickChatGPT":
        start_time = time.perf_counter()
        outlist = f(inlist)
        end_time = time.perf_counter()
        checksorted(outlist, f)
    else:
        start_time = time.perf_counter()
        f(inlist)
        end_time = time.perf_counter()
        checksorted(inlist, f)
    
    return end_time - start_time


def evaluate(n, k, num, f):
    firstlist = []
    total = 0
    for i in range(num):
        firstlist.append(randomlist(n,k))
    for j in firstlist:
        list_time = testonealg(j,f)
        total += list_time
    average = total/num
    print(average)
    

def evaluateall(n,k,num,funcs):
    list1 = []
   
    
    print("evaluate all:")
    for i in range(num):
        list1.append(randomlist(n,k))
    list2 = deepcopy(list1)
    list3 = deepcopy(list1)
    list4 = deepcopy(list1)
    list5 = deepcopy(list1)
    list6 = deepcopy(list1)
    list7 = deepcopy(list1)
    list8 = deepcopy(list1)
    biglist = [list1,list2,list3,list4,list5,list6,list7,list8]
    for count, func in enumerate(funcs):
        total = 0
        for j in biglist[count]:
            list_time = testonealg(j,func) 
            total += list_time
        average = total/num
        
        print(f"Sort Type: {func.__name__:<20}       Average Sort Time: {average:<30}  Length: {len(j)}")
            
def evaluateallpartial(n,k,swaps,num,funcs):
    
    list1 = []
    
    print("evaluate all partial:")
    for i in range(num):
        list1.append(partiallist(n,k,swaps))
    list2 = deepcopy(list1)
    list3 = deepcopy(list1)
    list4 = deepcopy(list1)
    biglist = [list1,list2,list3,list4]
    for count, func in enumerate(funcs):
        total = 0
        for j in biglist[count]:
            list_time = testonealg(j,func) 
            total += list_time
        average = total/num
        
        print(f"Sort Type: {func.__name__:<15}       Average Sort Time: {average:<25}  Length: {len(j)}  Swaps: {swaps:<5}")
        
def evaluatescale():
    parameters = [(10, 2),
                  (100, 20),
                  (1000, 200),
                  (10000, 2000)]
    functions = [ mergesort, mergeChatGPT, quicksort, quickChatGPT, heapsort, heapChatGPT,insertionsort, insertionChatGPT ]
    for (n,k) in parameters:
        evaluateall(n,k,20,functions)




# n lists are ran on each sorting algorithm and the average of n is given as the output.
# this code is testing the amount of random swaps that occur in the list to give a partially sorted list (swaps).
def evaluatescalepartial():
    parameters = [(1000, 200, 0),
                  (1000, 200, 100),
                  (1000, 200, 200),
                  (1000, 200, 300),
                  ]
    # parameters = [(10, 2, 0),
    #               (10, 2, 2),
    #               (10, 2, 4),
    #               (10, 2, 6),
    #               (10, 2, 10)]
    functions = [ mergesort, heapsort, insertionsort, quicksort]
    for (n,k,swaps) in parameters:
        evaluateallpartial(n,k,swaps,20,functions)
    


print(evaluate(10,3,3,mergesort))

print(partiallist(10,2,6))
evaluatescalepartial()

evaluateall(10,3,50,[heapsort,heapsort,heapsort,heapsort])
evaluateallpartial(10,3,1,1,[insertionsort,mergesort,heapsort,quicksort])

evaluatescale()
print(randomlist(10,3))




