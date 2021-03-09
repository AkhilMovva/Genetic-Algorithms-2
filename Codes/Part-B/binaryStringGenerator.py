from itertools import product

################################################################################################
#                   Binary String Generator based on No. of Bits
################################################################################################

def binaryStringGen(noof_bits):
	n=noof_bits
# generate product in reverse lexicographic order
	bin_str = [''.join(p) for p in product('10', repeat=n)]
# ['111', '110', '101', '100', '011', '010', '001', '000']    
# sort by number of ones
	bin_str.sort(key=lambda s: s.count('1')) 

	return bin_str