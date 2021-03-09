import numpy as np

################################################################################################
#                       Minimum Edit distance between two strings
################################################################################################

def minEditDist(final_state, goal_state):
  fitness_table = np.zeros((len(final_state) + 1 , len(goal_state) + 1), dtype=int)

  for row in range(len(final_state)+1):
    fitness_table[row][0] = row
  for col in range(len(goal_state)+1):
    fitness_table[0][col] = col

  for row in range(len(final_state)+1):
    for col in range(len(goal_state)+1):
      if row != 0 and col != 0:  
        if final_state[row-1] == goal_state[col-1]:
          fitness_table[row][col] = fitness_table[row-1][col-1]
        else:
            fitness_table[row][col] = min(fitness_table[row-1][col] + 1,
                                          fitness_table[row][col-1] + 1,
                                          fitness_table[row-1][col-1] + 2
            )
  return fitness_table[len(final_state)][len(goal_state)]
  
# Driver program 
str1 = "10111101"
str2 = "0111101"
  
#print(minEditDist(str1, str2)) 