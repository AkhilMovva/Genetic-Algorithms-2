import collections
import json
import copy

################################################################################################
#                           Sorting the population based on Fitness
################################################################################################

def sortPopulation1(population, p_size):
    
    sort_pop = collections.OrderedDict(sorted(population.items(), key=lambda t:t[1]["fitness"], reverse=False))

    output_dict = json.loads(json.dumps(sort_pop))
    sorted_pop = copy.deepcopy(output_dict)

    count = 0
    while(count<p_size):

        p = list(sorted_pop.keys())[count]
        output_dict[str(p_size+count)] = output_dict.pop(str(p))
        count +=1
 
    sorted_pop = copy.deepcopy(output_dict)  
    count = 0
    while(count<p_size):

        p = list(sorted_pop.keys())[count]
        output_dict[str(count)] = output_dict.pop(str(p))
        count +=1
   
    return output_dict


def sortPopulation(population, p_size):
    

    sorted_dic =copy.deepcopy(population)
    values = list(population.values())
    
    sorted_list = sorted(values, key = lambda i: i['fitness']) 
    
    #print(sorted_list)
    
    count = 0
    while(count<p_size):
    
        sorted_dic[str(count)] = sorted_list[count]
        count +=1
        
    #print(sorted_dic)
    
    return sorted_dic