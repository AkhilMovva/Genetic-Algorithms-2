import random
import numpy as np

################################################################################################
#                                     Non Uniform Mutation
################################################################################################

def nonUniformMutation(population_mut, sigma, pop_size):
    
    count = 1
    while(count<pop_size):
        ind = key, val = random.choice(list(population_mut.items()))
        
        rot_rate = 0.4
        mut_rate = 0.2
        
        if(sigma == 5):
           rot_rate = 0.2
           mut_rate = 0.4
    
        mu = 0.5
        
        pieces = ind[1]['puzzle']
        # l = ind[1]['length']
        # w = ind[1]['width']
        new_pieces=[]
        for p in pieces:
            rotated = False
            
            ran_value=np.random.uniform(0,1)
            if(rot_rate>ran_value):
 
                t=p[2]
                p[2]=p[3]
                p[3]=t
                
                rotated = True
                new_pieces.append(p)
            
            if (rotated==False):
                new_pieces.append(p)
        population_mut[str(ind[0])]['puzzle']=new_pieces
        
        new_pieces=[]     
        for p in pieces:
            changed = False
            ran_value2=np.random.uniform(0,1)
            if(mut_rate>ran_value2):
                p[0]= round(p[0]+np.random.normal(mu, sigma))
                p[1]= round(p[1]+np.random.normal(mu, sigma))
                
                changed = True
                new_pieces.append(p)
                
            if(changed==False):
                new_pieces.append(p)
             
        population_mut[str(ind[0])]['puzzle']=new_pieces
        
        count+=1

    return population_mut   

################################################################################################
#                                     Uniform Mutation
################################################################################################

def simpleMutation(population_mut, pop_size):
    
    count = 1
    while(count<pop_size):
        ind = key, val = random.choice(list(population_mut.items()))
        
        rot_rate = 0.3
        mut_rate = 0.3

        
        pieces = ind[1]['puzzle']
        # l = ind[1]['length']
        # w = ind[1]['width']
        new_pieces=[]
        for p in pieces:
            rotated = False
            
            ran_value=np.random.uniform(0,1)
            if(rot_rate>ran_value):
 
                t=p[2]
                p[2]=p[3]
                p[3]=t
                
                rotated = True
                new_pieces.append(p)
            
            if (rotated==False):
                new_pieces.append(p)
        population_mut[str(ind[0])]['puzzle']=new_pieces
        
        new_pieces=[]     
        for p in pieces:
            changed = False
            ran_value2=np.random.uniform(0,5)
            ran_value3=np.random.uniform(0,5)
            if(mut_rate>ran_value2 or mut_rate>ran_value3):
                p[0]= round(p[0]+ran_value2)
                p[1]= round(p[1]+ran_value3)
                
                changed = True
                new_pieces.append(p)
                
            if(changed==False):
                new_pieces.append(p)
             
        population_mut[str(ind[0])]['puzzle']=new_pieces
        
        count+=1

    return population_mut   