# CSE 5311-002 - Hands On 4

__System Specifications:__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.0
* Python version: 3.9.7

### Problem 0 - Fibonacci Sequence

1. Implemented the fibonacci sequence of question 0 in the file 'problem_0.py'.
   <br />Specific Fibonacci code:
   ```python
    def fib(n):
         if n == 0:
              return 0
         elif n == 1:
              return 1
         else:
              return fib(n-1) + fib(n-2)
   ```
   <br />Run with following command:
   ```
   python3 problem_0.py
   ```
   

2. By stepping into the function when calling fib(5), I get the following sequence:
   <br />fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1) -> fib(0)<br />-> fib(1) -> fib(2)<br /> -> fib(1) -> fib(0)<br />-> fib(3) -> fib(2) -> fib(1) -> fib(0)<br />-> fib(1)

### Problem 1 - Merge K Arrays (Min Heap)

1. Implemented the merge k arrays of question 1 in the file 'problem_1.py'.
   <br />
   ```python
   def merge_k_arrays(arrays):
    for i in range(len(arrays)): # c1*(k+1)
        heap.append((arrays[i][0], i, 0)) # c2*k
    for i in range(len(heap)//2, -1, -1): # c3*(k+1)/2
        heapify(heap, i) # c4*k*log(k)/2
    sorted_array = [] # c5
    while heap: # c6*(k*n+1)
        min_element, i, j = heappop(heap) # c7*k*n*log(k)
        sorted_array.append(min_element) # c8*k*n
        if j+1 < len(arrays[i]): # c9*k*n
            heappush(heap, (arrays[i][j+1], i, j+1)) # c10*k*n*log(k)
    return sorted_array
    ```
    <br />Run with following command:
    ```
    python3 problem_1.py
    ```
2. Time Complexity:
   * The time taken for each line is shown in the comments above.
   * The heapify and heappush operations are recursive and have a running time of $$T(k) = T(k/2) + c$$ and with the master theorem, we get $$T(k) = Θ(lg(k))$$
   * Every heappop operation will run the heapify operation and some other non recursive, non repetitive operations. Hence the heapify and heappop operations share the same time complexity.
   * The while loop will run $$k\*n + 1$$ times, and the heappop and heappush operations will run $$k\*n$$ times.
   * Every other non recursive operation will run at most $$c\*k\*n$$ times and therefore they will not affect the overall time complexity.
   Therefore, the time complexity is determined by the number of times the recursive functions will run inside the while loop:<br />
   $$T(n,k) = c_7\*k\*n\*lg(k) + c_{10}\*k\*n\*lg(k) + Θ(k\*n)$$
   $$\Rightarrow T(n, k) = c\*k\*n\*lg(k) + Θ(k\*n)$$
   $$\Rightarrow T(n, k) = Θ(k\*n\*lg(k))$$
   

### Problem 2 - Remove Duplicates from array

1. Implemented the remove duplicates of question 2 in the file 'problem_2.py'.
   <br />
   ```python
   def remove_duplicates(array):
    for i in range(len(array)-1, 0, -1): # - c1*(n+1)
        if array[i] == array[i-1]: # - c2*n
            array.pop(i)
    ```
    <br />Run with following command:
    ```
    python3 problem_2.py
    ```
2. Time Complexity:
   The runtime would be calculated with the following summation formula:
    <br />
    $$T(n) = \sum_{i=1}^{n+1} c_1 + \sum_{i=1}^{n} c_2$$
    $$\Rightarrow T(n) = c_1*(n+1) + c_2*n$$
    $$\Rightarrow T(n) = (c_1+c_2)*n + c_1$$
   $$\Rightarrow T(n) = Θ(n)$$