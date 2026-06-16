import matplotlib.pyplot as plt
import numpy as np
import math 

# to create initial centers
#c_available = []
#for i in range(3):
    #c = [0, 0, 0]
    #rand_idx = np.random.choice([0, 1, 2], size=3)
    #c[rand_idx] = np.random.choice([0,1, -1])

c_0 = (0,0,0) # this is what a center means. 

occupied_centers = {c_0 , (1,0,0), (0,1,0), (0,0,1),(2,0,0)}
# Initializing parameter values
## available parameter values
#par_values = [1, 0]

# Running the algorithm
#N = 10 # number of iterations


#for i in range(N):
    #p = np.random.choice(par_values, size=3) # gives us a random array of parameter values for 3 different paramters. Index 0 = x, Index 1 = y and Index 2 = z
# print(p)
    # p = [1, 1, 1]

    #directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    #active_centers = occupied_centers.copy()

    #for j, par in enumerate(p):
        #axis_of_interest = directions[2*j:2*j+2]
        #if par == 0:
            #continue
        #else:
            #candidate_sites = []
            #for cx, cy, cz in active_centers:
                #for dx, dy, dz in axis_of_interest:
                    #neighbor = (cx + dx, cy + dy, cz +dz)
                    #if neighbor not in occupied_centers:
                        #candidate_sites.append([(cx, cy, cz),neighbor]) 
            
            #new_center =  candidate_sites[np.random.choice(len(candidate_sites))]
            #occupied_centers.add(new_center[1]) 
            #active_centers.remove(new_center[0])
            #active_centers.add(new_center[1])
            
        #print(active_centers)
load = {}
Load_Limit = 1
for ox, oy, oz in occupied_centers:
    load[(ox, oy, oz)] = 1 #initializing every cube with a load equal to 1
#sorting the cubes from largest to smallest (descending order) to easily find the base cubes
sorted_centers = sorted(
    occupied_centers,
    key=lambda c:c[2],
    reverse=True
)
for centers in sorted_centers:
    x, y, z = centers
    supports =[]
    for sx in [-1,0,1]:
        for sy in [-1,0,1]:
            possibility = (
                x+sx,
                y+sy,
                z-1
            )
            if possibility in occupied_centers:
                supports.append(possibility)
        #print(supports)
    if not supports:
        continue
        #print(supports)
    portion = load[(x, y, z)]/len(supports) #equally distributes weight amongst all support cubes
    for support in supports:
        load[support] += portion #calculates how much load the base or support cubes experience
#print(load)

min_z = min(c[2] for c in occupied_centers)
base_cubes = []
acceptable = []
for cube in occupied_centers:
    if cube[2] == min_z:
        base_cubes.append(cube)
        #print(ratio)
        if load[cube] <= Load_Limit:
            acceptable.append(cube)
base_loads = [load[cube] for cube in base_cubes]
a = len(acceptable)/len(base_cubes) #calculates proportion of base cubes under the stress limit
b = np.average(base_loads)/max(base_loads)

Structural_Constraint_1 = 0.5*(a+b)
print(Structural_Constraint_1)
#print(a)
#print(b)
#print(base_loads)
#print(base_cubes)
#for cube in base_cubes:
    #print(cube, load[cube])
#print(a)    