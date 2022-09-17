def merge(sequence):
    
    if len(sequence) > 1:
        
        left = sequence[:len(sequence) // 2]
        right = sequence[len(sequence) // 2:]

        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sequence[k] = left[i]
                k += 1
                i += 1
            else:
                sequence[k] = right[j]
                k += 1
                j += 1

        if i < len(left):
            sequence[k] = left[i]
            k += 1
            i += 1

        if j < len(right):
            sequence[k] = right[j]
            k += 1
            j += 1

        return sequence
