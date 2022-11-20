"""
https://www.youtube.com/watch?v=g-PGLbMth_g

Два FOR лупа, первый устанавливай текуший индекс, второй пробегает по всем значеним выше этого индекса. 
Во время второго индекса, если значение текущего индекса больше значения второго индекса, то устанавливается новый текущий индекс.
Когда второй цикл пробежал по всем значениям, первый физически меняет местами значение первого индекса со вторым.
"""
def selection(sequence):
    
    for i in range(0, len(sequence)):
        current_index = i
        
        for j in range(i+1, len(sequence)):
            if sequence[current_index] > sequence[j]:
                current_index = j
        
        sequence[current_index], sequence[i] = sequence[i], sequence[current_index]
    
    return sequence
