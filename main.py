import random, time
import tabulate
import sys

sys.setrecursionlimit(20000)
###implement pivot choice functions, pivot_first chooses first element of list as pivot, pivot_random chooses a random element of list as pivot
def pivot_first(L):
    return L[0]
def pivot_random(L):
    return random.choice(L)

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        #print('selecting minimum %s' % L[m])       
        L[0], L[m] = L[m], L[0]
        #print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])
###implement qsort while using partitioning methods from lecture        
def qsort(a, pivot_fn):
    if len(a) <= 1:
        return a
    pivot_value = pivot_fn(a)

    L, R, P = [],[],[]
    for x in a:
        if x < pivot_value:
            L.append(x)
        elif x > pivot_value:
            R.append(x)
        else:
            P.append(x)
    return qsort(L, pivot_fn) + P+ qsort(R, pivot_fn)
        
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    L=list(mylist)
    start = time.time()
    sort_fn(L)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ###used our pivot choice functions to sort the algorithms for comparison
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda L: qsort(L, pivot_first)
    qsort_random_pivot = lambda L: qsort(L, pivot_random)
    tim_sort = sorted
    selection_sort= ssort
    print("--1b: Random Permutation--")
    result=[]
    for size in sizes:
        # create list in ascending order
        mylist_template = list(range(size))
        random.shuffle(mylist_template)

        result.append([
            len(mylist_template),
            time_search(selection_sort, mylist_template),
            time_search(qsort_fixed_pivot, mylist_template),
            time_search(qsort_random_pivot, mylist_template),
            time_search(tim_sort, mylist_template)
        ])
    print_results(result, headers=['n', 'Selection Sort', 'qsort-fixed-pivot', 'qsort-random-pivot', 'Timsort'])

    print("\n--1b: Already Sorted Permutations--")
    result_sorted= []
    for size in sizes:
        mylist_template = list(range(size))
        result_sorted.append([
            len(mylist_template),
            time_search(selection_sort, mylist_template),
            time_search(qsort_fixed_pivot, mylist_template),
            time_search(qsort_random_pivot, mylist_template),
            time_search(tim_sort, mylist_template)
        ])
    return result_sorted
    ###
headers=['n', 'Selection Sort', 'qsort-fixed-pivot', 'qsort-random-pivot', 'Timsort']
def print_results(results, headers):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=headers,
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    sizes = [100, 500, 1000, 2000, 5000, 10000] 
    results_sorted = compare_sort(sizes=sizes)
    print_results(results_sorted, headers=['n', 'Selection Sort', 'qsort-fixed-pivot', 'qsort-random-pivot', 'Timsort'])
    

random.seed()
test_print()
