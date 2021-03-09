import matplotlib.pyplot as plt
import json
import os
import time
import datetime;

path = os.getcwd()

################################################################################################
#                                     Puzzle Plotting
################################################################################################

def draw2(jsonInput, plotTitle):
    obj = json.loads(jsonInput)
    pieces = obj['puzzle']
    plt.axes()

    rectangle = plt.Rectangle((0, 0), obj['length'], obj['width'], ec="yellow")
    plt.gca().add_patch(rectangle)
    for i in pieces:
        x1 = i[0]
        y1 = i[1]
        x2 = i[2]
        y2 = i[3]
        rectangle = plt.Rectangle((x1, y1), x2, y2, fc='blue', ec="red")
        plt.gca().add_patch(rectangle)

    plt.axis('scaled')
    plt.title(plotTitle)
    plt.show()
   

