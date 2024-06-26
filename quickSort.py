def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = []
        greater = []
        
        for i in array[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        
        return quicksort(less) + [pivot] + quicksort(greater)

def main():
    print(quicksort([10, 5, 2, 3]))
    
if __name__ == "__main__":
    main()
