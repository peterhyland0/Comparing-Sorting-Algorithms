# Comparing-Sorting-Algorithms
In this project I coded 4 different sorting algorithms: heap sort, merge sort, insertion sort, and quicksort. These sorting algorithms were tested using various length and randomizations of list to see which performed the best. I then tested chatGPT's versions of these algorithms against the initial versions to see which performed more efficently.
# Random Lists
# testing list
The testonalg function allows me to test the runtime of a single sorting function, f, on a single input list , inlist. f is simply the name of any sort function implemented or imported into the file. The function checksorted checks if the list is sorted by the sorting algorithm. If the 1st argument is not sorted, it will print an error message which will print out the list and state the name of the function in the 2nd argument.
# Generating random lists
The function randomlist(n,k), which creates a list of n integers. It starts by generating a list of the integers from 1 to (n-k), and then, k times, it randomly selectss an integer from the list and appends it onto the end. The list will then have n items in total ( n-k distinct items, and k items that are duplicates of other items in the list). Finally it finishes by shuffling the list.
