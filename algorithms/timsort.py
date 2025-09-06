def timsort(arr):
    steps = []
    min_run = 32

    def insertion_sort(subarr, start, end):
        for i in range(start + 1, end + 1):
            key = subarr[i]
            j = i - 1
            while j >= start and subarr[j] > key:
                subarr[j + 1] = subarr[j]
                steps.append((subarr[:], [j, j+1]))
                j -= 1
            subarr[j + 1] = key
            steps.append((subarr[:], [j+1]))

    def merge(left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid+1:right+1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                steps.append((arr[:], [k]))
                i += 1
            else:
                arr[k] = R[j]
                steps.append((arr[:], [k]))
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            steps.append((arr[:], [k]))
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            steps.append((arr[:], [k]))
            j += 1
            k += 1

    n = len(arr)
    # Step 1: sort small chunks with insertion sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: merge sorted runs
    size = min_run
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(n-1, left+size-1)
            right = min((left + 2*size - 1), n-1)
            if mid < right:
                merge(left, mid, right)
        size *= 2

    return steps, len(steps)
