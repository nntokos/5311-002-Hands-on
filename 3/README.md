# CSE 5311-002 - Hands On 3

Implementing merge sort algorithms:
<br /> Run with following command:
  ```
  python3 merge_sort.py
  ```

The input is: A = [5, 2, 4, 7, 1, 3, 2, 6]

### Benchmarks

1. System Specifications:
   1. CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
   2. RAM: 16 GB LPDDR5 
   3. OS: MacOS Sonoma 14.0
   4. Python version: 3.9.7


2. Time taken for each algorithm is measured with the `timeit` module in Python.
   * __Merge Sort__ for A: 1.29*10^-5 s


3. The memory usage is measured using tracemalloc, which is a built-in Python module that measures the size of the memory blocks allocated to the program. Only measures the memory used by objects.
This metric does not include the memory used by the array itself, since it is irrelevant to the algorithm. However, every time memory is allocated within the algorithm, it is measured.
Because tracemalloc interferes with the time measurement (that is increases the time consumed to execute the sort algorithm), the two measurement were done separately.
   * __Merge Sort__ for A: 1840 B