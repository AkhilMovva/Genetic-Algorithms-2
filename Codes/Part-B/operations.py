import copy

import generator as gen
import minEditDistance as MED
import fitnessEvaluation as fit

################################################################################################
#                        Operations based on the Rule Table
################################################################################################

############ Rules #############

# 0 - replace the middle value with 0
# 1 - replace the middle value with 1
# 2 - delete the middle value
# 3 - replicate the middle value with left

def rulesPass(rule, current_state_sub):
 
    inter = current_state_sub
    #print(inter)
    count=5
    
    if( rule == 0 ):
        inter[2] = '0'
    if( rule == 1 ):
        inter[2] = '1'    
    if( rule == 2 ):
        inter.pop(2)
    if( rule == 3 ):
        p = inter[2]
        inter.insert(2,p) 
    
    next_state_sub = ''.join(inter)
    
    return next_state_sub

def replaceONPosition(position, substring5, fullstring):
    next_state_sub_list = list(substring5)
    next_state_full_list = list(fullstring)
    
    list1 = next_state_full_list
    list2 = next_state_sub_list
    L = len(list1)
    B = len(list2)
    final = []
    position = position
    
    count=0
    while(count <= position and L > B and position < L):
        inside=0
        pos=count
        p=L-4
        if(L>4 and B==6):
            fin = list2 + list1[(pos+B):]
            fin2 = list1[:pos] +list2 + list1[(pos+B-1):]
    
            t=len(fin2)
            if(t>L+1):
                t1=len(fin2[L+1:])
                fin3=fin2[L+1:]+fin2[t1:L+1]
                inside =1
                
        if(L>4 and B==5):
            fin = list2 + list1[(pos+B):]
            fin2 = list1[:pos] +list2 + list1[(pos+B):]
    
            t=len(fin2)
            if(t>L):
                t1=len(fin2[L:])
                fin3=fin2[L:]+fin2[t1:L]
                inside =1
        
        if(L>4 and B==4):
            fin = list2 + list1[(pos+B):]
            fin2 = list1[:pos] +list2 + list1[(pos+B+1):]
            
            t=len(fin2)
            if(t>L-1):
                t1=len(fin2[L-1:])
                fin3=fin2[L-1:]+fin2[t1:L-1]
                inside =1
    
        if(inside==0):
            #print(str(count)+" - "+str(fin2))
            final = fin2
        else:
            #print(str(count)+" - "+str(fin3)) 
            final = fin3
        count+=1
        
    if( L == B or L == 5):
        list1 = list2
        final = list1
        #print(final)
    
    if( L < B and L < 5):
        final = list1
        #print(final)
    

    #final_str= ''.join(final)

    
    return final

def findRule(individual_rules, current_state):
    
    search = ''.join(current_state)
    current_rule=next(elem[1] for elem in individual_rules if search in elem)
    
    # print("find rule "+str(current_rule)+" current_state "+str(current_state))
    
    return current_rule

def selectFive(current_list, position):
    
    list1 = current_list
    L=len(list1)
    position = position
    sub=[]
    count=0
    while(count <= position and position < L and L > 5):
        pos = count   
        
        if(pos<L-4):
            sub = list1[pos:pos+5]
            #print(sub) 
        if(pos>=L-4):
            p=len(list1[pos:])
            sub = list1[pos:]+ list1[:5-p]
            #print(sub)      
        
        count+=1
    
    if(L==5):
        sub = list1
    
    #print(sub)
    return sub

def operation(pop_orginal, ind, pop_size, pass_size):
    Initial_state = pop_orginal['0']['Initial']
    Goal_state = pop_orginal['0']['Goal']
    ind_rules=ind['Rules']
    
    forprint =0
     
    solution = 0
    rules_list = []
    final_states_list =[]

    final_state = ''
    
    current_state =list(Initial_state)
    c_ln = len(current_state)
    const1 = len(current_state)*pass_size
    state_count = 0
    while(state_count < const1 and solution == 0): 
        
        ln_CS=len(current_state)
        current = copy.deepcopy(current_state)
        current_copy = copy.deepcopy(current)
        
        c_ln = len(current_copy)
             
        slide_count=0
        while(slide_count < c_ln and solution==0 and c_ln > 4): 
            flag=0
            #print("slide_count ="+str(slide_count)+"  current ="+str(current_copy))
            if(len(current)>4):
                origi5 = selectFive(current, slide_count)
                rule = findRule(ind_rules, origi5)
                if(len(current_copy)>4):
                    ln_diff=len(current)-len(current_copy)
                    if(ln_diff>0):
                        currt5 = selectFive(current_copy, slide_count-ln_diff)
                        next_step4_5_6 = rulesPass(rule, currt5)
                        temp_list = replaceONPosition(slide_count-ln_diff, next_step4_5_6, current_copy)
                    elif(ln_diff<0):
                        currt5 = selectFive(current_copy, slide_count-ln_diff)
                        next_step4_5_6 = rulesPass(rule, currt5)
                        temp_list = replaceONPosition(slide_count-ln_diff, next_step4_5_6, current_copy)
                    else:
                        currt5 = selectFive(current_copy, slide_count)
                        next_step4_5_6 = rulesPass(rule, currt5)
                        temp_list = replaceONPosition(slide_count, next_step4_5_6, current_copy)
                    
                    
                    
                    current_copy=copy.deepcopy(temp_list) 
                    
                else:
                    current_copy = current_copy
                
            #print("origi5 -"+str(origi5))
                      
            #rules_list.append(rule)
            #print("current_copy "+ str(current_copy))    
            minEditDis =MED.minEditDist(Goal_state, ''.join(current_copy))
            fit.fitness(''.join(current_copy), ind)
            
            if(minEditDis==0):
                solution = 1
                # print("-------------Successfull Solution Found--------------")
                # print("fitness 0 for "+str(current_copy))
                forprint=1
            
            
            slide_count +=1
        # print("minEditDis ------------------------------"+str(minEditDis))    
        current_state = copy.deepcopy(current_copy)
        
        final_states_list.append(''.join(current_copy))
              
        #print("current_state "+ str(current_state))
        state_count += ln_CS
        
        # if(forprint==1):
        #    print("-------------Successfull Solution Found--------------")
        
        #print(rules_list)
    return final_states_list
            
        
        

    
    
    