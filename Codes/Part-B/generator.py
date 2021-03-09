#!/puzzle

from flask import jsonify
import random
import json
import copy

import binaryStringGenerator as binStr
import rulesTableGenerator as rulesTable

################################################################################################
#                                     Population Generator
################################################################################################

def generate(population_size=2):

    no_bits = 8
    bin_string = binStr.binaryStringGen(no_bits)
    # print(bin_string)

    Initial_State, Goal_State = random.sample(bin_string, 2)

    # print(Initial_State)
    # print(Goal_State)

    rules_table = rulesTable.rulesTableGen()

    population = {0:{'Initial': Initial_State, 'Goal': Goal_State, 'Rules': rules_table}}

    count = 1
    while(count<population_size):
        rules_table = rulesTable.rulesTableGen()
        population[count] = {'Initial': Initial_State, 'Goal': Goal_State, 'Rules': rules_table}

        count += 1

    # print(population)

    with open("automata-population.json",'w') as o:
        o.write(json.dumps(population))









