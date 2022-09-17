def selection(sequence):
    
    for i in range(0, len(sequence)):
        current_index = i
        
        for j in range(i+1, len(sequence)):
            if sequence[current_index] > sequence[j]:
                current_index = j
        
        sequence[current_index], sequence[i] = sequence[i], sequence[current_index]
    
    return sequence
