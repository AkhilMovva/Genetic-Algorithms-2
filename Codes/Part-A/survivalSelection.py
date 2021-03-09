import numpy as np
import copy
import sortPopulation as sort

################################################################################################
#                            Survival Selection Based on Fitness
################################################################################################

def survivorSelONFitness(parents_pop, offspring_pop, pop_size):
    
    count = 0
    temp_pop = copy.deepcopy(offspring_pop)
    while(count<pop_size):

        p = list(temp_pop.keys())[count]

        offspring_pop[str(pop_size+count)] = offspring_pop.pop(str(p))
    
        count +=1
    
    parents_pop.update(offspring_pop)
    parents_pop= sort.sortPopulation(parents_pop, 2*pop_size)
    # print(parents_pop)
    # res1 = dict(list(parents_pop.items())[pop_size:]) 
    res = dict(list(parents_pop.items())[:pop_size]) 

    return res

################################################################################################
#                            Survival Selection Using Crowding 
################################################################################################
    
def sortPuzzleLB(puzzle, pieces):
    
    weights=[]
    sortedpuzzle=[]
    count=0
    while(count<pieces):
        l=puzzle[count][2]
        b=puzzle[count][3]
        weights.append((l**2)+(b**2))
        count+=1
        
    sortedpuzzle = [x for _,x in sorted(zip(weights,puzzle))]
        
    return sortedpuzzle

def euclideanDis(point1, point2):
    
    return ((((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2))**0.5)

def distanceFinder(puzzle1, puzzle2, pieces):
    temp1=[]
    temp2=[]
    points1=[]
    points2=[]
    dis_var=0
    
    count=0
    while(count<pieces):
        l=puzzle1[count][0]
        b=puzzle1[count][1]
        temp1.append(l)
        temp1.append(b)
        points1.append(temp1)
        count+=1
    count=0
    while(count<pieces):
        l=puzzle2[count][0]
        b=puzzle2[count][1]
        temp2.append(l)
        temp2.append(b)
        points2.append(temp2)
        count+=1
    
    count=0
    while(count<pieces):
        dis_cal = euclideanDis(points1[count], points2[count])
        dis_var = dis_var + dis_cal
        
        count+=1
    
    return dis_var

def survivorSelONCrowding(parents_pop, offsprings_pop, pop_size):
    
    temp1 = copy.deepcopy(parents_pop)
    temp2 = copy.deepcopy(offsprings_pop)
    
    survivor_pop = copy.deepcopy(parents_pop)
    
    pieces = parents_pop[str(0)]['pieces']
    
    parent_pop_values = list(temp1.values())
    np.random.shuffle(parent_pop_values)
    count = 0
    while(count<pop_size):

        temp1[str(count)] = parent_pop_values[count]
        count +=1
    
    parents_pop= copy.deepcopy(temp1)
    
    offsprings_pop_values = list(temp2.values())
    np.random.shuffle(offsprings_pop_values)
    count = 0
    while(count<pop_size):

        temp2[str(count)] = offsprings_pop_values[count]
        count +=1
    
    offsprings_pop= copy.deepcopy(temp2)
    
    pop_count = 0
    while(pop_count<pop_size):

        parent1_puzzle = sortPuzzleLB(parents_pop[str(pop_count)]['puzzle'], pieces)
        parent2_puzzle = sortPuzzleLB(parents_pop[str(pop_count+1)]['puzzle'], pieces) 
        parent1_fitness = parents_pop[str(pop_count)]['fitness']
        parent2_fitness = parents_pop[str(pop_count+1)]['fitness']
                                       
        offspring1_puzzle = sortPuzzleLB(offsprings_pop[str(pop_count)]['puzzle'], pieces)
        offspring2_puzzle = sortPuzzleLB(offsprings_pop[str(pop_count+1)]['puzzle'], pieces) 
        offspring1_fitness = offsprings_pop[str(pop_count)]['fitness']
        offspring2_fitness = offsprings_pop[str(pop_count+1)]['fitness']
        
        direct_dis1 = distanceFinder(parent1_puzzle, offspring1_puzzle, pieces)
        direct_dis2 = distanceFinder(parent2_puzzle, offspring2_puzzle, pieces)
        
        cross_dis1 = distanceFinder(parent1_puzzle, offspring2_puzzle, pieces)
        cross_dis2 = distanceFinder(parent2_puzzle, offspring1_puzzle, pieces)

        if((direct_dis1+direct_dis2)<(cross_dis1+cross_dis2)):
            
            if(parent1_fitness>offspring1_fitness):              
                survivor_pop[str(pop_count)]['puzzle']= offsprings_pop[str(pop_count)]['puzzle']
            
            else:               
                survivor_pop[str(pop_count)]['puzzle']= parents_pop[str(pop_count)]['puzzle']
                                       
            if(parent2_fitness>offspring2_fitness):              
                survivor_pop[str(pop_count+1)]['puzzle']= offsprings_pop[str(pop_count+1)]['puzzle']
            
            else:                
                survivor_pop[str(pop_count+1)]['puzzle']= parents_pop[str(pop_count+1)]['puzzle']
                
            
        else:
            if(parent1_fitness>offspring2_fitness):              
                survivor_pop[str(pop_count)]['puzzle']= offsprings_pop[str(pop_count+1)]['puzzle']
            
            else:               
                survivor_pop[str(pop_count)]['puzzle']= parents_pop[str(pop_count)]['puzzle']
                                       
            if(parent2_fitness>offspring1_fitness):              
                survivor_pop[str(pop_count+1)]['puzzle']= offsprings_pop[str(pop_count)]['puzzle']
            
            else:                
                survivor_pop[str(pop_count+1)]['puzzle']= parents_pop[str(pop_count+1)]['puzzle']
               
        pop_count +=2 
    
    return survivor_pop

