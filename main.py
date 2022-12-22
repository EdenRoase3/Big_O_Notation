import time
import os
import random


Sys = os.sys
Sys.setrecursionlimit(2000000000)


# ---------------------------------####-Selection Sort-#####-------------------------------#
# ///////////Iterative Selection Sort
# https://www.delftstack.com/howto/python/selection-sort-in-python/

def SelectionSort(array, size):
    for step in range(size):
        min_a = step
        for i in range(step + 1, size):
            if array[i] < array[min_a]:
                min_a = i
        (array[step], array[min_a]) = (array[min_a], array[step])


# ///////////Recursive Selection Sort
#https://www.geeksforgeeks.org/recursive-selection-sort/

def minIndex(a, x, y):
    if x == y:
        return x
    z = minIndex(a, x + 1, y)
    return (x if a[x] < a[z] else z)


def recurSelectionSort(a, n, index=0):
    # Return when starting and
    # size are same
    if index == n:
        return -1

    # calling minimum index function
    # for minimum index
    k = minIndex(a, index, n - 1)

    # Swapping when index and minimum
    # index are not same
    if k != index:
        a[k], a[index] = a[index], a[k]

    # Recursively calling selection
    # sort function
    recurSelectionSort(a, n, index + 1)

# ---------------------------------####-Quick Sort-#####-------------------------------#
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


# ///////////Iterative Quick Sort
# https://www.geeksforgeeks.org/python-program-for-iterative-quick-sort/

def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# ///////////Recursive Quick Sort
def quickSortR(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quickSortR(array, low, pi - 1)

        quickSortR(array, pi + 1, high)


# ----------------------####-Perf_Counter() Testing Code-#####---------------------#

def selection_iterative_time(LIST_SIZE):
    for x in LIST_SIZE:
        times = []
        for j in range(5):
            #mylist = [random.randint(0, x) for y in range(x)]
            mylist = random.sample(range(0, x), x)
            start_time = time.perf_counter()
            SelectionSort(mylist, len(mylist))
            end_time = time.perf_counter()
            j = end_time - start_time
            times.append(j)

        print(min(times))
        #print(times)  # In case list of time for every trial is wished to be shown
        print(len(mylist))

def selection_recursive_time(LIST_SIZE):
    for x in LIST_SIZE:
        times = []
        for j in range(5):
            mylist = random.sample(range(0,x), x)
            start_time = time.perf_counter()
            recurSelectionSort(mylist, len(mylist))
            end_time = time.perf_counter()
            j = end_time - start_time
            times.append(j)

        print(min(times))
        print(len(mylist))

def quicksort_iterative_time(LIST_SIZE):
    for x in LIST_SIZE:
        times = []
        for j in range(5):
            mylist = random.sample(range(0, x), x)
            start_time = time.perf_counter()
            quickSortIterative(mylist, 0, len(mylist) - 1)
            end_time = time.perf_counter()
            j = end_time - start_time
            times.append(j)

        print(min(times))
        print(len(mylist))

def quicksort_recursive_time(LIST_SIZE):
    for x in LIST_SIZE:
        times = []

        for j in range(5):
            mylist = random.sample(range(0, x), x)
            start_time = time.perf_counter()
            quickSortR(mylist, 0, len(mylist) - 1)
            end_time = time.perf_counter()
            j = end_time - start_time
            times.append(j)

        print(min(times))
        print(len(mylist))

#_--------------------------Time.process_time() Testing Code----------------------------------

def selection_iterative_process(LIST_SIZE):
    for x in LIST_SIZE:

        times = []
        for j in range(5):
            mylist = random.sample(range(0, x), x)
            start_time = time.process_time()
            SelectionSort(mylist, len(mylist))
            end_time = time.process_time()
            execution_time = end_time - start_time
            times.append(execution_time)

        print(min(times))
        print(len(mylist))

def selection_recursive_process(LIST_SIZE):
    for x in LIST_SIZE:

        times = []
        for j in range(5):
            mylist = random.sample(range(0, x), x)
            start_time = time.process_time()
            recurSelectionSort(mylist, len(mylist))
            end_time = time.process_time()
            execution_time = end_time - start_time
            times.append(execution_time)

        print(min(times))
        print(len(mylist))

def quicksort_iterative_process(LIST_SIZE):
    for x in LIST_SIZE:

        times = []
        for j in range(5):
            mylist = random.sample(range(0, x), x)
            start_time = time.process_time()
            quickSortIterative(mylist, 0, len(mylist)-1)
            end_time = time.process_time()
            execution_time = end_time - start_time
            times.append(execution_time)

        print(min(times))
        print(len(mylist))

def quicksort_recursive_process(LIST_SIZE):
    for x in LIST_SIZE:

        times = []
        for j in range(5):
            mylist = random.sample(range(0, x), x)
            start_time = time.process_time()
            quickSortR(mylist,0, len(mylist)-1)
            end_time = time.process_time()
            execution_time = end_time - start_time
            times.append(execution_time)

            """
            THE PROBLEM was that I was doing a recurive research on an already sorted list
            the only thing possible is to create a list for every single one but it would be 
            very tedious. Also I would not be able to go through it all in one function. So in order to do that Im must 
            create a very different set of htings in order to actually fix the problem. 
            """


        print(min(times))
        print(len(mylist))


'''
So in breaking the code down and using another different method of timing, I realized how 
an erroneous use of a sorting algorithm, to sort an already sorted list, will only give result
to an overflow error, causing the maximum number of recursions to become negative. 
'''



#_--------------------------Text Based UI----------------------------------

def show_menu():
    LIST_SIZE = [10, 25, 100, 150, 250, 300, 550, 1000, 1250, 1300, 1400, 5000, 5300, 6000, 7500, 10000, 15000, 100000,
                 150000, 1000000]

    print("""
    This program calculates the time for the two sorting algorithms: 
    Selection Sort and Quick Sort and compares their Iterative vs Recursive versions. 
    
    Select one from the following options to get the analyzed data:
    
    1) Selection iterative  with perf_counter() method for a dataset of size 20
    2) Selection recursive with perf_counter() method for a datatset of size 20
    3) Quick sort iterative with perf_counter() method for a dataset of size 20 
    4) Quick sort recursive with perf_counter() method for a dataset of size 20
    5) Selection iterative  with time.process_time() method for a dataset of size 20
    6) Selection recursive with time.process_time() method for a datatset of size 20
    7) Quick sort iterative with time.process_time() method for a dataset of size 20 
    8) Quick sort recursive with time.process_time() method for a dataset of size 20
    
    9) Exit""")

    selection = int(input("Please enter your selection: "))

    while (selection) != 9:
     if selection == 1:
        selection_iterative_time(LIST_SIZE)
        break
     elif selection == 2:
        selection_recursive_time(LIST_SIZE)
        break
     elif selection == 3:
         quicksort_iterative_time(LIST_SIZE)
         break
     elif selection == 4:
         quicksort_recursive_time(LIST_SIZE)
         break
     elif selection == 5:
         selection_iterative_process(LIST_SIZE)
         break
     elif selection == 6:
         selection_recursive_process(LIST_SIZE)
         break
     elif selection == 7:
         quicksort_iterative_process(LIST_SIZE)
         break
     elif selection == 8:
         quicksort_recursive_process(LIST_SIZE)
         break
     else:
         print('Invalid input')



show_menu()


