import random
import json
import copy
import numpy as np
import matplotlib.pyplot as plt
################################################################################################
#                                   Name: Akhil Movva                                          #
#                                     ID: 40106477                                             #
#                                 Assignment - 2 Part B                                        #
################################################################################################

import generator as gen
import minEditDistance as MED
import operations as opt
import sortPopulationOnFitness as sort
import selection as select
import crossover as cros
import mutation as mut
import diversity as div

pop_size = 80
gen_size = 50
seed_size = 3
pass_size = 5
mut_rate = 0.2
cross_rate = 0.8

final_states_list =[]
np.seterr(divide='ignore', invalid='ignore')

def updatePopulation(population) :

    #print(population1)
    
    pop_orginal = copy.deepcopy(population)
      
    pop_count =0 
    while((pop_count<pop_size)): 
    
        ind=pop_orginal[str(pop_count)]
        states_list=opt.operation(pop_orginal, ind, pop_size, pass_size)
        final_states_list.append(states_list)
       # print(states_list)
        
        pop_count +=1
        
    # with open("automata-population.json",'w') as o:
    #     o.write(json.dumps(pop_orginal))
    
    return pop_orginal



################################################################################################
#                                      MAIN PROGRAM
################################################################################################
    
#random.seed(100) 
fit_max_seed_avg = np.zeros(gen_size)
fit_mean_seed_avg = np.zeros(gen_size)

initial_div = []
final_div = []

for s in range(seed_size):
    
    gen.generate(pop_size)

    with open("automata-population.json",'r') as o:
        main_population = json.loads(o.read())

    initial_div.append(div.measureDiversity(main_population, pop_size))
    
    u1_pop =updatePopulation(main_population)
    
    print( " initial "+ str(s)+" "+str(u1_pop["0"]))
    
    fit_max_gen = []
    fit_mean_gen = []
    gen_count =0
    while (gen_count<gen_size):
     
        updatedpopulation =updatePopulation(main_population) #update pop with fitness values
        
        # print("############### updated Population #################")
        # temp_pop = copy.deepcopy(updatedpopulation)
        # for key, temp_pop in temp_pop.items():
        #     print(key)
        #     for attribute, value in temp_pop.items():
        #         print('{} : {}'.format(attribute, value))
                
        p_size=pop_size
        sortedPop = sort.sortPopulation(updatedpopulation, p_size)
        sortedPop2 = copy.deepcopy(sortedPop)
        
        # print("############### Parent Selection #################")

        selectedPop = select.uniformParentSelection(sortedPop, pop_size)
        #selectedPop = select.expParentSelection(sortedPop, pop_size)
        #selectedPop = select.fitnessbasedParentSelection(sortedPop, pop_size)
        
        # print("############### Crossover #################")
        
        #crossedPop = cros.onePointCrossover(sortedPop, pop_size, cross_rate
        #crossedPop = cros.nPointCrossover(sortedPop, pop_size, cross_rate)
        crossedPop = cros.uniformCrossover(sortedPop, pop_size, cross_rate)
        updatedPopulationFitness1 =updatePopulation(crossedPop)
        
        # print("############### Mutation #################")
        
        mutatedPop=mut.mutation(crossedPop, mut_rate, pop_size)
        updatedPopulationFitness2 =updatePopulation(mutatedPop)
        # print("############### Survival Selection #################")
        
        survivalPop = select.survivorSelONFitness(sortedPop2, updatedPopulationFitness2, pop_size)
        

        fit_max_gen.append(survivalPop["0"]['fitness'])
        fit_mean_gen.append((sum(d['fitness'] for d in survivalPop.values() if d))/pop_size )
        print(" SEED " + str(s)+" GEN " + str(gen_count)+" fitness : "+" = "+str(survivalPop["0"]['fitness']))
        main_population = copy.deepcopy(survivalPop)
                
        gen_count+=1
     
    with open("final-automata-population.json",'w') as o:
        o.write(json.dumps(survivalPop)) 
    
    print( " final "+str(s)+" "+str(survivalPop["0"]))
    
    x_axis = np.arange(0, gen_size).tolist()
    plt.figure()
    plt.plot(x_axis, fit_max_gen)
    plt.legend(['max s per gen'])
    
    plt.figure()
    plt.plot(x_axis, fit_max_gen)
    plt.legend(['avg s per gen'])
    
    fit_max_seed_avg = np.vstack((fit_max_seed_avg, fit_max_gen))
    fit_mean_seed_avg  = np.vstack((fit_mean_seed_avg, fit_mean_gen))
    
    final_div.append(div.measureDiversity(survivalPop, pop_size))

fit_max_seed_avg = np.delete(fit_max_seed_avg, (0), axis=0)
fit_max_seed_mean=fit_max_seed_avg.mean(axis=0)
fit_max_seed_std=fit_max_seed_avg.std(axis=0)

fit_mean_seed_avg = np.delete(fit_mean_seed_avg, (0), axis=0)
fit_mean_seed_mean=fit_mean_seed_avg.mean(axis=0)
fit_mean_seed_std=fit_mean_seed_avg.std(axis=0)
       
x_axis = np.arange(0, gen_size).tolist()
plt.figure()
plt.plot(x_axis, fit_max_seed_mean)
plt.legend(['max s mean per gen'])

plt.figure()
plt.plot(x_axis, fit_max_seed_std)
plt.legend(['max s std per gen'])

plt.figure()
plt.plot(x_axis, fit_mean_seed_mean)
plt.legend(['avg s mean per gen'])

plt.figure()
plt.plot(x_axis, fit_mean_seed_std)
plt.legend(['avg s std per gen'])

#print(fit_max_gen)
#print(final_states_list)

print("initial_div "+str(initial_div)+" final_div "+str(final_div))