import random
import numpy as np
import copy
import math

################################################################################################
#                             Uniform Random Parent Selection
################################################################################################

def uniformParentSelection(all_population, pop_size): 

    pop_copy=copy.deepcopy(all_population)
    pop_values = list(pop_copy.values())
    random.shuffle(pop_values)
    
    count = 0
    while(count<pop_size):

        all_population[str(count)] = pop_values[count]
        count +=1
    
    return all_population
    
################################################################################################
#                             Exponential Parent Selection
################################################################################################

def expParentSelection(all_population, pop_size):
    
    p=pop_size
    exp_list=[]
    c= p-((math.exp(-p) - 1)/(math.exp(-1)-1))
    count=0
    while(count<p):
        
        rank = (1-math.exp(-count))/c
        exp_list.append(rank)
        count+=1
    exp_list.reverse()     
    pop_all_keys = list(all_population.values())
    #print(pop_all)
    selected_pop50 = np.random.choice(pop_all_keys, p, p=exp_list, replace = True)
    
    count = 0
    while(count<pop_size):

        all_population[str(count)] = selected_pop50[count]
        count +=1
    
    return all_population

################################################################################################
#                             fitness based Parent Selection
################################################################################################

def fitnessbasedParentSelection(all_population, pop_size):

    cost=[]
    for i in range (pop_size):
        cost.append(all_population[str(i)]['fitness'])
    
    choices = list(all_population.values())
    weights = np.array(cost)
    normalized_weights = weights / np.sum(weights)
    normalized_weights[np.isnan(normalized_weights)] = 0
    normalized_weights= normalized_weights[::-1] 
    
    number_of_choices = pop_size
    resample_counts = np.random.multinomial(number_of_choices, normalized_weights)
    
    chosen = []
    resample_index = 0
    for resample_count in resample_counts:
        for _ in range(resample_count):
            chosen.append(choices[resample_index])
        resample_index += 1
    
    count = 0
    while(count<pop_size):

        all_population[str(count)] = chosen[count]
        count +=1
    
    return all_population
    
