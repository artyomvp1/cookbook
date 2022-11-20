# v1
def insertion(sequence):
    
    for i in range(1, len(sequence)):
        current_value = sequence[i]
        current_position = i
        
        while current_position > 0 and sequence[current_position-1] > current_value:
            sequence[current_position] = sequence[current_position-1]
            current_position -=1
        
        sequence[current_position] = current_value
    
    return sequence


# v2
def insertion(sequence):
    
    for i in range(0, len(sequence)):
        current_value = sequence[i]
        prev_min_index = i - 1
        
        while prev_min_index >= 0 and sequence[prev_min_index] > current_value:
            sequence[prev_min_index+1] = sequence[prev_min_index]
            prev_min_index -= 1
            sequence[prev_min_index+1] = current_value
        
    return sequence
