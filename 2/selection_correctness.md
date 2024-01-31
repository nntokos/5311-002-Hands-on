## Selection Sort Correctness

__Loop invariant:__ At the start of each iteration of the outer for loop, the subarray A[1,..,i-1] contains the i-1 smallest elements of A, in sorted order.

* __Initialization:__ Prior to the first iteration (i = 1), the subarray A[1,..,i-1] = A[1,0] is empty, and so it trivially contains the i-1 smallest elements of A, in sorted order.

* __Maintenance:__ To see that each iteration maintains the loop invariant, we must show that A[1,..,i] contains the i smallest elements of A, in sorted order, given that A[1,..,i-1] contains the i-1 smallest elements of A, in sorted order.
<br />The inner loop of the algorithm searches for the smallest element in A[i,...,n] and swaps it with A[i].
Since A[1,..,i-1] contains the i-1 smallest elements of A, any element in A[i,...,n] will be bigger than any element in A[1,...,i-1]. So now A[i] is the biggest element in A[1,..,i].
<br />And since A[1,...,i-1] is sorted, A[1,...,i] is also sorted.

* __Termination:__ At termination, i = n+1. Using the loop invariant, the subarray A[1,..,n] contains the n smallest elements of A, in sorted order. Thus, the algorithm is correct.