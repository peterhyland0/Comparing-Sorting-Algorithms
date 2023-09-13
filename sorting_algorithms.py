import random
import copy

#I got this insertion sort and heap sort code from the solutions to lab 1.
#I got the merge sort algorithm from the lecture notes
#i got the quicksort algorithm from github
#https://github.com/msdundar/notes-algorithms/blob/master/07-quicksort/quicksort.py

def insertionsort(mylist):
    n = len(mylist)
    i = 1

    while i < n:
        j = i-1
        while mylist[i] < mylist[j] and j > -1:
            j -= 1
        #insert i in the cell after j
        temp = mylist[i]
        k = i-1
        while k > j:
            mylist[k+1] = mylist[k]
            k -= 1
        mylist[k+1] = temp
        i += 1

def heapsort(inlist):
    length = len(inlist)
    for i in range(length):
        bubbleup(inlist,i)

    length = len(inlist)
    for i in range(length):
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist,0, length-2-i)



def bubbleup(inlist, i):
    while i > 0:
        parent = (i-1) // 2
        if inlist[i] > inlist[parent]:
            # print('swapping:', inlist[i], 'with its parent:', inlist[parent])
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0

def bubbledown(inlist, i, last):
    while last > (i*2):  #so at least one child
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc   # start by assuming left child is the max child
        if last > lc and inlist[rc] > inlist[lc]:  #rc exists and is bigger
            maxc = rc
        if inlist[i] < inlist[maxc]:
            # print('swapping:', inlist[i], 'with its child:', inlist[maxc])
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last


def mergesort(mylist):
    n = len(mylist)
    if n > 1:
        list1 = mylist[:n//2]
        list2 = mylist[n//2:]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, mylist)

def merge(list1, list2, mylist):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(mylist):
        if f1 == len(list1):
            mylist[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            mylist[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            mylist[f1+f2] = list2[f2]
            f2 += 1
        else:
            mylist[f1+f2] = list1[f1]
            f1 += 1

#https://github.com/msdundar/notes-algorithms/blob/master/07-quicksort/quicksort.py
def quicksort(array):
  less = []
  greater = []

  if len(array) < 2:
    return array # base case
  else:
    pivot = array[0] # pick a pivot
    for i in array[1:]:
      if i <= pivot:
        less.append(i)
      else:
        greater.append(i)
      
    return quicksort(less) + [pivot] + quicksort(greater)

def testSorts():
    listforheap = [7,3,9,4,1,8,10,5,2,6]
    heapsort(listforheap)
    print(listforheap, "heapsorted list")
    listforins = [7,3,9,4,1,8,10,5,2,6]
    insertionsort(listforins)
    print(listforins, "insertionsort list")




def evaluateSorts():
    for i in range(4):
        print("List size:", pow(10,i+1))
        list = [j for j in range(pow(10,i+1))]
        random.shuffle(list)
        list2 = copy.copy(list)
        print("insertionsort starting ...")
        insertionsort(list)
        print("insertionsort finished")
        print("heapsort starting ...")
        heapsort(list2)
        print("heapsort finished")
        """ """        
        if i < 2:  # print the lists to check they have actually been sorted.
            print(list)
            print(list2)

        """ """

#print(quicksort([5, 2, 8, 8, 6, 7, 3, 4, 5, 1]))


if __name__ == "__main__":
    testSorts()
    evaluateSorts()
    
    