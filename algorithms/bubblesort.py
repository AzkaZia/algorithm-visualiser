def bubble_sort(arr):
    steps = [] #this records steps for visualisation
    n = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False
        for i in range(n):
            steps.append((arr[:], [i, i + 1]))  # record comparison
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                steps.append((arr[:], [i, i +1])) # record after swap
        n -= 1

    return steps