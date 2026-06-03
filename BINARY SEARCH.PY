"""BINARY SEARCH"""

"""Find the middle element of the array.
Compare the middle element with the target key. If equal: return index.
If the key is smaller: search the left half.
If the key is larger: search the right half.
Repeat until the element is found or the search space is empty."""

def Binary_Search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # Key not found

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low=0
high=len(arr)-1
key=int(input("Enter the key to search: "))
result=Binary_Search(arr, low, high, key)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

