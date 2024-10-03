def min_changes_to_periodic(M, dna):
    L = len(dna)
    min_changes = float('inf')
      
    for P in range(1, M + 1):
        changes = 0
               
        for start in range(P):
            count = [0] * 4  
           
            for i in range(start, L, P):
                if dna[i] == 'A':
                    count[0] += 1
                elif dna[i] == 'C':
                    count[1] += 1
                elif dna[i] == 'G':
                    count[2] += 1
                elif dna[i] == 'T':
                    count[3] += 1
                    
            max_count = max(count)           
            total_elements = (L - start + P - 1) // P           
            changes += total_elements - max_count
                   
        min_changes = min(min_changes, changes)

    return min_changes

M = int(input())
dna = input().strip()

result = min_changes_to_periodic(M, dna)

print(result)

