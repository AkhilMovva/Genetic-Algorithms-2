import random
import copy

import binaryStringGenerator as binStr

################################################################################################
#                           Rule Table Generator
################################################################################################

def rulesTableGen():
    no_bits=5
    bin_str = binStr.binaryStringGen(no_bits)
    count=0
    rules_table=[]
    while(count<32):
        r = random.randint(0, 3)
        rules_table.append([bin_str[count],r])

        count+=1

    return rules_table
