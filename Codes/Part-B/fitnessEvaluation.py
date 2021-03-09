import json
import minEditDistance as MED

################################################################################################
#                                     Fitness Evaluation
################################################################################################


def fitness(final_state, ind_obj):
   goal_state  = ind_obj['Goal']
    
   minEditDis =MED.minEditDist(goal_state, final_state)
   
   fitness = int(minEditDis)
   
   ind_obj.update({'fitness': fitness})
   
   return json.dumps({'fitness': fitness})
    
    