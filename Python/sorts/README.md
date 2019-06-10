

# Sorting Algorithms


### Bubble Sort
![alt text][bubble-image]

**Bubble sort**, sometimes referred to as *sinking sort*, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n)
* Average case performance	O(n<sup>2</sup>)

###### Source: [Wikipedia][bubble-wiki] 
###### View the algorithm in [action][bubble-toptal]

### Bucket
![alt text][bucket-image-1]
![alt text][bucket-image-2]

**Bucket sort**, or _bin sort_, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n+k)
* Average case performance	O(n+k)

###### Source: [Wikipedia][bucket-wiki] 


### Cocktail shaker
![alt text][cocktail-shaker-image]

**Cocktail shaker sort**, also known as _bidirectional bubble sort_, _cocktail sort_, _shaker sort_ (which can also refer to a variant of _selection sort_), _ripple sort_, _shuffle sort_, or _shuttle sort_, is a variation of bubble sort that is both a stable sorting algorithm and a comparison sort. The algorithm differs from a bubble sort in that it sorts in both directions on each pass through the list.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n)
* Average case performance	O(n<sup>2</sup>)

###### Source: [Wikipedia][cocktail-shaker-wiki] 


### Insertion Sort
![alt text][insertion-image]

**Insertion sort** is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on *large* lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n)
* Average case performance	O(n<sup>2</sup>)

###### Source: [Wikipedia][insertion-wiki]
###### View the algorithm in [action][insertion-toptal]


### Merge Sort
![alt text][merge-image]

**Merge sort** (also commonly spelled *mergesort*) is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output. Mergesort is a divide and conquer algorithm that was invented by John von Neumann in 1945.

__Properties__
* Worst case performance	O(n log n)
* Best case performance	O(n log n)
* Average case performance	O(n log n)

###### Source: [Wikipedia][merge-wiki] 
###### View the algorithm in [action][merge-toptal]

### Quick
![alt text][quick-image]

**Quicksort** (sometimes called *partition-exchange sort*) is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(*n* log *n*) or O(n) with three-way partition
* Average case performance	O(*n* log *n*)

###### Source: [Wikipedia][quick-wiki]
###### View the algorithm in [action][quick-toptal]


### Heap
![alt text][heapsort-image]

**Heapsort** is a _comparison-based_ sorting algorithm. It can be thought of as an improved selection sort. It divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region.

__Properties__
* Worst case performance	O(*n* log *n*)
* Best case performance	O(*n* log *n*)
* Average case performance	O(*n* log *n*)

###### Source: [Wikipedia][heap-wiki]
###### View the algorithm in [action](https://www.toptal.com/developers/sorting-algorithms/heap-sort)


### Radix

From [Wikipedia][radix-wiki]: Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.

__Properties__
* Worst case performance	O(wn)
* Best case performance	O(wn)
* Average case performance	O(wn)

###### Source: [Wikipedia][radix-wiki] 


### Selection
![alt text][selection-image]

**Selection sort** is an algorithm that divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

__Properties__
* Worst case performance	O(n<sup>2</sup>)
* Best case performance	O(n<sup>2</sup>)
* Average case performance	O(n<sup>2</sup>)

###### Source: [Wikipedia][selection-wiki] 
###### View the algorithm in [action][selection-toptal]


### Shell
![alt text][shell-image]

**Shellsort** is a generalization of *insertion sort* that allows the exchange of items that are far apart.  The idea is to arrange the list of elements so that, starting anywhere, considering every nth element gives a sorted list.  Such a list is said to be h-sorted.  Equivalently, it can be thought of as h interleaved lists, each individually sorted.

__Properties__
* Worst case performance O(*n*log<sup>2</sup>*n*)
* Best case performance O(*n* log *n*)
* Average case performance depends on gap sequence

###### Source: [Wikipedia][shell-wiki]
###### View the algorithm in [action][shell-toptal]


### Topological

From [Wikipedia][topological-wiki]: **Topological sort**, or _topological ordering of a directed graph_ is a linear ordering of its vertices such that for every directed edge _uv_ from vertex _u_ to vertex _v_, _u_ comes before _v_ in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this application, a topological ordering is just a valid sequence for the tasks. A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a _directed acyclic graph_ (DAG). Any DAG has at least one topological ordering, and algorithms are known for constructing a topological ordering of any DAG in linear time.

