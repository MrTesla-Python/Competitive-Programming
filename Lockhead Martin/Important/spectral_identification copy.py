import math
import itertools

def backtrack(remaining, elements, wavelengths, tol=1):
    if not remaining:
        return []
    
    for element in elements:

        temp_remaining = remaining[:]
        matches = []
       
        for exp in wavelengths[element]:
            found = False
            
            for rep in sorted(temp_remaining):
                if abs(exp - rep) <= tol:
                    matches.append(rep)
                    temp_remaining.remove(rep)
                    found = True
                    break
            if not found:
                break  
        if len(matches) == len(wavelengths[element]):
            
            remaining_elements = [e for e in elements if e != element]
            sol = backtrack(temp_remaining, remaining_elements, wavelengths, tol)
            if sol is not None:
                return [element] + sol
    return None

T = int(input())
atomic_order = {
    "H": 1,
    "He": 2,
    "O2": 8,
    "Na": 11,
    "Mg": 12,
    "Ca": 19,  
    "Ca+": 20,  
    "Ti+": 22,
    "Fe": 26,
    "Ni": 28,
    "Hg": 80
}
wavelengths = {
    "H" : [410.175, 486.134, 656.281],
    "He" : [587.562],
    "O2" : [627.661, 686.719, 759.370, 822.696, 898.765],
    "Na" : [588.995, 589.592],
    "Mg" : [516.733, 517.270, 518.362],
    "Ca" : [430.774],
    "Ca+" : [393.368, 396.847],
    "Ti+" : [336.112],
    "Fe" : [302.108, 358.121, 382.044, 430.790, 438.355, 466.814, 495.761, 516.891, 527.039],
    "Ni" : [299.444],
    "Hg" : [546.073]
}

for _ in range(T):
    wave_r = list(map(int, input().split()))
    wave_r.sort()
    
    
    sorted_elements = sorted(wavelengths.keys(), key=lambda x: (atomic_order[x], 0 if x=="Ca" else (1 if x=="Ca+" else 0)))
    
    solution = backtrack(wave_r, sorted_elements, wavelengths)
    if solution is not None:
        
        solution = sorted(solution, key=lambda x: (atomic_order[x], 0 if x=="Ca" else (1 if x=="Ca+" else 0)))
        print(" ".join(solution))
    else:
        print("No valid identification")
