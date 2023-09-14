# Comparing Sorting Algorithms
In this project I coded 4 different sorting algorithms: heap sort, merge sort, insertion sort, and quicksort. These sorting algorithms were tested using various length and randomizations of list to see which performed the best. I then tested chatGPT's versions of these algorithms against the initial versions to see which performed more efficently.
## Random Lists
### Testing list
The testonalg function allows me to test the runtime of a single sorting function, f, on a single input list , inlist. f is simply the name of any sort function implemented or imported into the file. The function checksorted checks if the list is sorted by the sorting algorithm. If the 1st argument is not sorted, it will print an error message which will print out the list and state the name of the function in the 2nd argument.
### Generating random lists
The function randomlist(n,k), which creates a list of n integers. It starts by generating a list of the integers from 1 to (n-k), and then, k times, it randomly selectss an integer from the list and appends it onto the end. The list will then have n items in total ( n-k distinct items, and k items that are duplicates of other items in the list). Finally it finishes by shuffling the list. I import the random package, first to select random indices in the list, and then to shuffle the list. we can now combine this with testonealg(...) to get a runtime for a sorting algorithm working on a random list of size n with k duplicates.
### Evaluating a Function on Multiple Lists
In order to get a reliable view of the runtime of an algorithm, we should not run it on just a single list of size n, since it is possible that a lucky shuffle has given us something easy to sort. Instead I generated many different shuffles of our list, run our sort algorithm on each one, and then report the average runtime. To do this, I wrote a function called evaluate(n, k, num, f), which generates num lists, each of length n with k duplicates, then calls testonealg(?,f) on each of them, computes the average runtime, and prints the result to screen, including the runtime, the function name, and the parameters n and k. 
### Evaluating Different Algorithms
I compare the runtimes of different algorithms. To be fair to each algorithm, I need to make sure that each sort algorithm is given the same set of lists to sort. So I wrote a new function evaluateall(n,k,num,funcs), which takes as the last argument a list of function names. I created num shuffled lists as before, but then, for each function f in funcs, for each list in the set, created a copy, and then call testonealg(...), recording the times. I print out the average time for each function. We do have to create these extra copies -- if we don't, then the 2nd algorithm to be evaluated will be given sorted lists as input values.
### Evaluating how algorithms scale with list size
To see how the different algorithms scale with the size of the list, I created an evaluate scale function that changes the length of the list when testing the algorithms.
### Partially Sorted Lists Performance
I wrote another function evaluateallpartial(n,k,d,num,funcs), which does the same as evaluateall(...) above, but now sorts on partially sorted lists. Each list that is generated should first be sorted by python, and then instead of shuffling, for n//d times, two random items in the list are swapped. These partially sorted lists should then by copied and sent to the algorithms for evaluation.
### ChatGPT VS My algorithms
To test chatGPTs accuracy for generating the most efficient version of an algorithm, I prompted chatGPT to give me all the sorting algorithms I needed and then i tested them with my code against my own version of the algorithms.
## Results

Link to results breakdown <a href=[review_sorting_algo.docx](https://github.com/peterhyland0/Comparing-Sorting-Algorithms/files/12609784/review_sorting_algo.docx)>here</a>
![image](https://github.com/peterhyland0/Comparing-Sorting-Algorithms/assets/92451669/83cee8ec-6411-4f76-a3aa-04ba220a1f24)

![image](https://github.com/peterhyland0/Comparing-Sorting-Algorithms/assets/92451669/ac07c724-1ae1-49c3-baba-842fa114c465)