### Time-Complexity Graphs

Comparing the complexity of sorting algorithms (*Bubble Sort*, *Insertion Sort*, *Selection Sort*)

![Complexity Graphs](https://github.com/prateekiiest/Python/blob/master/sorts/sortinggraphs.png)

Comparing the sorting algorithms:
<br>  -Quicksort is a very fast algorithm but can be pretty tricky to implement
<br>  -Bubble sort is a slow algorithm but is very easy to implement. To sort small sets of data, bubble sort may be a better option since it can be implemented quickly, but for larger datasets, the speedup from quicksort might be worth the trouble implementing the algorithm.



----------------------------------------------------------------------------------------------------------------------

[bubble-toptal]: https://www.toptal.com/developers/sorting-algorithms/bubble-sort
[bubble-wiki]: https://en.wikipedia.org/wiki/Bubble_sort
[bubble-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Bubblesort-edited-color.svg/220px-Bubblesort-edited-color.svg.png "Bubble Sort"

[bucket-wiki]: https://en.wikipedia.org/wiki/Bucket_sort
[bucket-image-1]: https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Bucket_sort_1.svg/311px-Bucket_sort_1.svg.png "Bucket Sort"
[bucket-image-2]: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Bucket_sort_2.svg/311px-Bucket_sort_2.svg.png "Bucket Sort"

[cocktail-shaker-wiki]: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
[cocktail-shaker-image]: https://upload.wikimedia.org/wikipedia/commons/e/ef/Sorting_shaker_sort_anim.gif "Cocktail Shaker Sort"

[insertion-toptal]: https://www.toptal.com/developers/sorting-algorithms/insertion-sort
[insertion-wiki]: https://en.wikipedia.org/wiki/Insertion_sort
[insertion-image]: https://upload.wikimedia.org/wikipedia/commons/7/7e/Insertionsort-edited.png "Insertion Sort"

[quick-toptal]: https://www.toptal.com/developers/sorting-algorithms/quick-sort
[quick-wiki]: https://en.wikipedia.org/wiki/Quicksort
[quick-image]: https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif "Quick Sort"

[heapsort-image]: https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif "Heap Sort"
[heap-wiki]: https://en.wikipedia.org/wiki/Heapsort

[radix-wiki]: https://en.wikipedia.org/wiki/Radix_sort

[merge-toptal]: https://www.toptal.com/developers/sorting-algorithms/merge-sort
[merge-wiki]: https://en.wikipedia.org/wiki/Merge_sort
[merge-image]: https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif "Merge Sort"

[selection-toptal]: https://www.toptal.com/developers/sorting-algorithms/selection-sort
[selection-wiki]: https://en.wikipedia.org/wiki/Selection_sort
[selection-image]: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Selection_sort_animation.gif/250px-Selection_sort_animation.gif "Selection Sort Sort"

[shell-toptal]: https://www.toptal.com/developers/sorting-algorithms/shell-sort
[shell-wiki]: https://en.wikipedia.org/wiki/Shellsort
[shell-image]: https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif "Shell Sort"

[topological-wiki]: https://en.wikipedia.org/wiki/Topological_sorting

[linear-wiki]: https://en.wikipedia.org/wiki/Linear_search
[linear-image]: http://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif "Linear Search"

[binary-wiki]: https://en.wikipedia.org/wiki/Binary_search_algorithm
[binary-image]: https://upload.wikimedia.org/wikipedia/commons/f/f7/Binary_search_into_array.png "Binary Search"


[interpolation-wiki]: https://en.wikipedia.org/wiki/Interpolation_search

[jump-wiki]: https://en.wikipedia.org/wiki/Jump_search

[quick-wiki]: https://en.wikipedia.org/wiki/Quickselect

[tabu-wiki]: https://en.wikipedia.org/wiki/Tabu_search

[ROT13-image]: https://upload.wikimedia.org/wikipedia/commons/3/33/ROT13_table_with_example.svg "ROT13"

[JumpSearch-image]: https://i1.wp.com/theoryofprogramming.com/wp-content/uploads/2016/11/jump-search-1.jpg "Jump Search"

[QuickSelect-image]: https://upload.wikimedia.org/wikipedia/commons/0/04/Selecting_quickselect_frames.gif "Quick Select"
