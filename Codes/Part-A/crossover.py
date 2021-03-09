import random
import numpy as np
import copy

################################################################################################
#                                    Discrete Uniform Crossover
################################################################################################

def discreteCrossover(sampled_pop, pop_size):

    pop_cross=copy.deepcopy(sampled_pop)
    pop_values = list(sampled_pop.values())
    random.shuffle(pop_values)
    ind_pieces =sampled_pop[str(0)]['pieces']
    count = 0
    while(count<pop_size):

        sampled_pop[str(count)] = pop_values[count]
        count +=1
    
    count0=0   

    while((count0)<((pop_size))):

        ind1_puzzle=sampled_pop[str(count0)]['puzzle']
        ind2_puzzle=sampled_pop[str(count0+1)]['puzzle']

        
        #print(ind1_puzzle)
        
        count=0
    
        while(count<ind_pieces):
            
            ind1_puzzle_piece = ind1_puzzle[count]
            ind1_x = ind1_puzzle_piece[0]
            ind1_y = ind1_puzzle_piece[1]
            ind1_L = ind1_puzzle_piece[2]
            ind1_B = ind1_puzzle_piece[3]
            
            count2=0
            while(count2<ind_pieces):
                
                ind2_L=ind2_puzzle[count2][2]
                ind2_B=ind2_puzzle[count2][3]
                if(ind1_L == ind2_L and ind1_B == ind2_B):
                    ind2_x=ind2_puzzle[count2][0]
                    ind2_y=ind2_puzzle[count2][1]
                    # print(pop_cross[str(count0)]['puzzle'])
                    pop_cross[str(count0)]['puzzle'][count][0] =ind2_x
                    pop_cross[str(count0)]['puzzle'][count][1] =ind2_y
                    pop_cross[str(count0+1)]['puzzle'][count][0] =ind1_x  
                    pop_cross[str(count0+1)]['puzzle'][count][1] =ind1_y
                    
                    break
                count2 +=1   
            
            count +=1
            
        count0 +=2
        
    
    return pop_cross

################################################################################################
#                                    Arthematic  Crossover
################################################################################################

def intermediateCrossover(sampled_pop, pop_size):

    pop_cross=copy.deepcopy(sampled_pop)
    pop_values = list(sampled_pop.values())
    random.shuffle(pop_values)
    ind_pieces =sampled_pop[str(0)]['pieces']
    count = 0
    while(count<pop_size):

        sampled_pop[str(count)] = pop_values[count]
        count +=1
    
    count0=0   

    while((count0)<((pop_size))):

        ind1_puzzle=sampled_pop[str(count0)]['puzzle']
        ind2_puzzle=sampled_pop[str(count0+1)]['puzzle']

        
        #print(ind1_puzzle)
        
        count=0
    
        while(count<ind_pieces):
            
            ind1_puzzle_piece = ind1_puzzle[count]
            ind1_x = ind1_puzzle_piece[0]
            ind1_y = ind1_puzzle_piece[1]
            ind1_L = ind1_puzzle_piece[2]
            ind1_B = ind1_puzzle_piece[3]
            
            count2=0
            while(count2<ind_pieces):
                u=np.random.uniform(0,1)
                ind2_L=ind2_puzzle[count2][2]
                ind2_B=ind2_puzzle[count2][3]
                if(ind1_L == ind2_L and ind1_B == ind2_B):
                    ind2_x=ind2_puzzle[count2][0]
                    ind2_y=ind2_puzzle[count2][1]
                    # print(pop_cross[str(count0)]['puzzle'])
                    c1_x = round((ind1_x * u)+ (ind2_x * (1-u)))  
                    c1_y = round((ind1_y * u)+ (ind2_y * (1-u)))
                    c2_x = round((ind1_x * (1-u))+ (ind2_x * u))
                    c2_y = round((ind1_y * (1-u))+ (ind2_y * u))
            
                    pop_cross[str(count0)]['puzzle'][count][0] =c1_x
                    pop_cross[str(count0)]['puzzle'][count][1] =c1_y
                    pop_cross[str(count0+1)]['puzzle'][count][0] =c2_x
                    pop_cross[str(count0+1)]['puzzle'][count][1] =c2_y
                    
                    break
                count2 +=1   
            
            count +=1
            
        count0 +=2
        
    
    return pop_cross