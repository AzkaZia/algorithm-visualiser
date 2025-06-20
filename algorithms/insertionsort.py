def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Visualize initial comparison
        steps.append((arr[:], [i, j]))

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            steps.append((arr[:], [j, j + 1]))  # visualize the shift
            j -= 1

        arr[j + 1] = key
        steps.append((arr[:], [j + 1, i]))  # visualize insertion

    return steps
