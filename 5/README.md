# CSE 5311-002 - Hands On 5

__System Specifications:__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.0
* Python version: 3.9.7

### Min Heap Data Structure

1. Implemented the build_min_heap function to build a min heap from a given list of variables.
    <br />Run with following command:
    ```
    python3 min_heap.py
    ```
<br>The implementation has the following functionality:
* Build min heap from a list of variables (build_min_heap)
* Heapify the list to maintain the min heap property (min_heapify). This is the essence of building a min heap.
* Pop the minimum element from the heap (min_heappop) and reheapify the list to maintain the min heap property.
* The algorithm can take any data structure that recognizes the less than operator.
* Examples used:
   * List of integers
    * List of floats
    * List of characters
    * Pop the minimum element from the int heap

