#!/puzzle

from flask import jsonify
import random
import puzzleGenerator as gen
import shuffle2DPieces as shuffle
import json
import rotate as r
import copy

################################################################################################
#                                     Population Generator
################################################################################################

def generate(population_size=2, sol=False):
    l = random.randint(50, 200) #random length for the frame
    w = random.randint(20, int(l/2)) #random width for the frame
    p = random.randint(8, int(l/4)) #random number of pieces
    # l = 80
    # w = 40
    # p = 8
    puzzle,solution = gen.generate(l, w, p, sol) #generating random puzzle


    while len(solution) == 0: #changing the seed and repeating the steps if the puzzle is not generated
        puzzle, solution = gen.generate(l, w, p, sol)

    population = {0:{'length': l, 'width': w, 'pieces': p, \
             'puzzle': puzzle}}

    count = 1
    while(count<population_size):
        npuzzle = shuffle.scatter(copy.deepcopy(solution), l, w)
        npuzzle = r.rotate(npuzzle)
        population[count] = {'length': l, 'width': w, 'pieces': p, \
                 'puzzle': npuzzle}

        count += 1

    with open("population.json",'w') as o:
        o.write(json.dumps(population))

    solved = {'length': l, 'width': w, 'pieces': p, \
             'puzzle':solution}

    if sol:
        with open("solution.json",'w') as o:
            o.write(json.dumps(solved))


#if __name__ == "__main__":
#    generate()
