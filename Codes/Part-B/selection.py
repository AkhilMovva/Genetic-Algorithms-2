import math
import numpy as np
import random
import copy
import collections
import sortPopulationOnFitness as sort

################################################################################################
#                             Uniform Random Parent Selection
################################################################################################

def uniformParentSelection(all_popupulation, pop_size): 
    p=pop_size
    pop_copy=copy.deepcopy(all_popupulation)
    pop_values = list(pop_copy.values())
    random.shuffle(pop_values)
    
    count = 0
    while(count<pop_size):

        all_popupulation[str(count)] = pop_values[count]
        count +=1
    
    return all_popupulation

################################################################################################
#                             Exponential Parent Selection
################################################################################################

def expParentSelection(all_popupulation, pop_size):
    p=pop_size
    exp_list=[]
    c= p-((math.exp(-p) - 1)/(math.exp(-1)-1))
    count=0
    selected_pop50=[]
    while(count<p):
        
        rank = (1-math.exp(-count))/c
        exp_list.append(rank)
        count+=1
    exp_list.reverse()    
    pop_all_values = list(all_popupulation.values())
    #print(pop_all_values)
    selected_pop50 = np.random.choice(pop_all_values, p,p=exp_list, replace = True)
    
    count = 0
    while(count<pop_size):

        all_popupulation[str(count)] = selected_pop50[count]
        count +=1
    
    
    return all_popupulation

################################################################################################
#                             fitness based Parent Selection
################################################################################################

def fitnessbasedParentSelection(all_popupulation, pop_size):
    p=pop_size
    exp_list=[]

    selected_pop50=[]
    
    pd=[]
    cost=[]
    for i in range (pop_size):
        cost.append(all_popupulation[str(i)]['fitness'])
    
    # pd=np.true_divide(cost,sum(cost))
    # pd[np.isnan(pd)] = 0
    # pd=list(pd)
    # pd.reverse()
    # pop_all_values = list(all_popupulation.values())
    # #print(pop_all_values)
    # selected_pop50 = np.random.choice(pop_all_values, p,p=pd, replace = True)
    
    choices = list(all_popupulation.values())
    weights = np.array(cost)
    normalized_weights = weights / np.sum(weights)
    normalized_weights[np.isnan(normalized_weights)] = 0
    normalized_weights= normalized_weights[::-1] 
    
    number_of_choices = pop_size
    resample_counts = np.random.multinomial(number_of_choices,
                                            normalized_weights)
    
    chosen = []
    resample_index = 0
    for resample_count in resample_counts:
        for _ in range(resample_count):
            chosen.append(choices[resample_index])
        resample_index += 1
    
    
    
    count = 0
    while(count<pop_size):

        all_popupulation[str(count)] = chosen[count]
        count +=1
    
    
    return all_popupulation



################################################################################################
#                            Survival Selection Based on Fitness
################################################################################################
    

def survivorSelONFitness(parents_pop, offspring_pop, pop_size):
    
    count = 0
    temp_parent_pop = copy.deepcopy(parents_pop)
    temp_parent_pop = sort.sortPopulation(temp_parent_pop, pop_size)
    temp_pop = sort.sortPopulation(offspring_pop, pop_size)
    temp_pop = copy.deepcopy(offspring_pop)
    while(count<pop_size):

        p = list(temp_pop.keys())[count]

        offspring_pop[str(pop_size+count)] = offspring_pop.pop(str(p))
    
        count +=1
    
    parents_pop.update(offspring_pop)
    sorted_pop = sort.sortPopulation(parents_pop, 2*pop_size)
    # print(parents_pop)
    # res1 = dict(list(parents_pop.items())[pop_size:]) 
    res = dict(list(sorted_pop.items())[:pop_size]) 

    
    return res
##############################################################################

