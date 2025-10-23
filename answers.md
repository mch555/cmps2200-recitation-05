# CMPS 2200 Reciation 5
## Answers

**Name:**____Maeren Hay_____________________


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
The running times confirm the asymptotic bounds for the algorithms. ssort (selection sort) showed O(n^2) quadratic growth in both tables. The Random Permutations test confirmed this for me, when doubling n from 5000 to 10000 increased the runtime by a factore of 4.04 (because 2682ms/663ms =4.04). This showed the complexity factor is 2^2 (4). The fixed pivot quicksort also confirmed the O(n^2) worse case bound when put through presorted permutations. Unlike these two, the random pivot quicksort and timsort confirmed their O(nlogn) bounds. For example, random pivot quicksort's time increased by a small factor of 1.68 when n was doubled from 5000 to 10000. This proves logarithmic growth since 1<1.68<2.

The biggest thing I noticed was how changing the input list affects the performance of the alogrithms. When the input changed to the pre sorted permutations, the fixed pivot quicksort was forced into worse case. This confirms that choosing a predetermined pivot, in this case item[0], makes the algortihm vulnerable with a O(n) recursion depth. 

The random pivot quicksort had consistent outputs, Its runtime stayed pretty close to the same when n was doubled from 5000 to 10000. This proves that randomization is efficient in preventing the worse case of O(n^2) and instead maintains O(nlogn) growth.


- **1c.**
Random pivot quicksort was my fastest output. Looking at Timsort's ouput compared to random pivot quicksort, I see that Timsort is much faster and more efficient. At n =10000 in the random permutations, the random pivot quicksort took 26.68 ms while Timsort took 0.207 ms. This proves that Timsort is the optimal choice and much more efficient in terms of runtime.
