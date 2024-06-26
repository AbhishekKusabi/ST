def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binarySearch(arr, target)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
        
if __name__ == "__main__":
    main()