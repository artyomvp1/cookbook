def bubble(sequence):
    
    sorted = True
    
    while sorted:
        sorted = False
        
        for i in range(0, len(sequence)-1):
            if sequence[i] > sequence[i+1]:
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
                sorted = True
    
    return sequence
  
