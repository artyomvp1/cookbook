def insertion(sequence):
    
    for i in range(0, len(sequence)):
        current_value = sequence[i]
        prev_min_index = i - 1
        
        while prev_min_index >= 0 and sequence[prev_min_index] > current_value:
            sequence[prev_min_index+1] = sequence[prev_min_index]
            prev_min_index -= 1
            sequence[prev_min_index+1] = current_value
        
    return sequence


# Explanation TBD
