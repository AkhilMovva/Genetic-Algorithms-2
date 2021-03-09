import random
def split(rect):
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]

    if random.uniform(0,1)>0.5:
        t =  random.randint(2, int(x2/2))
        new_rect = [x1+t,y1,x2-t,y2]
        rect = [x1,y1,t,y2]
    else:
        t =  random.randint(2,int(y2/2))
        new_rect = [x1,y1+t,x2,y2-t]
        rect = [x1,y1,x2,t]

    return rect,new_rect
