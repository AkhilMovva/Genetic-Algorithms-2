import numpy as np 
import random
import copy
import math

################################################################################################
#                           One Point Crossover
################################################################################################

def onePointCrossover(sampled_pop, pop_size, cross_rate):

   # cross_rate = 1
    
    pop_values = list(sampled_pop.values())
    np.random.shuffle(pop_values)
    count = 0
    while(count<pop_size):

        sampled_pop[str(count)] = pop_values[count]
        count +=1
    
    pop_cross= copy.deepcopy(sampled_pop)
    
    pop_count=0  
    #temp_var=0
    while(pop_count<pop_size and (pop_size-pop_count)>1):

        ind1_rules = sampled_pop[str(pop_count)]['Rules']
        ind2_rules = sampled_pop[str(pop_count+1)]['Rules']
        
        r = random.randint(1,31)
        if(cross_rate>np.random.uniform(0,1)):

            off1_rules = ind1_rules[0:r] + ind2_rules[r:32]
            off2_rules = ind2_rules[0:r] + ind1_rules[r:32]
            
            pop_cross[str(pop_count)]['Rules'] = off1_rules
            pop_cross[str(pop_count+1)]['Rules'] = off2_rules
        
        #temp_var=pop_count
        pop_count +=2
        
    return pop_cross    


################################################################################################
#                           N Point Crossover
################################################################################################

def nPointCrossover(sampled_pop, pop_size, cross_rate):  
    
   # cross_rate = 1
    
    n=6
    pop_values = list(sampled_pop.values())
    np.random.shuffle(pop_values)
    count = 0
    while(count<pop_size):

        sampled_pop[str(count)] = pop_values[count]
        count +=1
    
    pop_cross= copy.deepcopy(sampled_pop)
    
    pop_count=0  
    #temp_var=0
    while(pop_count<pop_size and (pop_size-pop_count)>1):

        ind1_rules = sampled_pop[str(pop_count)]['Rules']
        ind2_rules = sampled_pop[str(pop_count+1)]['Rules']
        

        r = random.sample(range(1, 32), n)
        r.sort()
        
        if(cross_rate>np.random.uniform(0,1)):
        
            off1_rules = ind1_rules[0:r[0]] +ind2_rules[r[0]:r[1]] +ind1_rules[r[1]:r[2]] +ind2_rules[r[2]:r[3]] +ind1_rules[r[3]:r[4]] +ind2_rules[r[4]:r[5]] +ind1_rules[r[5]:32]
            off2_rules = ind2_rules[0:r[0]] +ind1_rules[r[0]:r[1]] +ind2_rules[r[1]:r[2]] +ind1_rules[r[2]:r[3]] +ind2_rules[r[3]:r[4]] +ind1_rules[r[4]:r[5]] +ind2_rules[r[5]:32]
            
            pop_cross[str(pop_count)]['Rules'] = off1_rules
            pop_cross[str(pop_count+1)]['Rules'] = off2_rules
        
        #temp_var=pop_count
        pop_count +=2
        
        
    
    return pop_cross 


################################################################################################
#                           Uniform Crossover
################################################################################################


def uniformCrossover(sampled_pop, pop_size, cross_rate):  
    
    #cross_rate= 0.5
    
    n=6
    pop_values = list(sampled_pop.values())
    np.random.shuffle(pop_values)
    count = 0
    while(count<pop_size):

        sampled_pop[str(count)] = pop_values[count]
        count +=1
    
    pop_cross= copy.deepcopy(sampled_pop)
    
    pop_count=0  
    while(pop_count<pop_size and (pop_size-pop_count)>1):
        ind1_rules = sampled_pop[str(pop_count)]['Rules']
        ind2_rules = sampled_pop[str(pop_count+1)]['Rules']
        
        new_rules1=[]
        new_rules2=[]
        
        rule_count =0
        while(rule_count<32):
            ran_value =np.random.uniform(0,1)
            if(ran_value<cross_rate):
                new_rules1.append(ind1_rules[rule_count])
                new_rules2.append(ind2_rules[rule_count])
            else:
                new_rules1.append(ind2_rules[rule_count])
                new_rules2.append(ind1_rules[rule_count])
            
            rule_count+=1
        
        pop_cross[str(pop_count)]['Rules'] = new_rules1
        pop_cross[str(pop_count+1)]['Rules'] = new_rules2
        
        pop_count +=2
    
    return pop_cross 
    
    
    
    