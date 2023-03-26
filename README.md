# Binary-search-algorithm-
Binary search algorithm in python

This binary search algorithm is using the iteration method (see below pseudo code)

Iteration Method

  binarySearch(arr, x, low, high)
      repeat till low = high
             mid = (low + high)/2
                 if (x == arr[mid])
                 return mid

                 else if (x > arr[mid]) // x is on the right side
                     low = mid + 1

                 else                  // x is on the left side
                     high = mid - 1
                     
![image](https://user-images.githubusercontent.com/107822013/227797993-2ea347e0-f0f8-49f0-986d-2e24805d6d6d.png)

