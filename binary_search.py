# Binary search algorithm
# Version 3


def binary_search(array, x):
    low = 0
    high = len(array) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if array[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif array[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

def main(): 
    # Test array
    test_array = [2,3,4,10,40]
    x = 10
     
    result = binary_search(test_array, x)

    if result != -1:
        print(test_array)
        print("The element searched: ", x)
        print("Element is present at index", str(result))
        print()
    else:
        print(test_array)
        print("The element searched: ", x)
        print("Element is not present in array")
        print()

    # Should print :present at index 3:

    # Test array 2
    test_array_2 = [1,1,2,4,5]
    x = 1

    result = binary_search(test_array_2, x)

    if result != -1:
        print(test_array_2)
        print("The element searched: ", x)
        print("Element is present at index", str(result))
        print()
    else:
        print(test_array_2)
        print("The element searched: ", x)
        print("Element is not present in array")
        print()

    # Should print :present at index 0: 

    # Test array 3
    test_array_3 = [1,2,3,4,5,6,8,9,10]
    x = 5

    result = binary_search(test_array_3, x)

    if result != -1:
        print(test_array_3)
        print("The element searched: ", x)
        print("Element is present at index", str(result))
        print()
    else:
        print(test_array_3)
        print("The element searched: ", x)
        print("Element is not present in array")
        print()

    # Should print :present at index 4:

    # Test array 4
    test_array_4 = [1,2,3,4,5,6,8,9,10]
    x = 15

    result = binary_search(test_array_4, x)
     
    if result != -1:
        print(test_array_4)
        print("The element searched: ", x)
        print("Element is present at index", str(result))
        print()
    else:
        print(test_array_4)
        print("The element searched: ", x)
        print("Element is not present in array")
        print()

    # Should print :not present in the array:

main()
