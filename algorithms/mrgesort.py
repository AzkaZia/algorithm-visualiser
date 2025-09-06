def merge_sort(arr):
    steps = []
    comparisons = 0

    def merge(left, right, start_index):
        nonlocal comparisons
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            # highlight elements being compared
            steps.append((arr[:], [start_index + i, start_index + len(left) + j]))

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def sort(sub_arr, start_index):
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        left = sort(sub_arr[:mid], start_index)
        right = sort(sub_arr[mid:], start_index + mid)

        merged = merge(left, right, start_index)

        # update the original array to reflect the merge
        arr[start_index:start_index + len(merged)] = merged
        # record state after merge
        steps.append((arr[:], list(range(start_index, start_index + len(merged)))))
        return merged

    sort(arr, 0)
    return steps, comparisons
