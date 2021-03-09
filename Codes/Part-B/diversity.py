import math

################################################################################################
#                                    Diversity Measure
################################################################################################

def euclideanDis(point1, point2):
    
    return ((((point1-point2)**2))**0.5)

def distanceFinder(rule1, rule2):

    points1=[]
    points2=[]
    dis_var=0
    
    count=0
    while(count<32):
        l=rule1[count][1]
        points1.append(l)
        count+=1
    count=0
    while(count<32):
        b=rule2[count][1]
        points2.append(b)
        count+=1
    
    count=0
    while(count<32):
        dis_cal = euclideanDis(points1[count], points2[count])
        dis_var = dis_var + dis_cal
        
        count+=1
    
    return dis_var


def measureDiversity(population, pop_size):
    
    value = 0
    i = 0
    while(i<pop_size):

        ind_rul1 = population[str(i)]['Rules']
        dis1 = 0
        j=0
        while(j<i):
            
            ind_rul2 = population[str(j)]['Rules']
            
            d = distanceFinder(ind_rul1, ind_rul2)
            
            dis1 = d + dis1
            
            j+=1
        
        sq = math.sqrt(dis1)
        
        value = sq + value
        
        i+=1

    value = value/pop_size
        
    return value