def max_heapify(sequence, sequence_length, node_index):
    
    left = 2 * node_index + 1
    right = 2 * node_index + 2
    
    if left < sequence_length and sequence[left] > sequence[node_index]:
        largest = left
    else:
        largest = node_index
    
    if right < sequence_length and sequence[right] > sequence[largest]:
        largest = right
    
    if largest != node_index:
        sequence[largest], sequence[node_index] = sequence[node_index], sequence[largest]
        max_heapify(sequence, sequence_length, largest)
        
    
def build_heap(sequence):
    
    for i in range(len(sequence), -1, -1):
        max_heapify(sequence, len(sequence), i)
    
    for j in range(len(sequence)-1, 0, -1):
        sequence[0], sequence[j] = sequence[j], sequence[0]
        max_heapify(sequence, j, 0)
    

sequence = [5, 23, 33, 31, 12, 1, 1, 4, 56]
build_heap(sequence)
print(sequence)
