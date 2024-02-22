# CSE 5311-002 - Hands On 6

__System Specifications:__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.0
* Python version: 3.9.7

### Quicksort Algorithm

1. Implemented the quicksort algorithm for both last element and random choice pivots in Python.
    <br />For regular last element pivot, run with following command:
    ```
    python3 quicksort.py
    ```
   For random choice pivot, run with following command:
    ```
    python3 quicksort.py --random
    ```

2. __Functionality__

* Partitioning the array based on the pivot element.
  * This is done by selecting the pivot element and then moving all elements less than the pivot to the left and all elements greater than the pivot to the right.
  * The pivot is either the last element or a random element. (Depends on whether the --random flag is used)
  * The pivot is then placed in the correct position.
* Recursively calling the quicksort function on the left and right subarrays.

3. __Arrays used__

* __Worst Array:__ Array of length n with elements in descending order. This produces the worst case scenario since every partitioning results in a 0, n-1 split.
* __Average Array:__ Array of length n with random elements.
* __Best Array:__ For the best case scenario, a special function was created that reverse engineered the partitioning function.
    <br />This function is called `fillBestCaseQuicksortArray(arr, low, high)` and it recursively fills the array with elements in such a way that every element starting from the end of the array is always the pivot that splits the array into two equal halves.
<br />Specifically, The pivot is added to the beginning of the array. So the first element added (Which will be the last element of the final array) will be the median of the whole array.
<br />The second element to be added will be the median of the left half of the array.
<br />The third element to be added will be the median of the left quarter of the array.
<br />And so on until the left half of the array of each recursive call is fully filled.
<br />The same thing happens for the right halfs of each recursive call. Therefore, when the array is filled the partitioning will be done in a way that each recursive call will split the subarrays in equal halves.
<br />The function is called as `fillBestCaseQuicksortArray(arr, 0, n + 2**int(log2(n))-1)`. 
<br />Instead of n, `n + 2**int(log2(n))-1` is used to calculate the length of the array to be filled.
Since every recursive call (either left-hand or right-hand) disregards the mid element, the output of the function with a `(0, n)` input, would be short in length (in contrast to the n length arrays) by the number of mids that would occur which is equal to the number of subarrays created during the partitioning of the final (minus 1 for the first split). This number is `2**int(log2(n)) - 1`.

4. __Benchmarks__
<br />By using the timeit module, the following times were recorded (n=100)
* Non Random Pivot (Last Element):
  * tWorst:  0.00030150002567097545
  * tAvg:  7.400003960356116e-05
  * tBest:  6.512500112876296e-05
* Random Pivot:
  * tWorst:  0.00018375000217929482
  * tAvg:  6.616703467443585e-05
  * tBest:  6.525003118440509e-05

5. __Average Runtime Complexity__
<br />For the non random pivot version of quicksort each level of recursion takes:
<br />$$T(n) = T\left(\frac{ln}{k}\right) + T\left(\frac{(k-l)n}{k}\right) + n$$
<br />We know that the average runtime is bounded by the worst and best case scenarios. Therefore we assume that the best case scenario might be the average case and try to prove it.
$$T(n)<=cn\lg(n)$$

$$\Rightarrow T\left(\frac{ln}{k}\right) + T\left(\frac{\left(k-l\right)n}{k}\right) + n \leq c\frac{ln}{k}\lg\left(\frac{ln}{k}\right) + c\frac{(k-l)n}{k}\lg\left(\frac{\left(k-l\right)n}{k}\right) + n$$

$$= c\frac{ln}{k}\lg\left(\frac{ln}{k}\right) - c\left(\frac{(l-k)n}{k}\right)\lg\left(\frac{(k-l)n}{k}\right) + n$$

$$= cn\left(\frac{l}{k}\right)\left[\lg\left(\frac{l}{k}n\right) - k\lg\left(\frac{k-l}{k}n\right)\right] + n$$

$$= cn\left(\frac{l}{k}\right)\left[\lg\left(\frac{n}{\frac{k}{l}}\right) - k\lg\left(\frac{n}{\frac{k}{k-l}}\right)\right] + n$$

$$= cn\left(\frac{l}{k}\right)\left[\lg\left(n\right) - \lg\left(\frac{k}{l}\right) - k\lg\left(\frac{n}{\frac{k}{k-l}}\right)\right] + n$$

Cancelling the negative terms (hence producing a larger sum):

$$\leq cn\left(\frac{l}{k}\right)\lg\left(n\right) + n$$

$$\leq cn\lg\left(n\right) + n$$

$$\Rightarrow T(n) = O(n\lg(n))$$

6. __Notes__
* If a large n is required then the recursion limit should be increased. This is done by using the following command:
  ```
  import sys
  sys.setrecursionlimit(<large n + c>)
  ```
  Where c is a small constant added to n to ensure that the recursion limit is not reached because of the other functions in the script (e.g. insert, rand, etc. in this case).