import random
import json
import copy
import numpy as np
import matplotlib.pyplot as plt
################################################################################################
#                                   Name: Akhil Movva                                          #
#                                     ID: 40106477                                             #
#                                 Assignment - 2 Part A                                        #
################################################################################################
import generator as gen
import fitnessEval as fit
import puzzleDraw as pd

import sortPopulation as sort
import parentSelection as parentSel
import crossover as cros
import mutation as mut
import survivalSelection as survivalSel
import diversity as div


pop_size = 300
gen_size =200
seed_size = 3
      

def calFitness(population):
    count = 0
    while(count<pop_size):
        
        fit.fitnessEval(population[str(count)])
 
        # with open("population.json",'w') as o:
        #     o.write(json.dumps(population))
            
        count +=1
    
    return population

############################### Main Code ###################################
    
fit_max_seed_avg = np.zeros(gen_size)
fit_mean_seed_avg = np.zeros(gen_size)
initial_div = []
final_div = []
#random.seed(100) 
#random.seed(300)
#random.seed(103) 
for s in range(seed_size):

    gen.generate(pop_size, sol=True)
    
    with open("solution.json",'r') as f:
        solution = json.loads(f.read())
        pd.draw2(json.dumps(solution),"Solution")
     
    with open("population.json",'r') as o:
        main_population = json.loads(o.read())
        #pd.draw2(json.dumps(main_population["0"]),"Initial")
         
    fit_max_gen = []
    fit_mean_gen = []
    
    initial_div.append(div.measureDiversity(main_population, pop_size))
     
    for g in range(gen_size):

        
        population = calFitness(main_population) # Update pop with fitness values
            
        sorted_dict= sort.sortPopulation(population, pop_size)
        
        
        all_popupulation = copy.deepcopy(sorted_dict)  
        
        # print("------------------- Parent Selection----------------------")
        
        sampled_pop = parentSel.uniformParentSelection(all_popupulation, pop_size)
        #sampled_pop = parentSel.expParentSelection(all_popupulation, pop_size)
        #sampled_pop = parentSel.fitnessbasedParentSelection(all_popupulation, pop_size)
        
        # print("------------------- Crossover----------------------")          
        
        crossover_pop = cros.discreteCrossover(sampled_pop, pop_size)
        #crossover_pop = cros.intermediateCrossover(sampled_pop, pop_size)
        cross_cal_pop = calFitness(crossover_pop)    
        # cross_sort_pop = sort.sortPopulation(cross_cal_pop, pop_size)
    
        # print("--------------------- Mutation ----------------------")

        sigma = pop_size / (g+(pop_size/10))
                           
        if( g > round(gen_size//1.5)):
            res = fit_max_gen[-10:]
            set_res = set(res)
            if(len(set_res)<4):
                sigma = 5
                
        
        mutated_pop = mut.nonUniformMutation(cross_cal_pop, sigma, pop_size)
        #mutated_pop = mut.simpleMutation(cross_cal_pop, pop_size)
        mut_cal_pop = calFitness(mutated_pop) 
        # mut_sort_pop = sort.sortPopulation(mut_cal_pop, pop_size)
        
        # print("--------------------- Survival Selection ----------------------")
    
        #survival_pop = survivalSel.survivorSelONFitness(population, mut_cal_pop, pop_size)     
        survival_pop = survivalSel.survivorSelONCrowding(population, mut_cal_pop, pop_size)
        sur_sort_pop = sort.sortPopulation(survival_pop, pop_size)
        
  
        fit_max_gen.append(sur_sort_pop["0"]['fitness'])
        fit_mean_gen.append((sum(d['fitness'] for d in sur_sort_pop.values() if d))/pop_size )    
        
        print(" SEED " + str(s)+" GEN " + str(g)+" fitness : "+" = "+str(sur_sort_pop["0"]['fitness']))
        #pd.draw2(json.dumps(sur_sort_pop["0"]),str(g))
        
        main_population = copy.deepcopy(sur_sort_pop)
    
    
    with open("final_population.json",'w') as o:
         o.write(json.dumps(sur_sort_pop))
    
    
    x_axis = np.arange(0, gen_size).tolist()
    plt.figure()
    plt.plot(x_axis, fit_max_gen)
    plt.legend(['max per gen'])
    
    plt.figure()
    plt.plot(x_axis, fit_max_gen)
    plt.legend(['avg per gen'])
    
    
    plt.figure()
    pd.draw2(json.dumps(sur_sort_pop["0"]),str(g))  
    
    fit_max_seed_avg = np.vstack((fit_max_seed_avg, fit_max_gen))
    fit_mean_seed_avg  = np.vstack((fit_mean_seed_avg, fit_mean_gen))
    
    final_div.append(div.measureDiversity(sur_sort_pop, pop_size))
    
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

print("Initial diversity "+str(initial_div)+" Final diversity "+str(final_div))

 

        




